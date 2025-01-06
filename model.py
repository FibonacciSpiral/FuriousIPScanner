import os

from PyQt5.QtCore import QThreadPool


class Model:

    # Data and application helper functions will live in the model.
    # Workers are objects that carry out one specific task. Any functions that are used by only one worker
    # should be placed in the class definition of that worker.

    # workers are created in the controller but their instances are saved in the model
    normal_subnet = "192.168.2.0"
    dnet_subnet = "192.168.3.0"

    def __init__(self):
        # Worker objects live here. They are created as needed and when they are not, they are destroyed
        # they need a place to live, and the model is the default home for functions and data
        # do not try and access these during runtime. They may or may not exist
        self.DoNotContinue = False
        self.CurrentWorker = None
        self.taskRunning = False

        self.workingDirectory = os.getcwd()
        self.threadpool = QThreadPool()
        self.threadpool.setMaxThreadCount(256)
        self.totalThreadsRunning = 0
        self.totalThreadsStarted = 0
        self.threadsFinished = 0

    def taskFinished(self):
        self.taskRunning = False

    def processFailure(self, failed):
        self.DoNotContinue = failed