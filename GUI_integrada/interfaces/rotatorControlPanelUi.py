# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interfaces\rotatorControlPanelWindows.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_rotatorControlPanel(object):
    def setupUi(self, rotatorControlPanel):
        rotatorControlPanel.setObjectName("rotatorControlPanel")
        rotatorControlPanel.resize(990, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(rotatorControlPanel.sizePolicy().hasHeightForWidth())
        rotatorControlPanel.setSizePolicy(sizePolicy)
        rotatorControlPanel.setMinimumSize(QtCore.QSize(990, 600))
        rotatorControlPanel.setMaximumSize(QtCore.QSize(990, 600))
        self.gMainWindow = QtWidgets.QWidget(rotatorControlPanel)
        self.gMainWindow.setObjectName("gMainWindow")
        self.gAzimuthData = QtWidgets.QFrame(self.gMainWindow)
        self.gAzimuthData.setGeometry(QtCore.QRect(10, 10, 475, 260))
        self.gAzimuthData.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.gAzimuthData.setFrameShadow(QtWidgets.QFrame.Raised)
        self.gAzimuthData.setObjectName("gAzimuthData")
        self.txtAzimuth = QtWidgets.QLabel(self.gAzimuthData)
        self.txtAzimuth.setGeometry(QtCore.QRect(10, 10, 80, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtAzimuth.setFont(font)
        self.txtAzimuth.setObjectName("txtAzimuth")
        self.boxDataAz = QtWidgets.QLineEdit(self.gAzimuthData)
        self.boxDataAz.setEnabled(False)
        self.boxDataAz.setGeometry(QtCore.QRect(80, 60, 310, 100))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(239, 239, 239))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.boxDataAz.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(72)
        self.boxDataAz.setFont(font)
        self.boxDataAz.setMaxLength(5)
        self.boxDataAz.setAlignment(QtCore.Qt.AlignCenter)
        self.boxDataAz.setObjectName("boxDataAz")
        self.txtStatusAz = QtWidgets.QLabel(self.gAzimuthData)
        self.txtStatusAz.setEnabled(False)
        self.txtStatusAz.setGeometry(QtCore.QRect(160, 200, 70, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.txtStatusAz.setFont(font)
        self.txtStatusAz.setObjectName("txtStatusAz")
        self.lblStatusAz = QtWidgets.QLabel(self.gAzimuthData)
        self.lblStatusAz.setEnabled(False)
        self.lblStatusAz.setGeometry(QtCore.QRect(240, 200, 80, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lblStatusAz.setFont(font)
        self.lblStatusAz.setObjectName("lblStatusAz")
        self.gElevationData = QtWidgets.QFrame(self.gMainWindow)
        self.gElevationData.setGeometry(QtCore.QRect(505, 10, 475, 260))
        self.gElevationData.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.gElevationData.setFrameShadow(QtWidgets.QFrame.Raised)
        self.gElevationData.setObjectName("gElevationData")
        self.txtElevation = QtWidgets.QLabel(self.gElevationData)
        self.txtElevation.setGeometry(QtCore.QRect(10, 10, 85, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtElevation.setFont(font)
        self.txtElevation.setObjectName("txtElevation")
        self.boxDataEl = QtWidgets.QLineEdit(self.gElevationData)
        self.boxDataEl.setEnabled(False)
        self.boxDataEl.setGeometry(QtCore.QRect(90, 60, 310, 100))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(239, 239, 239))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.boxDataEl.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(72)
        self.boxDataEl.setFont(font)
        self.boxDataEl.setMaxLength(5)
        self.boxDataEl.setAlignment(QtCore.Qt.AlignCenter)
        self.boxDataEl.setObjectName("boxDataEl")
        self.txtStatusEl = QtWidgets.QLabel(self.gElevationData)
        self.txtStatusEl.setEnabled(False)
        self.txtStatusEl.setGeometry(QtCore.QRect(180, 200, 70, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.txtStatusEl.setFont(font)
        self.txtStatusEl.setObjectName("txtStatusEl")
        self.lblStatusEl = QtWidgets.QLabel(self.gElevationData)
        self.lblStatusEl.setEnabled(False)
        self.lblStatusEl.setGeometry(QtCore.QRect(260, 200, 70, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lblStatusEl.setFont(font)
        self.lblStatusEl.setObjectName("lblStatusEl")
        self.gGPS = QtWidgets.QFrame(self.gMainWindow)
        self.gGPS.setGeometry(QtCore.QRect(10, 290, 475, 220))
        self.gGPS.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.gGPS.setFrameShadow(QtWidgets.QFrame.Raised)
        self.gGPS.setObjectName("gGPS")
        self.txtGPS = QtWidgets.QLabel(self.gGPS)
        self.txtGPS.setGeometry(QtCore.QRect(10, 5, 70, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.txtGPS.setFont(font)
        self.txtGPS.setObjectName("txtGPS")
        self.txtLatitude = QtWidgets.QLabel(self.gGPS)
        self.txtLatitude.setGeometry(QtCore.QRect(30, 50, 80, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtLatitude.setFont(font)
        self.txtLatitude.setObjectName("txtLatitude")
        self.txtStatusAuxEl = QtWidgets.QLabel(self.gGPS)
        self.txtStatusAuxEl.setEnabled(False)
        self.txtStatusAuxEl.setGeometry(QtCore.QRect(280, 80, 30, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtStatusAuxEl.setFont(font)
        self.txtStatusAuxEl.setObjectName("txtStatusAuxEl")
        self.txtLongitude = QtWidgets.QLabel(self.gGPS)
        self.txtLongitude.setGeometry(QtCore.QRect(15, 100, 95, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtLongitude.setFont(font)
        self.txtLongitude.setObjectName("txtLongitude")
        self.txtStatusAuxAz = QtWidgets.QLabel(self.gGPS)
        self.txtStatusAuxAz.setEnabled(False)
        self.txtStatusAuxAz.setGeometry(QtCore.QRect(280, 34, 30, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtStatusAuxAz.setFont(font)
        self.txtStatusAuxAz.setObjectName("txtStatusAuxAz")
        self.lblLongitude = QtWidgets.QLabel(self.gGPS)
        self.lblLongitude.setGeometry(QtCore.QRect(125, 100, 65, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lblLongitude.setFont(font)
        self.lblLongitude.setObjectName("lblLongitude")
        self.txtAltitude = QtWidgets.QLabel(self.gGPS)
        self.txtAltitude.setGeometry(QtCore.QRect(35, 150, 80, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtAltitude.setFont(font)
        self.txtAltitude.setObjectName("txtAltitude")
        self.lblAltitude = QtWidgets.QLabel(self.gGPS)
        self.lblAltitude.setGeometry(QtCore.QRect(125, 150, 102, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lblAltitude.setFont(font)
        self.lblAltitude.setObjectName("lblAltitude")
        self.lblLatitude = QtWidgets.QLabel(self.gGPS)
        self.lblLatitude.setGeometry(QtCore.QRect(125, 50, 65, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lblLatitude.setFont(font)
        self.lblLatitude.setObjectName("lblLatitude")
        self.lnSeparator = QtWidgets.QFrame(self.gGPS)
        self.lnSeparator.setGeometry(QtCore.QRect(227, 0, 20, 220))
        self.lnSeparator.setFrameShape(QtWidgets.QFrame.VLine)
        self.lnSeparator.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lnSeparator.setObjectName("lnSeparator")
        self.btnTrack = QtWidgets.QPushButton(self.gGPS)
        self.btnTrack.setEnabled(False)
        self.btnTrack.setGeometry(QtCore.QRect(370, 180, 80, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btnTrack.setFont(font)
        self.btnTrack.setObjectName("btnTrack")
        self.lblStatusAuxAz = QtWidgets.QLabel(self.gGPS)
        self.lblStatusAuxAz.setEnabled(False)
        self.lblStatusAuxAz.setGeometry(QtCore.QRect(325, 34, 70, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lblStatusAuxAz.setFont(font)
        self.lblStatusAuxAz.setObjectName("lblStatusAuxAz")
        self.lblStatusAuxEl = QtWidgets.QLabel(self.gGPS)
        self.lblStatusAuxEl.setEnabled(False)
        self.lblStatusAuxEl.setGeometry(QtCore.QRect(325, 80, 81, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lblStatusAuxEl.setFont(font)
        self.lblStatusAuxEl.setObjectName("lblStatusAuxEl")
        self.lblStatusRange = QtWidgets.QLabel(self.gGPS)
        self.lblStatusRange.setEnabled(False)
        self.lblStatusRange.setGeometry(QtCore.QRect(390, 120, 91, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lblStatusRange.setFont(font)
        self.lblStatusRange.setObjectName("lblStatusRange")
        self.txtStatusRange = QtWidgets.QLabel(self.gGPS)
        self.txtStatusRange.setEnabled(False)
        self.txtStatusRange.setGeometry(QtCore.QRect(270, 120, 91, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtStatusRange.setFont(font)
        self.txtStatusRange.setObjectName("txtStatusRange")
        self.gRotatorParam = QtWidgets.QFrame(self.gMainWindow)
        self.gRotatorParam.setGeometry(QtCore.QRect(505, 290, 475, 220))
        self.gRotatorParam.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.gRotatorParam.setFrameShadow(QtWidgets.QFrame.Raised)
        self.gRotatorParam.setObjectName("gRotatorParam")
        self.txtRotatorPars = QtWidgets.QLabel(self.gRotatorParam)
        self.txtRotatorPars.setEnabled(True)
        self.txtRotatorPars.setGeometry(QtCore.QRect(10, 5, 200, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.txtRotatorPars.setFont(font)
        self.txtRotatorPars.setObjectName("txtRotatorPars")
        self.txtRotatorStatus = QtWidgets.QLabel(self.gRotatorParam)
        self.txtRotatorStatus.setEnabled(False)
        self.txtRotatorStatus.setGeometry(QtCore.QRect(30, 50, 135, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtRotatorStatus.setFont(font)
        self.txtRotatorStatus.setObjectName("txtRotatorStatus")
        self.lblRotatorStatus = QtWidgets.QLabel(self.gRotatorParam)
        self.lblRotatorStatus.setEnabled(False)
        self.lblRotatorStatus.setGeometry(QtCore.QRect(180, 50, 91, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lblRotatorStatus.setFont(font)
        self.lblRotatorStatus.setObjectName("lblRotatorStatus")
        self.btnHome = QtWidgets.QPushButton(self.gMainWindow)
        self.btnHome.setEnabled(False)
        self.btnHome.setGeometry(QtCore.QRect(70, 520, 120, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btnHome.setFont(font)
        self.btnHome.setObjectName("btnHome")
        self.btnSend = QtWidgets.QPushButton(self.gMainWindow)
        self.btnSend.setEnabled(False)
        self.btnSend.setGeometry(QtCore.QRect(305, 520, 120, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btnSend.setFont(font)
        self.btnSend.setObjectName("btnSend")
        self.btnOnOff = QtWidgets.QPushButton(self.gMainWindow)
        self.btnOnOff.setGeometry(QtCore.QRect(605, 520, 275, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btnOnOff.setFont(font)
        self.btnOnOff.setObjectName("btnOnOff")
        rotatorControlPanel.setCentralWidget(self.gMainWindow)
        self.statusBar = QtWidgets.QStatusBar(rotatorControlPanel)
        self.statusBar.setObjectName("statusBar")
        rotatorControlPanel.setStatusBar(self.statusBar)
        self.menuBar = QtWidgets.QMenuBar(rotatorControlPanel)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 990, 26))
        self.menuBar.setObjectName("menuBar")
        self.menuParameters = QtWidgets.QMenu(self.menuBar)
        self.menuParameters.setObjectName("menuParameters")
        self.menuConfigure = QtWidgets.QMenu(self.menuParameters)
        self.menuConfigure.setObjectName("menuConfigure")
        rotatorControlPanel.setMenuBar(self.menuBar)
        self.actTrSendFreq = QtWidgets.QAction(rotatorControlPanel)
        self.actTrSendFreq.setObjectName("actTrSendFreq")
        self.actRefCoords = QtWidgets.QAction(rotatorControlPanel)
        self.actRefCoords.setObjectName("actRefCoords")
        self.menuConfigure.addAction(self.actTrSendFreq)
        self.menuConfigure.addAction(self.actRefCoords)
        self.menuParameters.addAction(self.menuConfigure.menuAction())
        self.menuBar.addAction(self.menuParameters.menuAction())

        self.retranslateUi(rotatorControlPanel)
        QtCore.QMetaObject.connectSlotsByName(rotatorControlPanel)

    def retranslateUi(self, rotatorControlPanel):
        _translate = QtCore.QCoreApplication.translate
        rotatorControlPanel.setWindowTitle(_translate("rotatorControlPanel", "rotatorUI-FyCUS"))
        self.txtAzimuth.setText(_translate("rotatorControlPanel", "Azimuth"))
        self.txtStatusAz.setText(_translate("rotatorControlPanel", "Status:"))
        self.lblStatusAz.setText(_translate("rotatorControlPanel", "---.--"))
        self.txtElevation.setText(_translate("rotatorControlPanel", "Elevation"))
        self.txtStatusEl.setText(_translate("rotatorControlPanel", "Status:"))
        self.lblStatusEl.setText(_translate("rotatorControlPanel", "--.--"))
        self.txtGPS.setText(_translate("rotatorControlPanel", "GPS"))
        self.txtLatitude.setText(_translate("rotatorControlPanel", "Latitude:"))
        self.txtStatusAuxEl.setText(_translate("rotatorControlPanel", "El:"))
        self.txtLongitude.setText(_translate("rotatorControlPanel", "Longitude:"))
        self.txtStatusAuxAz.setText(_translate("rotatorControlPanel", "Az:"))
        self.lblLongitude.setText(_translate("rotatorControlPanel", "000.00"))
        self.txtAltitude.setText(_translate("rotatorControlPanel", "Altitude:"))
        self.lblAltitude.setText(_translate("rotatorControlPanel", "000.00"))
        self.lblLatitude.setText(_translate("rotatorControlPanel", "000.00"))
        self.btnTrack.setText(_translate("rotatorControlPanel", "Track"))
        self.lblStatusAuxAz.setText(_translate("rotatorControlPanel", "000.00"))
        self.lblStatusAuxEl.setText(_translate("rotatorControlPanel", "000.00"))
        self.lblStatusRange.setText(_translate("rotatorControlPanel", "00.00"))
        self.txtStatusRange.setText(_translate("rotatorControlPanel", "Dist (km):"))
        self.txtRotatorPars.setText(_translate("rotatorControlPanel", "Rotator parameters"))
        self.txtRotatorStatus.setText(_translate("rotatorControlPanel", "Rotator status:"))
        self.lblRotatorStatus.setText(_translate("rotatorControlPanel", "---------"))
        self.btnHome.setText(_translate("rotatorControlPanel", "Home"))
        self.btnSend.setText(_translate("rotatorControlPanel", "Send"))
        self.btnOnOff.setText(_translate("rotatorControlPanel", "On"))
        self.menuParameters.setTitle(_translate("rotatorControlPanel", "Parameters"))
        self.menuConfigure.setTitle(_translate("rotatorControlPanel", "Configure"))
        self.actTrSendFreq.setText(_translate("rotatorControlPanel", "Send frequency - tracking mode"))
        self.actRefCoords.setText(_translate("rotatorControlPanel", "Point reference coordinates"))
