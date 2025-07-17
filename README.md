# PTDump
Protothrottle Experiments, dump slot memory

- This is python code for a PC. I'm running windows 11 and python 3.11.0
- This program REQUIRES a USB Xbee 'dongle' device to talk to the Protothrottle. The dongle MUST use the Silicon Labs CP210x chipset and have the USB Driver for that installed on your PC. 
  The dongle H/W can be found on Amazon, search for 'WaveShare Xbee'.
- The Xbee chip for this can be ordered from Sparkfun.com.
- You will also need the XCTU program from the Xbee manufacturer, Digi, it's free. If you want to play with around with Xbees, this program is essential.
- As far as configuration, the Xbee must have the 802.15.4 TH firmware installed, many are shipped with the Digimesh firmware, that won't work. XCTU will let you install the latest if needed using the 'update' button at the top. Once the firmware is verified, you have to change a few configuration items in the chip.  Set the ID Network PAN ID to 225. Find the API Enable and set it to API Mode without Escapes (1).  Just below that, find the baud rate and set it to 38400.  Everything else you can leave at the defaults.
- Example Output. To the left is the locomotive address, it's the first two bytes of each line, each line is a config slot. The number at the far right is the offset we started the read from. This represents reading the first 12 bytes of a slot config, then skipping to the next slot, etc. I can't seem to get past slot 17, although I have all 20 configs in my PT setup.  It just stops sending valid stuff when I ask for the remaining configs.
```
E:\Program Files\Beeware\PTInterface>python main.py
xbee port opened
9310 - 5e 24 02 01 0b 10 05 06 0b 80 18 0c -   128
7032 - 78 1b 02 01 07 10 0c 80 80 80 00 18 -   256
3878 - 26 0f 02 01 07 0a 0c 80 80 80 00 80 -   384
 333 - 4d 01 02 01 0b 16 05 06 00 80 00 19 -   512
2002 - d2 07 02 01 07 16 0c 80 00 80 00 19 -   640
2100 - 34 08 02 01 0b 16 08 80 00 80 00 19 -   768
1022 - fe 03 02 01 0a 09 08 80 80 80 00 80 -   896
3010 - c2 0b 02 01 0a 09 08 80 80 80 00 80 -  1024
2020 - e4 07 02 01 0a 09 08 80 80 80 00 80 -  1152
 832 - 40 03 02 01 0a 09 08 80 80 80 00 80 -  1280
2005 - d5 07 02 01 07 0a 0c 80 80 80 00 80 -  1408
9022 - 3e 23 02 01 07 0a 0c 80 80 80 00 80 -  1536
8755 - 33 22 02 01 0b 0d 08 06 80 80 00 80 -  1664
2003 - d3 07 02 01 06 07 08 80 80 0a 00 80 -  1792
1956 - a4 07 02 01 07 80 08 80 04 80 00 09 -  1920
 729 - d9 02 02 01 0b 16 08 80 00 80 00 19 -  2048
5406 - 1e 15 02 01 0b 04 05 06 00 80 00 19 -  2176


E:\Program Files\Beeware\PTInterface>python dump.py
xbee port opened
9310 - 5e 24 02 01 0b 10 05 06 0b 80 18 0c 00 00 00 00 00 00 00 00 07 17 27 37 ff ff ff ff ff ff ff ff ff ff ff ff -   128
7032 - 78 1b 02 01 07 10 0c 80 80 80 00 18 80 80 1b 1a 0e 16 80 80 80 ff 05 0f 47 57 67 77 ff ff ff ff ff ff ff ff -   256
3878 - 26 0f 02 01 07 0a 0c 80 80 80 00 80 00 00 00 00 00 00 00 00 07 17 27 37 ff ff ff ff ff ff ff ff ff ff ff ff -   384
 333 - 4d 01 02 01 0b 16 05 06 00 80 00 19 80 00 00 01 02 00 7f 28 32 3c 46 ff ff ff ff ff ff ff ff -   512
2002 - d2 07 02 01 07 16 0c 80 00 80 00 19 80 00 00 01 02 00 7f 00 80 00 00 00 00 00 00 07 17 27 37 ff ff ff ff ff ff ff ff ff ff ff ff -   640
2100 - 34 08 02 01 0b 16 08 80 00 80 00 19 00 00 02 00 00 00 00 00 07 17 27 37 80 00 00 01 02 00 7f -   768
1022 - fe 03 02 01 0a 09 08 80 80 80 00 80 00 00 00 00 00 00 00 00 07 17 27 37 80 00 00 01 02 00 7f -   896
3010 - c2 0b 02 01 0a 09 08 80 80 80 00 80 00 00 00 00 00 00 00 00 07 17 27 37 ff ff ff ff ff ff ff ff ff ff ff ff -  1024
2020 - e4 07 02 01 0a 09 08 80 80 80 00 80 00 00 00 00 00 00 00 00 07 17 27 37 47 57 67 77 ff ff ff ff ff ff ff ff -  1152
 832 - 40 03 02 01 0a 09 08 80 80 80 00 80 80 00 00 01 02 00 7f 47 57 67 77 ff ff ff ff ff ff ff ff -  1280
2005 - d5 07 02 01 07 0a 0c 80 80 80 00 80 03 80 00 80 08 04 80 80 80 ff 05 07 00 00 00 00 00 00 00 00 12 18 28 37 80 00 00 01 02 00 7f -  1408
9022 - 3e 23 02 01 07 0a 0c 80 80 80 00 80 03 80 00 80 08 04 80 80 80 ff 05 05 47 57 67 77 ff ff ff ff ff ff ff ff -  1536
8755 - 33 22 02 01 0b 0d 08 06 80 80 00 80 48 58 68 7e ff ff ff ff ff ff ff ff -  1664
2003 - d3 07 02 01 06 07 08 80 80 0a 00 80 80 00 00 01 02 00 7f 47 57 67 77 ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff -  1792
1956 - a4 07 02 01 07 80 08 80 04 80 00 09 80 00 00 01 02 00 7e 00 00 00 00 00 00 00 00 02 0c 18 24 2f 39 42 50 ff ff ff ff ff ff ff ff 80 80 80 80 ff ff ff ff ff ff ff ff -  1920
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



