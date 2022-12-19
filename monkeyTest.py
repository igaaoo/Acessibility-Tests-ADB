from ppadb.client import Client as AdbClient
from time import sleep
import random

# Configurações do ADB
client = AdbClient(host="127.0.0.1", port=5037)
device = client.device("")

# Realiza o monkey test


def startTest(xInit, xFinal, yInit, yFinal):
    for i in range(0, 10):
        x = random.randint(xInit, xFinal)
        y = random.randint(yInit, yFinal)
        print("Tocando em {} x {}".format(x, y))
        device.shell("input tap {} {}".format(x, y))
        sleep(0.5)
