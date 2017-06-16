import IsegSHQ222M
import sys

if len(sys.argv) != 2:
    print 'Usage: python test.py port'
    exit(1)

hv = IsegSHQ222M.IsegSHQ222M(sys.argv[1])

print hv.GetModuleID()

print 'Set break time to 10'
hv.SetBreakTime(10)
print hv.GetBreakTime()

print 'Reading currents and voltages'
for i in range(2):
    print hv.GetMeasVoltage(1)
    print hv.GetMeasCurrent(1)
    print hv.GetMeasVoltage(2)
    print hv.GetMeasCurrent(2)
    
print 'Current and voltage limits in %'
print hv.GetVoltageLimit(1)    
print hv.GetVoltageLimit(2)
print hv.GetCurrentLimit(1)
print hv.GetCurrentLimit(2)

print 'Set target voltages'
hv.SetVoltage(1, 20.1)
hv.SetVoltage(2, -300.25666)
print hv.GetSetVoltage(1)
print hv.GetSetVoltage(2)

print 'Set ramp speed'
hv.SetRampSpeed(1, 20)
hv.SetRampSpeed(2, -5)
print hv.GetRampSpeed(1)
print hv.GetRampSpeed(2)

hv.SetVoltage(1, 0)
hv.SetVoltage(2, 0)

hv.StartVchange(1)
hv.StartVchange(2)

print 'Channel status'
print hv.GetStatus(1)
print hv.GetStatus(2)

print 'Module status'
print hv.GetModuleStatus(1)
print hv.GetModuleStatus(2)

print 'Set current trip'
hv.SetCurrentTrip_mA(1, 5e-6)
print hv.GetCurrentTrip_mA(1)

hv.SetCurrentTrip_uA(2, 1e-9)
print hv.GetCurrentTrip_uA(2)

print 'Remove current trip'
hv.RemoveCurrentTrip_mA(1)
hv.RemoveCurrentTrip_uA(1)
hv.RemoveCurrentTrip_mA(2)
hv.RemoveCurrentTrip_uA(2)
print hv.GetCurrentTrip_mA(1)
print hv.GetCurrentTrip_uA(1)
print hv.GetCurrentTrip_mA(2)
print hv.GetCurrentTrip_uA(2)

print 'Ramp and wait'
hv.SetRampSpeed(1, 20)
hv.SetRampSpeed(2, 100)
hv.SetVrampWait(1, 200)
hv.SetVrampWait(2, 500)
hv.SetVrampWait(1, 0)
hv.SetVrampWait(2, 0)


print 'End of test'
