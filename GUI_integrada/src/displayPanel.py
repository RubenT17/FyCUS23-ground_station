
import time, serial, threading
import bus_packet as bp
import src.globals as GLOBALS
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QApplication, QLineEdit, QVBoxLayout, QLabel, QPushButton, QDialog
from interfaces.displayPanelUI import Ui_FyCUS23_DisplayPanel
import multiprocessing as mp



class displayPanel(QMainWindow):
    def __init__(self,_tc_buffer):
        super().__init__()
        self.tc_buffer=_tc_buffer
        self.displayPanelWindow=Ui_FyCUS23_DisplayPanel()
        self.displayPanelWindow.setupUi(self)
        self.stop_read_event = threading.Event()


        self.show()
        self.center()
        self.setSignalSlots()
        self.launchInputRead()

    def setSignalSlots(self):
        # Buttons
        self.displayPanelWindow.pushButton_RqGNSS.pressed.connect(self.btnRqGNSS)
        self.displayPanelWindow.pushButton_RqAcell.pressed.connect(self.btnRqAcell)
        self.displayPanelWindow.pushButton_Rqgyro.pressed.connect(self.btnRqGyro)
        self.displayPanelWindow.pushButton_Rqmag.pressed.connect(self.btnRqMag)
        self.displayPanelWindow.pushButton_Rqpress.pressed.connect(self.btnRqPress)
        self.displayPanelWindow.pushButton_Rqtout.pressed.connect(self.btnRqTout)
        self.displayPanelWindow.pushButton_Rqtup.pressed.connect(self.btnRqTup)
        self.displayPanelWindow.pushButton_Rqtbatt.pressed.connect(self.btnRqTbat)
        self.displayPanelWindow.pushButton_Rqtdwon.pressed.connect(self.btnRqTdown)
        self.displayPanelWindow.pushButton_Rqpv.pressed.connect(self.btnRqPV)
        self.displayPanelWindow.pushButton_Rqbat.pressed.connect(self.btnRqBat)
        self.displayPanelWindow.pushButton_Rqcarga.pressed.connect(self.btnRqCarga)
        self.displayPanelWindow.pushButton_Rqall.pressed.connect(self.btnRqAll)        

    #############################################
    ##### Buttons/Actions behaviour (Slots) #####
    #############################################
    def btnRqGNSS(self):
        data=bp.REQUIRED_DATA_GNSS 
        self.customTcReq(data)
    def btnRqAcell(self):
        data=bp.REQUIRED_DATA_ACELL 
        self.customTcReq(data)
    def btnRqGyro(self):
        data=bp.REQUIRED_DATA_GYRO 
        self.customTcReq(data)
    def btnRqMag(self):
        data=bp.REQUIRED_DATA_MAGNETOMETER 
        self.customTcReq(data)
    def btnRqPress(self):
        data=bp.REQUIRED_DATA_PRESSURE 
        self.customTcReq(data)
    def btnRqTout(self):
        data=bp.REQUIRED_DATA_TEMPERATURE_OUTDOOR 
        self.customTcReq(data)
    def btnRqTup(self):
        data=bp.REQUIRED_DATA_TEMPERATURE_UP 
        self.customTcReq(data)
    def btnRqTbat(self):
        data=bp.REQUIRED_DATA_TEMPERATURE_UP 
        self.customTcReq(data)
    def btnRqTdown(self):
        data=bp.REQUIRED_DATA_TEMPERATURE_DOWN 
        self.customTcReq(data)
    def btnRqPV(self):
        data=bp.REQUIRED_DATA_PV_CURRENT + bp.REQUIRED_DATA_PV_VOLTAGE 
        self.customTcReq(data)
    def btnRqBat(self):
        data=bp.REQUIRED_DATA_BATTERY_CURRENT + bp.REQUIRED_DATA_BATTERY_VOLTAGE 
        self.customTcReq(data)
    def btnRqCarga(self):
        data=bp.REQUIRED_DATA_BATTERY_CHARGING 
        self.customTcReq(data)
    def btnRqAll(self):
        data=bp.REQUIRED_DATA_ALL 
        self.customTcReq(data)

    def customTcReq(self,data):
        try:
            status, datos = bp.bus_packet_EncodePacketize(bp.BUS_PACKET_TYPE_TC, bp.APID_TC_REQUIRED_DATA, bp.BUS_PACKET_ECF_EXIST, data, len(data))
            if self.status == 0:
                self.tc_buffer.put(datos)
            print("hola")
        except:
            print('no he hecho nada')
            pass

    def customTcSet(self,data):
        status, datos = bp.bus_packet_EncodePacketize(bp.BUS_PACKET_TYPE_TC, bp.APID_TC_SET_PROGRMMED_TELEMETRY, bp.BUS_PACKET_ECF_EXIST, data, len(data))
        if status == 0:
            self.tc_buffer.put(datos)
    #########################################
    ######   Thread related events   ########
    #########################################
    def closeEvent(self, event):
        '''
        @Overrides
        '''
        #Gently stop possible running threads
        self.stop_read_event.set()
        event.accept()
    
    def launchInputRead(self):
        status_thr = threading.Thread(target=self.statusReadThread,args=[self.stop_read_event], daemon=True)
        status_thr.start()

    def statusReadThread(self, stop_thread_event: threading.Event):
        stop_thread_event.clear()
        while not stop_thread_event.is_set():

            if GLOBALS.GLOBAL_GNSS:
                lat,latSign,lon,lonSign,altOrt,undGeoide=GLOBALS.GLOBAL_GNSS
                self.displayPanelWindow.lbl_GPSlat.setText(str(lat)+latSign)
                self.displayPanelWindow.lbl_GPSlon.setText(str(lon)+lonSign)
                self.displayPanelWindow.lbl_GPSalt.setText(altOrt)
                # self.displayPanelWindow.lbl_accelx.setText(GLOBALS.GLOBAL_ACELL[0])
                # self.displayPanelWindow.lbl_accely.setText(GLOBALS.GLOBAL_ACELL[1])
                # self.displayPanelWindow.lbl_accelz.setText(GLOBALS.GLOBAL_ACELL[2])
                # self.displayPanelWindow.lbl_gyrox.setText(GLOBALS.GLOBAL_GYRO[0])
                # self.displayPanelWindow.lbl_gyroy.setText(GLOBALS.GLOBAL_GYRO[1])
                # self.displayPanelWindow.lbl_gyroz.setText(GLOBALS.GLOBAL_GYRO[2])
                # self.displayPanelWindow.lbl_magx.setText(GLOBALS.GLOBAL_MAG[0])
                # self.displayPanelWindow.lbl_magy.setText(GLOBALS.GLOBAL_MAG[1])
                # self.displayPanelWindow.lbl_magz.setText(GLOBALS.GLOBAL_MAG[2])
                # self.displayPanelWindow.lbl_press.setText(GLOBALS.GLOBAL_PRESS)
                # self.displayPanelWindow.lbl_tempout.setText(GLOBALS.GLOBAL_TEMP[0])
                # self.displayPanelWindow.lbl_tempup.setText(GLOBALS.GLOBAL_TEMP[1])
                # self.displayPanelWindow.lbl_tempbatt.setText(GLOBALS.GLOBAL_TEMP[2])
                # self.displayPanelWindow.lbl_tempdown.setText(GLOBALS.GLOBAL_TEMP[3])
                # self.displayPanelWindow.lbl_pvA.setText(GLOBALS.GLOBAL_PV[0])
                # self.displayPanelWindow.lbl_pvV.setText(GLOBALS.GLOBAL_PV[1])
                # self.displayPanelWindow.lbl_batV.setText(GLOBALS.GLOBAL_BATT[1])
                # self.displayPanelWindow.lbl_batA.setText(GLOBALS.GLOBAL_BATT[0])
                # self.displayPanelWindow.lbl_batcarga.setText(GLOBALS.GLOBAL_BATT[2])



    #########################################
    ######   Window layout helpers   ########
    #########################################
        
    def center(self):
        frame_geo = self.frameGeometry()
        screen_geo = QApplication.desktop().screenGeometry().center()
        frame_geo.moveCenter(screen_geo)
        self.move(frame_geo.topLeft())





        # Función para enviar el paquete
