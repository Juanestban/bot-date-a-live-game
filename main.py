"""
Cerated on Fri Nov 19 10:51 AM - 2021

@author: Juanestban
"""
import requests, sys, signal, time
from ppadb.client import Client


def handler_Exit(sig, frame):
    print('')
    print('-' * 80)
    print('\n[*] Exiting...\n')
    sys.exit(0)


signal.signal(signal.SIGINT, handler_Exit)


def runCommad(cmd):
    if (cmd == 'exit'):
        handler_Exit()


while True:
    cmd = input("$/~ ")
    runCommad(cmd)

    client = Client(host="127.0.0.1", port=5037)
    devices = client.devices()
    device = devices[0]

    device.shell("input touchscreen swipe [coords 0 0 1]")

    print("hello world")
