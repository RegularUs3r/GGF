#!/bin/python3

import socket
import sys
import concurrent.futures
import ctypes
import time
from colorama import Fore

WRO = '\33[91m'
NG = '\33[0m'
PO = '\33[34m'
RT = '\33[0m'

libgcc_s = ctypes.CDLL('libgcc_s.so.1')

start = time.perf_counter()

target = sys.argv[1]
print("Created by: SickAndTired")
print("")
def scan(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.2)
    try:
        s.connect((target, port))
        p = (PO + f"{port}" + RT)
        print("OPEN"+f"[{p}]")
        s.close()
    except:
        pass

with concurrent.futures.ThreadPoolExecutor(max_workers=2000) as executor:
    for port in range(65535):
        executor.submit(scan, port)

end = time.perf_counter()
final = float(end - start)
print(f"\ntime elapsed:[{final:0.4f} sec]")
