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


### coords [x, y]
iconHome = ["1536", "50"]
iconBack = ["50", "50"]
iconSendTask = ["1400", "800"]
ButtonClainAll = ["1550", "180"]
# tip => do it steps manual one time and write steps for implement with coords [x,y]
coordsNew = [
    "86", "240", "850", "850", "850", "850", *iconHome, "1090", "360", "1470",
    "160", "1470", "160", *iconHome, "1200", "330", "1200", "840", "1400",
    "840", *iconHome, "1520", "830", "270", "580", "1200", "680", "1200",
    "680", "1300", "800", "1080", "612", *iconBack, "1520", "360", *iconHome,
    "140", "270", *iconSendTask, "60", "150", *iconSendTask, "60", "280",
    *iconSendTask, "60", "440", *iconSendTask, "60", "590", *iconSendTask,
    "60", "760", *iconSendTask, *iconHome
]
coordsWithout = [
    "86", "240", "850", "850", "850", "850", *iconHome, "1090", "360", "1470",
    "160", "1470", "160", *iconHome, "1200", "330", "1200", "840", "1400",
    "840", *iconHome, "1530", "830", "270", "580", "1200", "680", "1200",
    "680", "1300", "800", "1080", "612", *iconBack, "1520", "360", "140",
    "270", *iconSendTask, "60", "150", *iconSendTask, "60", "280",
    *iconSendTask, "60", "440", *iconSendTask, "60", "590", *iconSendTask,
    "60", "760", *iconSendTask, *iconHome
]
# look part when iconBack & iconHome are used so close

### Client ADB Device
client = Client(host="127.0.0.1", port=5037)
devices = client.devices()
device = devices[0]
print(len(coordsNew) / 2, len(coordsWithout) / 2)
### Exce command
# device.shell("input touchscreen tap {x} {y}".format(x=coords[4], y=coords[5]))

count = 0
step = 1
stepsComplete = len(coordsWithout) / 2

while stepsComplete >= step:
    count += 2
    coords = coordsWithout
    x = coords[count - 2]
    y = coords[count - 1]

    device.shell("input touchscreen tap {x} {y}".format(x=x, y=y))
    print(x, y)
    input('are you wish continue?\n')
    step += 1
