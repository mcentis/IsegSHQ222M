
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

    def chInRange(self, ch):
        if ch == 1 or ch == 2:
            return True
        else:
            print 'Error: wrong channel number: ' + str(ch)
            return False

    def cleanString(self, out): # used for returned values
        out = out.split('\n')[1] # isolate the second line (usually contains the good part)
        out = out.translate(None, '\r') # eliminate carriage return
        return out

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
        ret = self.read()
        return self.cleanString(ret)

    def SetBreakTime(self, bt):
        if bt > 255:
            print 'Error: break time too high'
        else:
            self.write('W='+str(bt))
            self.read() # get response
            
    def GetBreakTime(self):
        self.write('W')
        ret = self.read()
        return int(self.cleanString(ret))

    def GetMeasVoltage(self, ch):
        if self.chInRange(ch):
            self.write('U'+str(ch))
            ret = self.read()
            ret = self.cleanString(ret)
            print ret # continue from here!!!
            
