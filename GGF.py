#!/bin/python3

import socket
import sys
import concurrent.futures
import ctypes
import time

libgcc_s = ctypes.CDLL('libgcc_s.so.1')

start = time.perf_counter()

target = sys.argv[1]

def scan(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.2)
    try:
        s.connect((target, port))
        print(f"{target}:{port}")
        s.close()
    except:
        pass

with concurrent.futures.ThreadPoolExecutor(max_workers=2000) as executor:
    for port in range(65535):
        executor.submit(scan, port)

end = time.perf_counter()
final = float(end - start)
print(f"\ntime elapsed:[{final:0.4f} sec]")
