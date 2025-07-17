# PTDump
Protothrottle Experiments, dump slot memory

- This is python code for a PC. I'm running windows 11 and python 3.11.0
- This program REQUIRES a USB Xbee 'dongle' device to talk to the Protothrottle. The dongle MUST use the Silicon Labs CP210x chipset and have the USB Driver for that installed on your PC. 
  The dongle H/W can be found on Amazon, search for 'WaveShare Xbee'.
- The Xbee chip for this can be ordered from Sparkfun.com.
- You will also need the XCTU program from the Xbee manufacturer, Digi, it's free. If you want to play with around with Xbees, this program is essential.
- As far as configuration, the Xbee must have the 802.15.4 TH firmware installed, many are shipped with the Digimesh firmware, that won't work. XCTU will let you install the latest if needed using the 'update' button at the top. Once the firmware is verified, you have to change a few configuration items in the chip.  Set the ID Network PAN ID to 225. Find the API Enable and set it to API Mode without Escapes (1).  Just below that, find the baud rate and set it to 38400.  Everything else you can leave at the defaults.
- Example Output. To the left is the locomotive address, it's the first two bytes of each line, each line is a config slot. The number at the far right is the offset we started the read from.
- For a description of what byte means what, take a look at this file:
```
https://github.com/IowaScaledEngineering/mrbw-cst/blob/master/src/cst-eeprom.h
```
```
E:\Program Files\Beeware\PTInterface>python dump.py
xbee port opened
9310 - 5e 24 02 01 0b 10 05 06 0b 80 18 0c 1b 80 19 1a 0e 16 1b 1c 80 ff 05 03 -   128
7032 - 78 1b 02 01 07 10 0c 80 80 80 00 18 80 80 1b 1a 0e 16 80 80 80 ff 05 0f -   256
3878 - 26 0f 02 01 07 0a 0c 80 80 80 00 80 03 80 00 80 08 04 80 80 80 ff 05 05 -   384
 333 - 4d 01 02 01 0b 16 05 06 00 80 00 19 80 80 18 1c 16 06 80 80 80 ff 05 09 -   512
2002 - d2 07 02 01 07 16 0c 80 00 80 00 19 80 80 18 1c 80 80 80 80 80 ff 05 0d -   640
2100 - 34 08 02 01 0b 16 08 80 00 80 00 19 80 80 18 1c 80 80 80 80 80 ff 02 05 -   768
1022 - fe 03 02 01 0a 09 08 80 80 80 00 80 80 80 00 80 05 06 80 80 80 ff 05 01 -   896
3010 - c2 0b 02 01 0a 09 08 80 80 80 00 80 80 80 00 80 05 06 80 80 80 ff 05 01 -  1024
2020 - e4 07 02 01 0a 09 08 80 80 80 00 80 80 80 00 80 05 06 80 80 80 ff 05 01 -  1152
 832 - 40 03 02 01 0a 09 08 80 80 80 00 80 80 80 00 80 05 06 80 80 80 ff 05 01 -  1280
2005 - d5 07 02 01 07 0a 0c 80 80 80 00 80 d5 07 02 01 07 0a 0c 80 80 80 00 80 -  1408
9022 - 3e 23 02 01 07 0a 0c 80 80 80 00 80 03 80 00 80 08 04 80 80 80 ff 05 05 -  1536
8755 - 33 22 02 01 0b 0d 08 06 80 80 00 80 18 18 00 18 16 06 80 80 80 ff 05 01 -  1664
2003 - d3 07 02 01 06 07 08 80 80 0a 00 80 80 80 00 80 05 06 80 80 80 ff 02 04 -  1792
1956 - a4 07 02 01 07 80 08 80 04 80 00 09 0d 80 03 0a 45 45 80 80 80 ff 02 04 -  1920
```

```
XCTU download
```
http://blueridgeengineering.net/bin/40003026_AH.exe
```
Silicon Labs PC driver
```
 blueridgeengineering.net/bin/pololu-cp2102-windows-121204.zip
```
Xbee Radio Module Sparkfun
```
https://www.sparkfun.com/xbee-3-module-pcb-antenna.html
```



