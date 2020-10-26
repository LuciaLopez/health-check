#!/usr/bin/env python3

#another import
#one more
import os 
import sys


def check_reboot():
    """Returns True if the machine has a pending reboot."""
    return os.path.exists("/run/reboot-required")

def check_disk_full(disk,min_gb, min_percent):
    """Supposed to return True if there isn't enough disk space"""
    pass 

def check_root_full():
    """Returns True if the root partition is full, False otherwise."""
    return check_disk_full(disk="/",min_gb=2, min_percent=10)

def main():
    checks = [
        (check_reboot, "Pending Reboot"),
        (check_root_full, "Root partition full"),
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