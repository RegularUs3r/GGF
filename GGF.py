#!/bin/python3

import socket
import sys
import concurrent.futures
import ctypes
import time
import requests



from services import services
from ports import ports
from portas import portas


WRO = '\33[91m'
NG = '\33[0m'
PO = '\33[34m'
RT = '\33[0m'



libgcc_s = ctypes.CDLL('libgcc_s.so.1')



start = time.perf_counter()



target = sys.argv[1]
ip = str(socket.gethostbyname(target))



print("Created by: SickAndTired")
print("")



const1 = (35)
const2 = (24)


bla = ['21','22','65000']


def scan(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(3)
        if s.connect_ex((ip, int(port))) == 0:
            s.connect_ex((ip, int(port)))
            try:
                recv = s.recv(35)
                if len(recv) == const1 or const2:
                    for p, service in zip(portas, services):
                        if port == p:
                            result = recv
                            print("OPEN [" + PO +f"{p}" + RT + "] [" f"{service}" "]",str(result).strip('b').replace('-', '').replace('\\r\\n', '').replace("'", ""))
                            s.close()
                        else:
                            pass
            except:
                url = (f"http://{ip}:{port}")
                r = requests.head(url=url)
                for p, service in zip(portas, services):
                    if port == p:
                        if (r.headers["Server"]) == "":
                            #port = (PO + f"{port}" + RT)
                            print("OPEN [" + PO +f"{port}" + RT + "] [" f"{service}" "] unknown")
                        else:
                            print("OPEN [" + PO +f"{port}" + RT + "] [" f"{service}" "] "+f"{r.headers['Server']}")
                    else:
                        pass
                
        else:
            pass
    except:
        sys.exit(0)


with concurrent.futures.ThreadPoolExecutor(max_workers=1000) as executor:
    for port in bla:
        executor.submit(scan, port)



end = time.perf_counter()
final = float(end - start)
print(f"\ntime elapsed:[{final:0.4f} sec]")
