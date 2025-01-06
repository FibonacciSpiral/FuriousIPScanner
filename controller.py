import ipaddress

from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator, QValidator

from ping_sweep_worker import PingSweepWorker
from ping_worker import PingWorker
from abstract_worker import AbstractWorker
from model import Model

from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
                          QRect, QSize, QUrl, Qt)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
                         QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
                         QRadialGradient, QStandardItem)
from PyQt5.QtWidgets import *


# The controller has knowledge of both the view and the model and it's only real job is to
# hook up commands to buttons. The controller would normally define some kind of command,
# but it doesn't necessarily have to come up with its own function to connect to a button
# any function works!

class Controller:

    def __init__(self, view, model):
        self.View = view
        self.Model: Model = model
        self.View.UpdateProgressBar(0)
        self.UpdateMessage("Eagerly awaiting furious IP scan. View results here!")
        self.UpdateMessage("__________________________________________")
        # setting up some validation for text boxes
        # this is a regular expression
        ipRange = "(([_0]+)|([_0]*[0-9]_*)|([0-9][0-9]_)|([_0][0-9][0-9])|(1[0-9][0-9])|([2][0-4][0-9])|(25[0-5]))"
        ipRegex = QRegExp("^" + ipRange
                          + "\\." + ipRange
                          + "\\." + ipRange
                          + "\\." + ipRange + "$")
        self.ipValidator = QRegExpValidator(ipRegex)
        self.View.ipEditFirst.setValidator(self.ipValidator)
        self.View.ipEditLast.setValidator(self.ipValidator)
        self.View.ipEditFirst.setInputMask("000.000.000.000;_")
        self.View.ipEditLast.setInputMask("000.000.000.000;_")

        cidrRange = "([\/]0?[1-9]|[\/][12][0-9]|[\/]3[0-2])$"
        cidrRegex = QRegExp("^" + cidrRange)
        self.cidrValidator = QRegExpValidator(cidrRegex)

        self.subnetDetectionMethods = []
        for i in range(self.View.subnetOptions.count()):
            self.subnetDetectionMethods.append(self.View.subnetOptions.itemText(i))
        self.subnetOptionChanged(self.View.subnetOptions, self.View.subnetEdit)

        self.pingResults = []
        self.ConnectSignalsAndSlots()

    # Here every button and slot is mapped to a function or a slot
    def ConnectSignalsAndSlots(self):
        ####################################################################################################
        # here we are hooking up the actual commands to the buttons. Pressing a button will start a thread
        # that will run the desired command. lambdas are used to easily pass function pointers.
        ####################################################################################################

        self.View.pingSweepBtn.clicked.connect(self.beginPingSweep)
        self.View.ipEditFirst.textChanged.connect(
            lambda: self.pingSweepIPValidator(self.View.ipEditFirst, self.View.ipEditLast, self.View.pingSweepBtn))

        self.View.ipEditLast.textChanged.connect(
            lambda: self.pingSweepIPValidator(self.View.ipEditFirst, self.View.ipEditLast, self.View.pingSweepBtn))

        self.View.subnetOptions.currentIndexChanged.connect(
            lambda: self.subnetOptionChanged(self.View.subnetOptions, self.View.subnetEdit))

    def beginPingSweep(self):
        self.View.DisableButtons()
        okayToContinue = True
        firstIP = self.View.ipEditFirst.text()
        lastIP = None   # just a default value
        ip_octetsFirst = firstIP.split('.')
        bit_count = 0
        # the list has all the names of the different options
        if self.subnetDetectionMethods[self.View.subnetOptions.currentIndex()] == "Subnet Mask":
            list = self.View.subnetEdit.text().split('.')
            ip_subnet_octets = []
            for octet in list:
                ip_subnet_octets.append(int(octet))
        else:
            ip_subnet_octets = None

        # if we are using a subnet mask...
        if self.subnetDetectionMethods[self.View.subnetOptions.currentIndex()] == "Subnet Mask":
            for subnet in ip_subnet_octets:
                if subnet == 255:
                    bit_count += 8
                else:
                    mask = 0x80
                    while mask != 0x0:
                        if (int(subnet) & mask) == mask:
                            bit_count += 1
                            mask = mask >> 1
                        else:
                            break  # no more bits to count

        elif self.subnetDetectionMethods[self.View.subnetOptions.currentIndex()] == "CIDR Notation":
            cidrInput = str(self.View.subnetEdit.text())
            bit_count = int(cidrInput.lstrip('/'))
        else:  # here we automatically detect the subnet using math!
            lastIP = self.View.ipEditLast.text()
            ip_octetsLast = lastIP.split('.')
            for (first, last) in zip(ip_octetsFirst, ip_octetsLast):
                if first != last:
                    if (int(last) - int(first)) < 0:
                        self.UpdateMessage(
                            "IP Range is negative. For the first octet, please enter an address that is on a lower subnet than the end of range address.")
                        okayToContinue = False
                    mask = 0x01
                    while mask != 0x100:
                        if (int(first) & mask) == (int(last) & mask) and (int(first) & mask) == mask and (
                                int(last) & mask) == mask:
                            bit_count += 1
                            mask = mask << 1
                        else:
                            break  # no more bits to count
                    break

                else:
                    bit_count += 8

        max_ip = lastIP
        if okayToContinue is True:
            self.launchPingSweep(firstIP, bit_count, max_ip)
        else:
            self.EnableButtons()

    def validateIPAddress(self, IP, button=None):
        if self.Model.taskRunning is False:
            ip_octets = IP.split('.')
            valid = True
            if len(ip_octets) == 4:
                for item in ip_octets:
                    if item == '':
                        valid = False
            else:
                valid = False
            if valid is True:
                if button is not None:
                    button.setEnabled(True)
            else:
                if button is not None:
                    button.setEnabled(False)
            return valid

    def pingSweepIPValidator(self, IP1edit, IP2edit, buttonToEnable):
        valid = False
        if self.validateIPAddress(IP1edit.text()) and self.validateIPAddress(IP2edit.text()):
            valid = True

        if buttonToEnable is not None:
            buttonToEnable.setEnabled(valid)

    def EnableButtons(self):
        # enables all buttons, use when a thread is active
        self.View.pingSweepBtn.setEnabled(True)

    def CountThreads(self):
        self.Model.totalThreadsRunning -= 1
        if self.Model.totalThreadsRunning == 0:
            self.Model.taskFinished()
            self.EnableButtons()
            self.Model.totalThreadsRunning = 0
            self.View.UpdateProgressBar(0)
            for result in self.pingResults:
                self.UpdateMessage(result)

    def queueUpPingResults(self, resultListOfStrings):
        for string in resultListOfStrings:
            self.pingResults.append(string)

    def launchPingSweep(self, ip_address, numberOfBits, maximumIPAddress):
        self.View.DisableButtons()
        self.Model.taskRunning = True
        self.Model.totalThreadsRunning = 0
        self.Model.totalThreadsStarted = 0
        self.pingResults = []
        numberOfOctets = int(numberOfBits / 8)
        bitsInOctet = int(numberOfBits % 8)
        subnetRemainder = 0
        mask = 1
        for i in range(8):
            if i < bitsInOctet:
                subnetRemainder |= mask
                mask <<= 1
            else:
                subnetRemainder <<= 1
        # if numberOfOctets == 4:
        #     numberOfOctets = 3

        # this will look at the subnet calculated and set any host bits to 0.
        ip_octets = ip_address.split('.')
        new_ip_octet_list = []
        for (octet, i) in zip(ip_octets, range(4)):
            if i == numberOfOctets:
                new_ip_octet_list.append(str(int(octet) & subnetRemainder))
            elif i > numberOfOctets:
                new_ip_octet_list.append('0')
            else:
                new_ip_octet_list.append(octet)

        editted_ip_address = "{}.{}.{}.{}".format(new_ip_octet_list[0], new_ip_octet_list[1], new_ip_octet_list[2], new_ip_octet_list[3])

        # /24 for example. the IPv4Network function accepts CIDR notation only
        subnet = "/" + str(numberOfBits)
        list_of_ip = [str(ip) for ip in ipaddress.IPv4Network(editted_ip_address + subnet)]

        # this ensures that the IP range selected with auto will actually just test the range
        # the other subnet options are not really about a range. They just test the whole subnet
        if self.subnetDetectionMethods[self.View.subnetOptions.currentIndex()] == "Use IP Range":
            minimumIPAddress = ip_address
            listOfOctetsForMinimumIP = minimumIPAddress.split('.')
            listOfOctets = maximumIPAddress.split('.')
            new_ip_list = []
            for ip in list_of_ip:
                ipAsList = ip.split('.')
                addToList = True

                for min, max, amount in zip(listOfOctetsForMinimumIP, listOfOctets, ipAsList):
                    if int(min) <= int(amount) <= int(max):
                        addToList = True
                    else:
                        addToList = False
                        break
                if addToList is True:
                    new_ip_list.append(ip)

            list_of_ip.clear()
            list_of_ip = new_ip_list.copy()
        sub_lists = [list_of_ip[x:x + 1] for x in range(0, len(list_of_ip), 1)]
        for item in sub_lists:
            worker = PingSweepWorker(self.Model, item)
            worker.signals.TextOutput.connect(self.UpdateMessage)
            worker.signals.DebugOutput.connect(print)
            worker.signals.Progress.connect(self.View.UpdateProgressBar)
            worker.signals.Finished.connect(self.CountThreads)
            worker.signals.data.connect(self.queueUpPingResults)
            self.Model.threadpool.start(worker)
            # makes a count of threads that way we can track progress with precision
            self.Model.totalThreadsRunning += 1
            self.Model.totalThreadsStarted += 1

    # Creates a worker and thread that will carry out a task
    def startWorkerThread(self, Worker: AbstractWorker, callBack=None):
        if self.Model.taskRunning is not True:
            self.View.DisableButtons()
            self.Model.taskRunning = True
            self.Model.CurrentWorker = Worker
            self.Model.CurrentWorker.moveToThread(self.Model.CurrentWorker.Thread)
            # Connect signals and slots
            self.Model.CurrentWorker.Thread.started.connect(self.Model.CurrentWorker.run)

            self.Model.CurrentWorker.Finished.connect(self.Model.CurrentWorker.Thread.quit)
            self.Model.CurrentWorker.Finished.connect(self.Model.taskFinished)
            self.Model.CurrentWorker.Finished.connect(self.Model.CurrentWorker.WorkerComplete)
            self.Model.CurrentWorker.Finished.connect(self.EnableButtons)
            self.Model.CurrentWorker.Thread.finished.connect(self.Model.CurrentWorker.Thread.deleteLater)
            if callBack is not None:
                self.Model.CurrentWorker.Thread.finished.connect(callBack)

            self.Model.CurrentWorker.error.connect(self.Model.CurrentWorker.Thread.quit)
            self.Model.CurrentWorker.error.connect(self.Model.taskFinished)
            self.Model.CurrentWorker.error.connect(self.Model.CurrentWorker.WorkerError)
            self.Model.CurrentWorker.error.connect(self.EnableButtons)

            self.Model.CurrentWorker.Progress.connect(self.View.UpdateProgressBar)

            self.Model.CurrentWorker.TextOutput.connect(self.UpdateMessage)

            self.Model.CurrentWorker.DebugOutput.connect(print)

            self.Model.CurrentWorker.failed.connect(self.Model.processFailure)
            # Start the thread
            self.Model.CurrentWorker.Thread.start()

    def subnetOptionChanged(self, subnetOptions, subnetEdit):
        if self.subnetDetectionMethods[subnetOptions.currentIndex()] == "Subnet Mask":
            self.View.ipEditLast.setEnabled(False)
            subnetEdit.setEnabled(True)
            subnetEdit.setValidator(self.ipValidator)
            subnetEdit.setInputMask("000.000.000.000;_")
            subnetEdit.setPlaceholderText("255.255.255.0")
            subnetEdit.setText("255.255.255.0")
            #
        elif self.subnetDetectionMethods[subnetOptions.currentIndex()] == "CIDR Notation":
            self.View.ipEditLast.setEnabled(False)
            subnetEdit.setEnabled(True)
            subnetEdit.setPlaceholderText("/")
            subnetEdit.setInputMask("")
            subnetEdit.setValidator(self.cidrValidator)
            subnetEdit.setText("/24")

        else:
            self.View.ipEditLast.setEnabled(True)
            self.View.subnetEdit.setValidator(None)
            subnetEdit.setInputMask("")
            subnetEdit.setPlaceholderText("")
            subnetEdit.setEnabled(False)
            
    def UpdateMessage(self, string):
        # UpdateMessage updates the message on the bottom of the GUI with a string
        self.View.textBrowser.append(string)


