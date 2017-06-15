
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

    def interpretNum(self, numStr):
        if len(numStr) == 9: # value with sign (e.g. voltage)
            num = float(numStr[:6])
            num *= pow(10, float(numStr[6:]))
        elif len(numStr) == 8:  # value without sign (e.g. current)
            num = float(numStr[:5])
            num *= pow(10, float(numStr[5:]))            
        else:
            num = -1e6
            print numStr
        return num
    
    def write(self, command):
        self.ser.write(command + '\r\n')
        time.sleep(0.6) # time for the instrument to receive (and process) the instruction
        
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
            return self.interpretNum(ret)
        
    def GetMeasCurrent(self, ch):
        if self.chInRange(ch):
            self.write('I'+str(ch))
            ret = self.read()
            ret = self.cleanString(ret)
            return self.interpretNum(ret)

    def GetVoltageLimit(self, ch):
        if self.chInRange(ch):
            self.write('M'+str(ch))
            ret = self.read()
            ret = self.cleanString(ret)
            return int(ret)

    def GetCurrentLimit(self, ch):
        if self.chInRange(ch):
            self.write('N'+str(ch))
            ret = self.read()
            ret = self.cleanString(ret)
            return int(ret)

    def SetVoltage(self, ch, volt):
        volt = abs(volt)
        if volt > 2000:
            volt = 2000
        voltStr = '%0.2f' % volt
        if self.chInRange(ch):
            self.write('D'+str(ch)+'='+voltStr)
            self.read() # get the response
            
    def GetSetVoltage(self, ch):
        if self.chInRange(ch):
            self.write('D'+str(ch))
            ret = self.read()            
            ret = self.cleanString(ret)
            return self.interpretNum(ret)

    def SetRampSpeed(self, ch, rampSpeed):
        rs = int(abs(rampSpeed))
        if rs < 2:
            rs = 2
        if rs > 255:
            rs = 255
        if self.chInRange(ch):
            self.write('V'+str(ch)+'='+str(rs))
            self.read() # get the response

    def GetRampSpeed(self, ch):
        if self.chInRange(ch):
            self.write('V'+str(ch))
            ret = self.read()
            ret = self.cleanString(ret)
            return int(ret)

    def StartVchange(self, ch):
        if self.chInRange(ch):
            self.write('G'+str(ch))
            self.read() # get the response

    def GetStatus(self, ch):
        if self.chInRange(ch):
            self.write('S'+str(ch))
            ret = self.read()
            ret = self.cleanString(ret)
            return ret[3:]

    def GetModuleStatus(self, ch):
        if self.chInRange(ch):
            self.write('T'+str(ch))
            ret = self.read()
            ret = self.cleanString(ret)
            return int(ret)

    def SetCurrentTrip_mA(self, ch, trip):
        minTrip = 1e-7 # lowest setting for this range
        if abs(trip < minTrip):
            trip = 1
        else:
            trip = int(abs(trip/minTrip)) # to get appropriate units for instrument
        if self.chInRange(ch):
            self.write('LB'+str(ch)+'='+str(trip))
            self.read() # get the response

    def GetCurrentTrip_mA(self, ch):
        if self.chInRange(ch):
            self.write('LB'+str(ch))
            ret = self.read()
            ret = self.cleanString(ret)
            return self.interpretNum(ret)

    def SetCurrentTrip_uA(self, ch, trip):
        minTrip = 1e-10 # lowest setting for this range
        if abs(trip < minTrip):
            trip = 1
        else:
            trip = int(abs(trip/minTrip)) # to get appropriate units for instrument
        if self.chInRange(ch):
            self.write('LS'+str(ch)+'='+str(trip))
            self.read() # get the response

    def GetCurrentTrip_uA(self, ch):
        if self.chInRange(ch):
            self.write('LS'+str(ch))
            ret = self.read()
            ret = self.cleanString(ret)
            return self.interpretNum(ret)
