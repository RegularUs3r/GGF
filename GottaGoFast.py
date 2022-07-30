#!/bin/python3

import socket
import sys
import concurrent.futures
import requests
import time


#local stuff
from services import services
from Yports import yports
from Xports import xports


#just colors
W = '\033[37m'
EB = '\33[0m'

SOC = '\033[37m'
KET = '\33[0m'

UNK = '\33[33'
NOWN = '\33[0m'

SER = '\33[101m'
VER = '\33[0m'



#I'm counting!
start = time.perf_counter()





print("Created by: SickAndTired")
print("")




try:
    target = sys.argv[1]
    ip = str(socket.gethostbyname(target))
    if target in f"{sys.argv[1]}":
        pass
    else:
        pass
except IndexError:
    print("You might missing something")
    print("Usage: ./GottaGoFast.py target.com/1.1.1.1")



comparison1 = (35)
comparison2 = (24)



def scan(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(3)
        if s.connect_ex((ip, int(port))) == 0:
            s.connect_ex((ip, int(port)))
            try:
                recv = s.recv(35)
                if len(recv) == comparison1 or comparison2:
                    for p, service in zip(xports, services):
                        if port == p:
                            step1 = recv
                            p = (SOC + f"{port}" + KET)
                            service = (f"{service}")
                            result = (str(step1).strip('b').replace('-', '').replace('\\r\\n', '').replace("'", ""))
                            print(f"OPEN   [{p}]       [{service}]       [{result}]")
                            s.close()
                        else:
                            pass
            except:
                url = (f"http://{ip}:{port}")
                r = requests.head(url=url)
                for p, service in zip(xports, services):
                    if port == p:
                        p = (W + f"{port}" + EB)
                        unknown = (UNK + "¿unknown?" + NOWN)
                        server = (SER + f'{r.headers["Server"]}' + VER)
                        if (r.headers["Server"]) == "":
                            service = (f"{service}")
                            print(f"OPEN   [{p}]    [{service}]   [{unknown}]")
                        else:
                            print(f"OPEN   [{p}]    [{service}]   [{server}]")
                    else:
                        pass
        else:
            pass
    except:
        pass




with concurrent.futures.ThreadPoolExecutor(max_workers=1000) as executor:
    for port in yports:
        executor.submit(scan, port)




end = time.perf_counter()
final = float(end - start)
print(f"\ntime elapsed:[{final:0.4f} sec]")
