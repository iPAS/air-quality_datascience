#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Author: Supatra Manatrinon, @ 2019

import serial, time, struct

ser = serial.Serial()
ser.port = "COM17" # Set this to your serial port
ser.baudrate = 9600

ser.open()
ser.flushInput()

byte, lastbyte = "\x00", "\x00"

while True:
    lastbyte = byte
    #byte = ser.read(size=1)
    
    # We got a valid packet header
    #if lastbyte == "\xaa" and byte == "\xc0":
    print (byte);
    msg = ser.read(size=10) # Read 8 more bytes
        #readings = struct.unpack('<hhxxcc',sentence) # Decode the packet - big endian, 2 shorts for pm2.5 and pm10, 2 reserved bytes, checksum, message tail
        
    pm2_5 = (msg[3] * 256 + msg[2]) / 10.0
    pm10 = (msg[5] * 256 + msg[4]) / 10.0
        # ignoring the checksum and message tail
        
    print ("PM 2.5:",pm2_5,"μg/m^3  PM 10:",pm10,"μg/m^3")
