from xbee import *

def main():

    # setup main Xbee interface class
    Xbee = xbeeController()
    if Xbee.getStatus() != None:
       Xbee.clear()

    start = 128

    while (True):

        slotindex = start

        laddr = start & 0x00ff
        haddr = (start & 0xff00) >> 8

        # can only get 12 bytes at a time so just request the first 12 of each slot config
        xbeeFrame = Xbee.xbeeBroadCastRequest(48, 154, [ord('R'), laddr, haddr, 12])

        # parse out the data the PT sends back
        msg = Xbee.getPacket()

        if msg == None:                         # sometimes nothing comes back, just skip
           continue

        if len(msg) < 29:                       # short ones sometimes, not sure why, toss it
           continue

        m = []                                  # stick the data bytes into a list
        for i in range(16, len(msg)-1):         # trim off the header info and the checksum from the xbee return message
           m.append(msg[i])

        for i in range(0, 4):                   # get the remainder of the slot data
            slotindex = slotindex + 12
            lad = slotindex & 0x00ff
            had = (slotindex & 0xff00) >> 8

            xbeeFrame = Xbee.xbeeBroadCastRequest(48, 154, [ord('R'), lad, had, 12])
            msg = Xbee.getPacket()

            if msg == None:                     # skip misfires
               continue

            for i in range(16, len(msg)-1):     # trim off stuff we don't need
               m.append(msg[i])

        la = m[0]
        lh = m[1] << 8
        adr = lh | la                       # first two bytes are the locomotive address, go ahead and print that 

        p0 = f"{adr:4d} - "
        p1 = " ".join("{:02x}".format(num) for num in m)  # print the small amount of config data we got
        p2 = f" - {start:5d}"
        print (p0+p1+p2)

        start = start + 128                 # jump to the next slot config
        if start >= 2048:                   # stop at slot 15
           break



main()
