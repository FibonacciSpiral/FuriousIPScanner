# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FuriousIPScannerzCZUlk.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
                         QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
                         QRadialGradient, QStandardItem)
from PyQt5.QtWidgets import *

import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 750)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.verticalLayout_5 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.verticalLayoutWidget_2 = QWidget(self.splitter)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayout_4 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_3 = QLabel(self.verticalLayoutWidget_2)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)

        self.verticalLayout_3.addWidget(self.label_3)

        self.textEdit = QTextEdit(self.verticalLayoutWidget_2)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setReadOnly(True)

        self.verticalLayout_3.addWidget(self.textEdit)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.ipEditLast = QLineEdit(self.verticalLayoutWidget_2)
        self.ipEditLast.setObjectName(u"ipEditLast")

        self.gridLayout.addWidget(self.ipEditLast, 0, 3, 1, 1)

        self.label = QLabel(self.verticalLayoutWidget_2)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.ipEditFirst = QLineEdit(self.verticalLayoutWidget_2)
        self.ipEditFirst.setObjectName(u"ipEditFirst")

        self.gridLayout.addWidget(self.ipEditFirst, 0, 1, 1, 1)

        self.label_2 = QLabel(self.verticalLayoutWidget_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 1)

        self.pingSweepBtn = QPushButton(self.verticalLayoutWidget_2)
        self.pingSweepBtn.setObjectName(u"pingSweepBtn")

        self.gridLayout.addWidget(self.pingSweepBtn, 0, 4, 1, 1)

        self.subnetOptions = QComboBox(self.verticalLayoutWidget_2)
        self.subnetOptions.addItem("")
        self.subnetOptions.addItem("")
        self.subnetOptions.addItem("")
        self.subnetOptions.setObjectName(u"subnetOptions")

        self.gridLayout.addWidget(self.subnetOptions, 1, 1, 1, 1)

        self.subnetEdit = QLineEdit(self.verticalLayoutWidget_2)
        self.subnetEdit.setObjectName(u"subnetEdit")

        self.gridLayout.addWidget(self.subnetEdit, 1, 3, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        self.splitter.addWidget(self.verticalLayoutWidget_2)
        self.textBrowser = QTextBrowser(self.splitter)
        self.textBrowser.setObjectName(u"textBrowser")
        self.splitter.addWidget(self.textBrowser)

        self.verticalLayout_5.addWidget(self.splitter)

        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(24)

        self.verticalLayout_5.addWidget(self.progressBar)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Furious IP Scanner", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Welcome to Furious IP Scanner!!!", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Furious IP Scanner is a bare bones IP scanner that uses multithreaded processing to rapidly ping a range of hosts. The ping sweep feature was designed to be as fast as possible and has a very high accuracy rate. That said, if no results are found, please try once more to make sure the correct host is not actually there.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/resource/furious_emoji.png\" /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-lef"
                        "t:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Some instructions:</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">You may select a range of IP addresses and press start and the IP scanner will simply ping the whole range selected. For example: 192.168.6.4 to 192.168.7.6 will only ping the following addresses:</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">192.168.6.4</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text"
                        "-indent:0px;\"><span style=\" font-size:8pt;\">192.168.6.5</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">192.168.6.6</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">192.168.7.4</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">192.168.7.5</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">192.168.7.6</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-l"
                        "eft:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Ping the whole subnet by increasing the range all the way up to 255. </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Alternatively, you may simply select a subnet using a notation like 255.255.255.0 (subnet mask). </p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">OR you may use CIDR notation which looks like this /24. If you use either of these methods, the range is not used. The IP address entered on the far left (the beginning of "
                        "IP range) is used for the calculation of the subnet to ping. The IP address on the far right (the end of the IP range) is not actually used with those methods. It will become disabled.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">If any issues are found or if you have any neat ideas about how to improve Furious IP Scanner, please let Giselle Dockterburke know. My email is giselle.dockterburke@edwardsvacuum.com.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.ipEditLast.setText(QCoreApplication.translate("MainWindow", u"192.168.2.255", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"IP Range:", None))
        self.ipEditFirst.setText(QCoreApplication.translate("MainWindow", u"192.168.2.0", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"to:", None))
        self.pingSweepBtn.setText(QCoreApplication.translate("MainWindow", u"Start!", None))
        self.subnetOptions.setItemText(0, QCoreApplication.translate("MainWindow", u"Use IP Range", None))
        self.subnetOptions.setItemText(1, QCoreApplication.translate("MainWindow", u"CIDR Notation", None))
        self.subnetOptions.setItemText(2, QCoreApplication.translate("MainWindow", u"Subnet Mask", None))

    # retranslateUi

   # def CopyBtn_clicked(self):
   #      # CopyBtn copies the output in the text browser to the system clipboard
   #      self.textBrowser.selectAll()
   #      self.textBrowser.copy()
   #      self.UpdateMessage("Text is copied to system clipboard")

    '''Methods to Update UI Elements'''
    def UpdateTextBrowser(self, string):
        # UpdateTextBrowser updates the main text box with a string
        self.textBrowser.setText(string)


    def UpdateProgressBar(self, value):
        # UpdateProgressBar updates the chunk level of the progress bar and the number associated with it
        self.progressBar.setValue(value)

    def DisableButtons(self):
        self.pingSweepBtn.setEnabled(False)

