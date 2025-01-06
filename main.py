from PyQt5.QtWidgets import QApplication
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import QFile
from PyQt5.QtWidgets import QMainWindow

from view import Ui_MainWindow
from model import Model

from controller import Controller
import sys

# This is the program launcher for the EcoLink Automation Project (ELAP).

if __name__ == '__main__':
    """Main function."""
    # Create an instance of `QApplication`
    app = QApplication(sys.argv)
    # Show the GUI
    MainWindow = QMainWindow()
    view = Ui_MainWindow()
    view.setupUi(MainWindow)
    MainWindow.setWindowIcon(QtGui.QIcon('furious_emoji.ico'))
    qss = "TCobra.qss"
    with open(qss, "r") as fh:
        app.setStyleSheet(fh.read())
    MainWindow.show()
    model = Model()
    # Create instances of the model and the controller
    ctrl = Controller(view=view, model=model)
    # Execute calculator's main loop
    sys.exit(app.exec_())