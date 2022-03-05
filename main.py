"""
Cerated on Fri Nov 19 10:51 AM - 2021

@author: Juanestban
"""
import sys, signal, time
from ppadb.client import Client
from constants import COORDS_WITHOUT, brakets


def handle_exit():
    print("")
    print('-' * 80)
    print('\n[*] Exiting...\n')
    sys.exit(0)


signal.signal(signal.SIGINT, handle_exit)


### Client ADB Device
def getClient():
    try:
        client = Client(host="127.0.0.1", port=5037)
        devices = client.devices()
        return devices[0]
    except:
        print(brakets, "[+] Error to try to get your device", brakets)
        inputAnswer = int(
            input(
                "\nDo you want retry find some devices? [YES=1] [NO=0]:\n$/:"))

        if inputAnswer == 0:
            handle_exit()
            return

        getClient()


device = getClient()

### Exce command
# device.shell("input touchscreen tap {x} {y}".format(x=coords[4], y=coords[5]))

step = 0
stepsComplete = len(COORDS_WITHOUT) - 1

while stepsComplete >= step:
    coords = COORDS_WITHOUT
    x = coords[step][0]
    y = coords[step][1]

    device.shell("input touchscreen tap {x} {y}".format(x=x, y=y))
    print('coordX:', x, "coordY:", y, "DATA:", coords[step])
    answer = input('Are you wish continue? [y:yes] [n:no]\n')

    if answer == "n":
        handle_exit()

    # time.sleep(2)
    step += 1
