##!/usr/bin/env python3
from pyfanuc import pyfanuc

conn=pyfanuc('192.168.3.6')
if conn.connect():
	print("Connected")
	print("Read PLC value D2204 as 16 bits")
	n=conn.readpmc(1,9,2204,1)
	if n is not None:
		print("Conductance %0.1f" % (n[2204]/48))
	print("Read SPS value D1870 & 1874 as 32 bit")
	n=conn.readpmc(2,9,1870,2)
	if n is not None:
		print("Length: %i von %i (%0.1f %%)" % (n[1870],n[1874],n[1870]/n[1874]*100))
	print("Read axes")
	for key,val in conn.readaxis(conn.ABS | conn.SKIP | conn.REL | conn.REF).items():
		print(key,val)
	print("Read program O5555")
	print(conn.getprog("O0011"))
