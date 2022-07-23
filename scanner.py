#!/usr/bin/env python3
import socket
from sys import argv

def is_IP(ip):
    check = ip.split('.') 
    
    if len(check) != 4:
        return False

    for tmp in check:
        try:
            tmp = int(tmp)
        except ValueError:
            return False
        if tmp < 0 or tmp > 255:
            return False
    return True 

def is_Port(port):
    try:
        port = int(port)
    except ValueError:
        return False

    if 0 < port and port < 65535:
        return True
    return False

def is_Open(ip, port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        try:
            s.connect((ip, int(port)))
            s.shutdown(socket.SHUT_RDWR)
            s.close()
            return True
        except:
            s.close()
            return False


def increment_IP(ip):
    IPparts = list(map(int, ip.split(".")))
    IPparts[3] += 1
    for i in (3, 2, 1):
        if IPparts[i] > 255:
            IPparts[i] = 0
            IPparts[i-1] += 1
    return ".".join(map(str, IPparts))

def usage():
    print("usage: [IP] [port] [IP counts to scan]\nEX: 10.10.10.10 80 10")
    exit()


if len(argv) > 1:
    if is_IP(argv[1]) and is_Port(argv[2]):
        try:
            number = int(argv[3])
        except ValueError:
            usage()
        ip = argv[1]
        port = argv[2]
        for i in range(0, number):
            if is_Open(ip, port):
                print(ip + ":" + port + " is open\n")
            else:
                print(ip, "is closed")
            ip = increment_IP(ip)
    else:
        usage()
else:
    usage()
