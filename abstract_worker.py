from abc import abstractmethod

from PyQt5.QtCore import QObject, pyqtSignal, QThread


# import logging

# The path to the csv file

class AbstractWorker(QObject):
    Finished = pyqtSignal()
    Progress = pyqtSignal(int)
    TextOutput = pyqtSignal(str)
    DebugOutput = pyqtSignal(str)
    data = pyqtSignal(list)
    error = pyqtSignal(str)
    failed = pyqtSignal(bool)

    def __init__(self):
        super().__init__()
        self.Thread = QThread()

    def printx(self, mes):
        self.TextOutput.emit(mes)

    def debugOut(self, mes):
        self.DebugOutput.emit(mes)

    def WorkerComplete(self):
        self.TextOutput.emit("Task complete.")
        self.TextOutput.emit("_______________________________________________________________")
        self.Progress.emit(0)


    def WorkerError(self):
        self.TextOutput.emit("Task failed.")
        self.TextOutput.emit("_______________________________________________________________")
        self.Progress.emit(0)


    @abstractmethod
    def run(self):
        pass