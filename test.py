import IsegSHQ222M
import sys

if len(sys.argv) != 2:
    print 'Usage: python test.py port'
    exit(1)

hv = IsegSHQ222M.IsegSHQ222M(sys.argv[1])
print hv.GetModuleID()


print 'Endo of test'
