"""
Global Configuration Module

This file contains DEFAULT global configuration variables.
These can be changed with the menu-bar of the UI.
"""

# Serial port name and baud rate
SERIAL_PORT = "COM7"
BAUD_RATE = 9600

# Data send frequency when tracking mode (seconds)
TR_SEND_FREQ = 1

# Settle point reference coordinates (Sevilla)
REF_LAT = 37.411644  # Reference latitude
REF_LON = -6.000173 # Reference longitude
REF_ALT = 7.0  # Reference altitude

GLOBAL_GNSS=[]
GLOBAL_GNSSdisp=[]
GLOBAL_ACELL=[0.0,0.0,0.0]
GLOBAL_GYRO=[0.0,0.0,0.0]
GLOBAL_MAG=[0.0,0.0,0.0]
GLOBAL_PRESS=[0.0]
GLOBAL_TEMP=[0.0,0.0,0.0,0.0]
GLOBAL_TIME=[0.0]
GLOBAL_PV=[0.0,0.0]
GLOBAL_BATT=[0.0,0.0,0.0]
GLOBAL_TM=[]