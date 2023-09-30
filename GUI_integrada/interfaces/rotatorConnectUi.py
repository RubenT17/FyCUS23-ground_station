# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interfaces\rotatorConnectWindows.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_rotatorConnect(object):
    def setupUi(self, rotatorConnect):
        rotatorConnect.setObjectName("rotatorConnect")
        rotatorConnect.resize(600, 300)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(rotatorConnect.sizePolicy().hasHeightForWidth())
        rotatorConnect.setSizePolicy(sizePolicy)
        rotatorConnect.setMinimumSize(QtCore.QSize(600, 300))
        rotatorConnect.setMaximumSize(QtCore.QSize(600, 300))
        self.gConnect = QtWidgets.QWidget(rotatorConnect)
        self.gConnect.setObjectName("gConnect")
        self.progressBar = QtWidgets.QProgressBar(self.gConnect)
        self.progressBar.setGeometry(QtCore.QRect(100, 230, 400, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.progressBar.setFont(font)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.boxOffset = QtWidgets.QLineEdit(self.gConnect)
        self.boxOffset.setGeometry(QtCore.QRect(240, 70, 120, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.boxOffset.setFont(font)
        self.boxOffset.setObjectName("boxOffset")
        self.btnConnect = QtWidgets.QPushButton(self.gConnect)
        self.btnConnect.setGeometry(QtCore.QRect(240, 150, 120, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnConnect.setFont(font)
        self.btnConnect.setObjectName("btnConnect")
        self.txtOffset = QtWidgets.QLabel(self.gConnect)
        self.txtOffset.setGeometry(QtCore.QRect(150, 70, 70, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.txtOffset.setFont(font)
        self.txtOffset.setObjectName("txtOffset")
        rotatorConnect.setCentralWidget(self.gConnect)
        self.menuBar = QtWidgets.QMenuBar(rotatorConnect)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 600, 22))
        self.menuBar.setObjectName("menuBar")
        self.actSerialPort = QtWidgets.QMenu(self.menuBar)
        self.actSerialPort.setObjectName("actSerialPort")
        rotatorConnect.setMenuBar(self.menuBar)
        self.actConfigure = QtWidgets.QAction(rotatorConnect)
        self.actConfigure.setObjectName("actConfigure")
        self.actSerialPort.addAction(self.actConfigure)
        self.menuBar.addAction(self.actSerialPort.menuAction())

        self.retranslateUi(rotatorConnect)
        QtCore.QMetaObject.connectSlotsByName(rotatorConnect)

    def retranslateUi(self, rotatorConnect):
        _translate = QtCore.QCoreApplication.translate
        rotatorConnect.setWindowTitle(_translate("rotatorConnect", "rotatorUI-FyCUS"))
        self.boxOffset.setText(_translate("rotatorConnect", "0"))
        self.btnConnect.setText(_translate("rotatorConnect", "Connect"))
        self.txtOffset.setText(_translate("rotatorConnect", "Offset:"))
        self.actSerialPort.setTitle(_translate("rotatorConnect", "Serial port"))
        self.actConfigure.setText(_translate("rotatorConnect", "Configure"))
