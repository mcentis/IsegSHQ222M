
# class with methods to communicate with the Iseg SHQ 222M power supply

import serial
import time

class IsegSHQ222M:
    def __init__(self, port):
        self.ser = serial.Serial(
            port=port,
            baudrate=9600,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS
        )
        if self.ser.isOpen() == False:
            print 'Error: Could not open ' + port
            exit(1)


    def write(self, command):
        self.ser.write(command + '\r\n')
        time.sleep(0.5) # time for the instrument to receive (and process) the instruction
        
    def read(self):
        out = ''
        while self.ser.inWaiting() > 0:
            out += self.ser.read(1)
        return out

    def GetModuleID(self):
        self.write('#')
        return self.read()
