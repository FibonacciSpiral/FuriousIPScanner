import platform
import subprocess
from _winapi import CREATE_NO_WINDOW

from PyQt5.QtCore import pyqtSignal

from abstract_worker import AbstractWorker


class PingWorker(AbstractWorker):
    error = pyqtSignal(str)
    def __init__(self, model, _ipAddress):
        super().__init__()
        self.Context = model
        self.ipAddress = _ipAddress

    def run(self):
        if self.ipAddress is not None:
            self.multiPing(self.ipAddress, 0)
        self.Finished.emit()

    def ping(self, host):
        """
        Returns True if host (str) responds to a ping request.
        Remember that a host may not respond to a ping (ICMP) request even if the host name is valid.
        """

        self.printx("Pinging {} with 32 bytes of data:".format(host))

        # Option for the number of packets as a function of
        param = '-n' if platform.system().lower() == 'windows' else '-c'

        # Building the command. Ex: "ping -c 1 google.com"
        command = ['ping', param, '1', host]

        result = subprocess.run(command, creationflags=CREATE_NO_WINDOW, stdout=subprocess.PIPE)
        output = result.stdout.decode('utf8')
        if "Request timed out." in output or "100% packet loss" in output or "Destination host unreachable." in output:
            return False
        return True

    def multiPing(self, host, currentProgress):
        response = None
        successCount = 0
        for i in range(4):
            response = self.ping(host)
            if currentProgress <= 85:
                self.Progress.emit(currentProgress + 15)
                currentProgress += 25
            if response != 0:
                successCount += 1
            else:
                self.printx("Request timed out.")
        if successCount >= 3:
            self.printx("You are connected to {}!".format(host))
        else:
            self.printx("Not connected to {}, please check power and ethernet connections.".format(host))
        return response

