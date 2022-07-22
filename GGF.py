#!/usr/bin/python3



import socket
import sys
import concurrent.futures
import time
import ctypes



print("\nCreated by: SickAndTired")
print("")



#just colors
PO = '\33[34m'
RT = '\33[0m'


#Nedded line for pthread_cancel
libgcc_s = ctypes.CDLL('libgcc_s.so.1')



#Timer startup
start = time.perf_counter()



target = sys.argv[1]



#get host by name
def host(port):
    host = socket.gethostbyname(target)
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2)
        result = s.connect_ex((host, port))
        if result == 0:
            p = (PO + f"{port}" + RT)
            #print(s.recv(1024))
            print("OPEN"+f"[{p}]")
        s.close()
    except socket.gaierror:
        print("gaierror")
    except socket.error:
        print("not responding")



#just address
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



#determining if target it is ip adrress or not
if target.count('.') == 3:
    with concurrent.futures.ThreadPoolExecutor(max_workers=2000) as executor:
        for port in range(65535):
            executor.submit(scan, port)
else:
    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
        for port in range(79, 81):
            executor.submit(host, port)



#Timer resolution
end = time.perf_counter()
final = float(end - start)
print(f"\ntime elapsed:[{final:0.4f} sec]")
