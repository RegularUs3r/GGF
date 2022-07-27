#!/bin/python3

import socket
import sys
import concurrent.futures
import ctypes
import time
import requests
import re
from colorama import Fore



WRO = '\33[91m'
NG = '\33[0m'
PO = '\33[34m'
RT = '\33[0m'



libgcc_s = ctypes.CDLL('libgcc_s.so.1')



start = time.perf_counter()



target = sys.argv[1]
ip = str(socket.gethostbyname(target))
#ip = str(socket.gethostbyname("resendefc.com.br"))



print("Created by: SickAndTired")
print("")



def scan(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(3)
        if s.connect_ex((ip, int(port))) == 0:
            s.connect_ex((ip, int(port)))
            try:
                result = (str(s.recv(35)).strip('b').replace('-', '').replace('\\r\\n', '').replace('\'', '').replace('*', '').replace('+', ''))
                print("OPEN [" + PO +f"{port}" + RT + "]    "+f"{result}")
                s.close()
            except:
                url = (f"http://{ip}:{port}")
                r = requests.head(url=url)
                if (r.headers["Server"]) == "":
                    #port = (PO + f"{port}" + RT)
                    print("OPEN [" + PO +f"{port}" + RT + "]    unknown")
                else:
                    print("OPEN [" + PO +f"{port}" + RT + "]    "+f"{r.headers['Server']}")
        else:
            pass
    except:
        pass



with concurrent.futures.ThreadPoolExecutor(max_workers=400) as executor:
    for port in range(1, 65001):
        executor.submit(scan, port)



end = time.perf_counter()
final = float(end - start)
print(f"\ntime elapsed:[{final:0.4f} sec]")
