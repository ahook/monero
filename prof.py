#!/usr/bin/env python3

'''
' $ sudo apt-get install google-perftools libgoogle-perftools-dev
' $ ./prof.py 127.0.0.1:18080 START
' $ ./prof.py 127.0.0.1:18080 STOP
' $ google-pprof --pdf build/Linux/master/release/bin/monerod ./cpu.prof > cpu.pdf
'''

import socket, struct, sys, time

TARGET_IP = sys.argv[1].split(":")[0]
TARGET_PORT = int(sys.argv[1].split(":")[1])
COMMAND = 11111 if sys.argv[2] == "START" else 22222

MSG_SIZE = 1024
LEVIN_SIG = 0x0101010101012101
HEADER = struct.pack("<QQ?LLLL", LEVIN_SIG, MSG_SIZE, 0, COMMAND, 0, 0, 0)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
s.connect((TARGET_IP, TARGET_PORT))
s.send(HEADER)
time.sleep(1)
