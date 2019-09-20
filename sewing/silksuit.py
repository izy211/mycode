#!/usr/bin/env python3
import threading
import time

def groundcontrol():
    for i in range(10, 0, -1):
        print(i)
        time.sleep(1)

print("Orion, you are primed for launch. Ignition in T-Minus...")
time.sleep(1)
mythread = threading.Thread(target=groundcontrol)
mythread.start()

print("OH GAWD I FORGOT MY WALLET! COOL THE ENGINES!")
time.sleep(3)
print("NO REALLY! I HAVE A FREE SUB ON MY PUNCHCARD IN THERE!")
time.sleep(3)
print("PLEASE I'M SCARED OF HEIGHTS! JUST LET ME JUMP OUT!")
mythread.join()
print("AAAAAAAAAAAAAAAAAAAAAH!")

time.sleep(3)
input("\n\n\n\nPress F to pay respects.")
