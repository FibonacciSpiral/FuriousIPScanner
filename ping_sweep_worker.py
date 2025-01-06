import platform
import subprocess
from _winapi import CREATE_NO_WINDOW

from PyQt5.QtCore import pyqtSignal, QRunnable, pyqtSlot, QObject


class WorkerSignals(QObject):
    '''
    Defines the signals available from a running worker thread.

    Supported signals are:

    finished
        No data

    error
        tuple (exctype, value, traceback.format_exc() )

    result
        object data returned from processing, anything

    '''
    Finished = pyqtSignal()
    Progress = pyqtSignal(int)
    TextOutput = pyqtSignal(str)
    DebugOutput = pyqtSignal(str)
    data = pyqtSignal(list)
    FinishedWithResult = pyqtSignal(str)


class PingSweepWorker(QRunnable):
    ip_address_list = []

    def __init__(self, model, _ip_address_list):
        super(PingSweepWorker, self).__init__()
        self.Context = model
        self.ip_address_list = _ip_address_list
        self.signals = WorkerSignals()

    def ping(self, host):
        """
        Returns a valid response if host (str) responds to a ping request, else it will return None
        Remember that a host may not respond to a ping (ICMP) request even if the host name is valid.
        """
        # Option for the number of packets as a function of
        param = '-n' if platform.system().lower() == 'windows' else '-c'

        # Building the command. Ex: "ping -c 1 google.com"
        command = ['ping', param, '1', host]

        result = subprocess.run(command, creationflags=CREATE_NO_WINDOW, stdout=subprocess.PIPE)
        output = result.stdout.decode('utf8')
        if "Request timed out." in output or "100% packet loss" in output or "Destination host unreachable." in output:
            return None
        else:
            return output
    @pyqtSlot()
    def run(self):
        for ip in self.ip_address_list:
            self.signals.TextOutput.emit("Pinging {}".format(ip))
            response = self.ping(ip)
            if response is not None:
                response = self.ping(ip)
                if response is not None:
                    separator = "_________________________________________"
                    pingResponse = "Received response from {}!".format(ip)
                    self.signals.TextOutput.emit(pingResponse)
                    blueString = f"<p style='color:Cyan'>{pingResponse}</p>"
                    #self.signals.FinishedWithResult.emit(blueString)
                    whiteString =f"<p style='color:white'>{separator}</p>"
                    #self.signals.FinishedWithResult.emit(blackString)

                    data = []
                    data.append(response + separator)
                    data.append(blueString)
                    data.append(whiteString)

                    self.signals.data.emit(data)
        self.signals.Progress.emit(int((1.00 - float(self.Context.totalThreadsRunning) / float(self.Context.totalThreadsStarted)) * 100.00))
        self.signals.Finished.emit()