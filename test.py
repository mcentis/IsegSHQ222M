import IsegSHQ222M
import sys

if len(sys.argv) != 2:
    print 'Usage: python test.py port'
    exit(1)

hv = IsegSHQ222M.IsegSHQ222M(sys.argv[1])

# print hv.GetModuleID()

# print 'Set break time to 10'
# hv.SetBreakTime(10)
# print hv.GetBreakTime()

# print 'Reading currents and voltages'
# for i in range(2):
#     print hv.GetMeasVoltage(1)
#     print hv.GetMeasCurrent(1)
#     print hv.GetMeasVoltage(2)
#     print hv.GetMeasCurrent(2)
    
# print 'Current and voltage limits in %'
# print hv.GetVoltageLimit(1)    
# print hv.GetVoltageLimit(2)
# print hv.GetCurrentLimit(1)
# print hv.GetCurrentLimit(2)

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

print hv.GetStatus(1)
print hv.GetStatus(2)

print 'End of test'
