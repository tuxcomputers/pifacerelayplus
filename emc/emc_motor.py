#!/usr/bin/env python3
import os
import sys
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)
import time
import pifacerelayplus


if __name__ == '__main__':
    pf = pifacerelayplus.PiFaceRelayPlus(pifacerelayplus.RELAY)
    while True:
        for i in range(4):
            pf.motors[i].forward()
        time.sleep(0.25)
        for i in range(4):
            pf.motors[i].coast()
        time.sleep(0.25)
        for i in range(4):
            pf.motors[i].reverse()
        time.sleep(0.25)
        for i in range(4):
            pf.motors[i].brake()
        time.sleep(0.25)