def ENVIAR_PAQUETE(apid, data):
    import struct

    # Convierte data_tc en una secuencia de 4 bytes
    data_tc = data.to_bytes(3, byteorder='big')

    # Crea una lista para meterlo en la función
    data_tc = list(data_tc)

    # Aquí debes implementar la lógica para enviar el paquete con el APID y DATA proporcionados
    print(f"Enviando paquete - APID: {hex(apid)}, DATA: {data_tc}")

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QComboBox, QCheckBox, QLineEdit, QPushButton, QVBoxLayout, QWidget



class GUI(QMainWindow):
    def _init_(self):
        super()._init_()

        self.setWindowTitle("Control de Misión de Satélite")
        self.setGeometry(100, 100, 400, 400)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()

        etiqueta_apid = QLabel("Selecciona un APID:")
        layout.addWidget(etiqueta_apid)

        apids = [
            "APID_TC_PROGRAMMED_TELECOMMAND (0x20)",
            "APID_TC_REQUIRED_REPORT_OBC (0x21)",
            "APID_TC_REQUIRED_REPORT_EPS (0x22)",
            "APID_TC_REQUIRED_REPORT_MODEM (0x23)",
            "APID_TC_REQUIRED_DATA (0x24)",
            "APID_TC_SET_PROGRMMED_TELEMETRY (0x30)",
            "APID_TC_ARE_YOU_ALIVE (0x31)"
        ]

        self.combo_apid = QComboBox()
        self.combo_apid.addItems(apids)
        layout.addWidget(self.combo_apid)

        self.checkbox_data_required = QCheckBox("Seleccionar datos requeridos:")
        self.checkbox_data_required.stateChanged.connect(self.toggle_data_widgets)
        layout.addWidget(self.checkbox_data_required)

        # Casillas de verificación para los datos requeridos
        self.checkboxes_data_required = []
        data_required_labels = [
            "REQUIRED_DATA_GNSS",
            "REQUIRED_DATA_ACELL",
            "REQUIRED_DATA_GYRO",
            "REQUIRED_DATA_MAGNETOMETER",
            "REQUIRED_DATA_PRESSURE",
            "REQUIRED_DATA_TEMPERATURE_0",
            "REQUIRED_DATA_TEMPERATURE_1",
            "REQUIRED_DATA_TEMPERATURE_2",
            "REQUIRED_DATA_TEMPERATURE_3",
            "REQUIRED_DATA_PV_VOLTAGE",
            "REQUIRED_DATA_PV_CURRENT",
            "REQUIRED_DATA_BATTERY_VOLTAGE",
            "REQUIRED_DATA_BATTERY_CURRENT",
            "REQUIRED_DATA_CURRENT_TIME",
            "REQUIRED_DATA_ALL"
        ]

        for label in data_required_labels:
            checkbox = QCheckBox(label)
            layout.addWidget(checkbox)
            self.checkboxes_data_required.append(checkbox)

        self.label_tiempo = QLabel("Tiempo (3-60 segundos):")
        self.entrada_tiempo = QLineEdit()
        self.boton_enviar = QPushButton("Enviar")
        self.boton_enviar.clicked.connect(self.enviar_paquete)

        # Inicialmente, ocultar los widgets de datos requeridos y tiempo
        self.toggle_data_widgets()

        layout.addWidget(self.label_tiempo)
        layout.addWidget(self.entrada_tiempo)
        layout.addWidget(self.boton_enviar)

        central_widget.setLayout(layout)

    def toggle_data_widgets(self):
        if self.checkbox_data_required.isChecked():
            for checkbox in self.checkboxes_data_required:
                checkbox.setEnabled(True)
            self.label_tiempo.show()
            self.entrada_tiempo.show()
            self.boton_enviar.show()
        else:
            for checkbox in self.checkboxes_data_required:
                checkbox.setEnabled(False)
            self.label_tiempo.hide()
            self.entrada_tiempo.hide()
            self.boton_enviar.hide()

    def enviar_paquete(self):
        apid_text = self.combo_apid.currentText()
        data_required = 0

        if apid_text == "APID_TC_REQUIRED_DATA (0x24)" or apid_text == "APID_TC_SET_PROGRMMED_TELEMETRY (0x30)":
            for checkbox in self.checkboxes_data_required:
                if checkbox.isChecked():
                    data_required |= 1 << self.checkboxes_data_required.index(checkbox)
            tiempo_str = self.entrada_tiempo.text()
            tiempo = int(tiempo_str)
            data = (tiempo << 16) | data_required
        else:
            data = 0

        apid = int(apid_text.split("(")[1].split(")")[0], 16)

        ENVIAR_PAQUETE(apid, data)

