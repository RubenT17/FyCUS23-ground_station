
import time, serial, threading,struct
import bus_packet as bp
import src.globals as GLOBALS
import numpy as np
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QApplication, QLineEdit, QVBoxLayout, QLabel, QPushButton, QDialog
from interfaces.displayPanelUI import Ui_FyCUS23_DisplayPanel
import multiprocessing as mp

float2bytes = lambda x: struct.pack('f', float(x))
bytes2float = lambda x: struct.unpack('f', bytes(x))[0]
bytes2uint = lambda x: struct.unpack('<H', bytes(x))[0]
bytes2int = lambda x: struct.unpack('<h', bytes(x))[0]

class displayPanel(QMainWindow):
    def __init__(self,_tm_buffer,_tc_buffer):
        super().__init__()
        self.tm_buffer=_tm_buffer
        self.tc_buffer=_tc_buffer
        self.displayPanelWindow=Ui_FyCUS23_DisplayPanel()
        self.displayPanelWindow.setupUi(self)
        self.stop_read_event = threading.Event()


        self.show()
        self.place_top_left()
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
        # Convierte data_tc en una secuencia de 4 bytes
        data_tc = data.to_bytes(3, byteorder='big')
        # Crea una lista para meterlo en la función
        data_tc = list(data_tc)
        # Aquí debes implementar la lógica para enviar el paquete con el APID y DATA proporcionados
        print(f"Enviando paquete - APID: {hex(bp.APID_TC_REQUIRED_DATA)}, DATA: {data_tc}")
        try:
            status, datos = bp.bus_packet_EncodePacketize(bp.BUS_PACKET_TYPE_TC, bp.APID_TC_REQUIRED_DATA, bp.BUS_PACKET_ECF_EXIST, data_tc, len(data_tc))
            if status == 0:
                self.tc_buffer.put(datos)
        except:
            pass

    def customTcSet(self,data):
        data_tc = data.to_bytes(3, byteorder='big')
        data_tc = list(data_tc)
        print(f"Enviando paquete - APID: {hex(bp.APID_TC_SET_PROGRMMED_TELEMETRY)}, DATA: {data_tc}")
        try:
            status, datos = bp.bus_packet_EncodePacketize(bp.BUS_PACKET_TYPE_TC, bp.APID_TC_SET_PROGRMMED_TELEMETRY, bp.BUS_PACKET_ECF_EXIST, data_tc, len(data_tc))
            if status == 0:
                self.tc_buffer.put(datos)
        except:
            pass


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
            time.sleep(0.1)
            try:           
                data = self.tm_buffer.get()
                if data != []:
                    #self.changeText(data)
                    self.displayPanelWindow.lbl_accelx.setText(str(data[0]))
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
            except:
                pass

    def changeText(self,data):
        pos = 2
        last_pos = pos
        if(data.data[0] & bp.REQUIRED_DATA_GNSS):
            last_pos = pos
            pos+=18
            gnss = self.bytes2nmea(data.data[last_pos:pos])
            gnss_tr=self.nmea2geodetic(gnss)

            self.displayPanelWindow.lbl_GPSlat.setText(str(gnss_tr[0])+str(gnss_tr[1]))
            self.displayPanelWindow.lbl_GPSlon.setText(str(gnss_tr[2])+str(gnss_tr[3]))
            self.displayPanelWindow.lbl_GPSalt.setText(str(gnss_tr[4]))

        if(data.data[0] & bp.REQUIRED_DATA_ACELL):
            last_pos = pos
            pos+=2
            accel_x = bytes2int(data.data[last_pos:pos])
            last_pos = pos
            pos+=2
            accel_y = bytes2int(data.data[last_pos:pos])
            last_pos = pos
            pos+=2
            accel_z = bytes2int(data.data[last_pos:pos])

            self.displayPanelWindow.lbl_accelx.setText(str(accel_x))
            self.displayPanelWindow.lbl_accely.setText(str(accel_y))
            self.displayPanelWindow.lbl_accelz.setText(str(accel_z))
            

        if(data.data[0] & bp.REQUIRED_DATA_GYRO):
            last_pos = pos
            pos+=2
            gyro_x = bytes2int(data.data[last_pos:pos])
            last_pos = pos
            pos+=2
            gyro_y = bytes2int(data.data[last_pos:pos])
            last_pos = pos
            pos+=2
            gyro_z = bytes2int(data.data[last_pos:pos])

            self.displayPanelWindow.lbl_gyrox.setText(str(gyro_x))
            self.displayPanelWindow.lbl_gyroy.setText(str(gyro_y))
            self.displayPanelWindow.lbl_gyroz.setText(str(gyro_z))

        if(data.data[0] & bp.REQUIRED_DATA_MAGNETOMETER):
            last_pos = pos
            pos+=2
            mag_x = bytes2int(data.data[last_pos:pos])
            last_pos = pos
            pos+=2
            mag_y = bytes2int(data.data[last_pos:pos])
            last_pos = pos
            pos+=2
            mag_z = bytes2int(data.data[last_pos:pos])
            self.displayPanelWindow.lbl_magx.setText(str(mag_x))
            self.displayPanelWindow.lbl_magy.setText(str(mag_y))
            self.displayPanelWindow.lbl_magz.setText(str(mag_z))           

        if(data.data[0] & bp.REQUIRED_DATA_PRESSURE):
            last_pos = pos
            pos+=4
            pressure = bytes2float(data.data[last_pos:pos])
            self.displayPanelWindow.lbl_press.setText(str(pressure))

        if(data.data[0] & bp.REQUIRED_DATA_TEMPERATURE_OUTDOOR):
            last_pos = pos
            pos+=4
            t = bytes2float(data.data[last_pos:pos])
            self.displayPanelWindow.lbl_tempout.setText(str(t))

        if(data.data[0] & bp.REQUIRED_DATA_TEMPERATURE_UP):
            last_pos = pos
            pos+=4
            t = bytes2float(data.data[last_pos:pos])
            self.displayPanelWindow.lbl_tempup.setText(str(t))
            
        if(data.data[0] & bp.REQUIRED_DATA_TEMPERATURE_BATTERY):
            last_pos = pos
            pos+=4
            t = bytes2float(data.data[last_pos:pos])
            self.displayPanelWindow.lbl_tempbatt.setText(str(t))
            
        if(data.data[1] & bp.REQUIRED_DATA_TEMPERATURE_DOWN):
            last_pos = pos
            pos+=4
            t = bytes2float(data.data[last_pos:pos])
            self.displayPanelWindow.lbl_tempdown.setText(str(t))

        if(data.data[1] & bp.REQUIRED_DATA_PV_VOLTAGE):
            last_pos = pos
            pos+=4
            pvV = bytes2float(data.data[last_pos:pos])
            self.displayPanelWindow.lbl_pvV.setText(str(pvV))    
        
        if(data.data[1] & bp.REQUIRED_DATA_PV_CURRENT):
            last_pos = pos
            pos+=4
            pvA = bytes2float(data.data[last_pos:pos])
            self.displayPanelWindow.lbl_pvA.setText(str(pvA)) 
        
        if(data.data[1] & bp.REQUIRED_DATA_BATTERY_VOLTAGE):
            last_pos = pos
            pos+=4
            batV = bytes2float(data.data[last_pos:pos])
            self.displayPanelWindow.lbl_batV.setText(str(batV)) 

        if(data.data[1] & bp.REQUIRED_DATA_BATTERY_CURRENT):
            last_pos = pos
            pos+=4
            batA = bytes2float(data.data[last_pos:pos])
            self.displayPanelWindow.lbl_batA.setText(str(batA)) 

        if(data.data[1] & bp.REQUIRED_DATA_BATTERY_CHARGING):
            last_pos = pos
            pos+=4
            batCh = bytes2float(data.data[last_pos:pos])
            self.displayPanelWindow.lbl_batcarga.setText(str(batCh)) 

        # if(data.data[1] & bp.REQUIRED_DATA_BATTERY_DIETEMP):
        #     last_pos = pos
        #     pos+=4
        #     batDie = bytes2float(data.data[last_pos:pos])
        #     self.displayPanelWindow.lbl_batdie.setText(batDie) 

        if(data.data[1] & bp.REQUIRED_DATA_CURRENT_TIME):
            last_pos = pos
            pos+=4
            time = bytes2float(data.data[last_pos:pos])
            self.displayPanelWindow.lbl_time.setText(str(time)) 


    def bytes2nmea(self,data):
        lat = bytes2float(data[0:4])
        ns = data[4]
        lon = bytes2float(data[5:9])
        ew = data[9]
        alt = bytes2float(data[10:14])
        sep = bytes2float(data[14:18])
        return [lat, ns, lon, ew, alt, sep]

    def nmea2geodetic(self,data):
        lat_aux=data[0]/100
        lat_deg=np.trunc(lat_aux)
        lat_min=lat_aux-lat_deg
        lat=lat_deg+lat_min/60

        lon_aux=data[2]/100
        lon_deg=np.trunc(lon_aux)
        lon_min=lon_aux-lon_deg
        lon=lon_deg+lon_min/60

        data[0]=lat
        data[1]=chr(data[1])
        data[2]=lon  
        data[3]=chr(data[3])
        return data



    #########################################
    ######   Window layout helpers   ########
    #########################################
        
    def center(self):
        frame_geo = self.frameGeometry()
        screen_geo = QApplication.desktop().screenGeometry().center()
        frame_geo.moveCenter(screen_geo)
        self.move(frame_geo.topLeft())

    def place_top_left(self):
        desktop_geo = QApplication.desktop().screenGeometry()
        self.move(desktop_geo.topLeft())


