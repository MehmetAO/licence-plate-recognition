import liveLPR
import serial
import time

# For windows PC use COM* ports / For linux use /dev/tty*

arduinoData = serial.Serial("/dev/ttyUSB0", 9600)
#arduinoData = serial.Serial("COM4", 9600)

time.sleep(3)

plate = liveLPR.main()

on = "1"
off = "0"

if plate == ["3","5","A","D","4","5","9","7"]:
    arduinoData.write(on.encode())
