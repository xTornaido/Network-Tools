from math import floor
from socket import getaddrinfo
from scapy.layers.inet import IP, ICMP
from scapy.sendrecv import sr1
from colorama import Fore
import os
import time

def clear():
    os.system("cls")

def format(data):
    return Fore.MAGENTA + "     > " + Fore.LIGHTCYAN_EX + data + Fore.LIGHTBLACK_EX + ": " + Fore.MAGENTA

def format_ping(host, time, ttl, result):
    final = "null"
    
    if(result):
        final = Fore.MAGENTA + "        > " + Fore.GREEN + host + Fore.LIGHTGREEN_EX + " is online! " + Fore.LIGHTCYAN_EX + "Time" + Fore.LIGHTBLACK_EX + ": " + Fore.MAGENTA + str(time) + Fore.LIGHTCYAN_EX + " TTL" + Fore.LIGHTBLACK_EX + ": " + Fore.MAGENTA + str(ttl) + Fore.LIGHTBLACK_EX + "."
    else:
        final = final = Fore.MAGENTA + "        > " + Fore.RED + host + Fore.LIGHTRED_EX + " is online! " + Fore.LIGHTCYAN_EX + "Time" + Fore.LIGHTBLACK_EX + ": " + Fore.MAGENTA + str(time) + Fore.LIGHTCYAN_EX + " TTL" + Fore.LIGHTBLACK_EX + ": " + Fore.MAGENTA + str(ttl) + Fore.LIGHTBLACK_EX + "."

    return final

def main():

    clear()

    host = input(format("Enter host"))
    count = input(format("Enter count"))
    ttl = input(format("Enter TTL"))
    timeout = input(format("Enter timeout"))
    verbose = input(format("Verbose (y/n)"))

    values = [host, count, ttl, timeout, verbose]

    for i in values:
        try:
            i = str(i)
        except:
            val = "null"

            for x in values:
                if i == x[0]: val = "Host"
                if i == x[1]: val = "Count"
                if i == x[2]: val = "TTL"
                if i == x[3]: val = "Timeout"
                if i == x[4]: val = "Verbose"

            print("Enter correct value for: " + val)

    ints = [count, ttl, timeout]

    for i in ints:
        try:
            i = int(i)

            new_ints = []
            new_ints.append(i)

            if i == int(ints[0]): count = i
            if i == int(ints[1]): ttl = i
            if i == int(ints[2]): timeout = i

        except:
            val = 0

            for x in ints:
                if x == i[0]: val = "Count"
                if x == i[1]: val = "TTL"
                if x == i[2]: val = "Timeout"

            print("Enter correct value for: " + val)

    if(verbose.lower() == "n"):
        verbose = False
    else:
        verbose = True

    clear()
    ping(host, count, ttl, timeout, verbose)


def ping(host="127.0.0.1", count=5, ttl=64, timeout=5, verbose=True):
    host_status = False

    for i in range(count):
        start_time = time.time()

        packet = IP(dst=host, ttl=ttl) / ICMP(type="echo-request")

        try:
            response = sr1(packet, timeout=timeout, verbose=0, retry=1)
        except:
            print(format("Invalid host").replace(":", ""))

        end_time = time.time()
        final_time = "%.2f" % (end_time - start_time)

        host_status = bool(response)

        if(host_status):
            message = format_ping(host, final_time, ttl, True)
        else:
            message = (host, final_time, ttl, False)
        
        if(verbose):
            print(message)

main()