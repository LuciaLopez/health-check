#!/usr/bin/env python3
#a note

#import something
import os 
import sys
import shutil
import socket

def check_reboot():
    """Returns True if the machine has a pending reboot."""
    return os.path.exists("/run/reboot-required")

def check_disk_full(disk,min_gb, min_percent):
    """Supposed to return True if there isn't enough disk space"""
    pass 

def check_root_full():
    """Returns True if the root partition is full, False otherwise."""
    return check_disk_full(disk="/",min_gb=2, min_percent=10)

def check_no_network():
    """Returns True if it fails to resolve Google's URL, False otherwise"""
    try:
        socket.gethostbyname("www.google.com")
        return False
    except:
        return True


def main():
    checks = [
        (check_reboot, "Pending Reboot"),
        (check_root_full, "Root partition full"),
        (check_no_network, "No working network"),
    ]
    everything_ok = True
    for check, msg in checks:
        if check():
            print(msg)
            everything_ok = False

    if not everything_ok: 
        sys.exit(1)  
    """ if check_reboot():
        print("Pending reboot. Test")
        sys.exit(1)
    if check_root_full():
        print("Root partiton full.")
        sys.exit(1) """
    """adding one more comment"""
    print("Everything ok.")
    sys.exit(0)

main()