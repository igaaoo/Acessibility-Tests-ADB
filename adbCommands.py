from ppadb.client import Client as AdbClient
import monkeyTest as monkey

import time

# Configurações do ADB
client = AdbClient(host="127.0.0.1", port=5037)
device = client.device("")

# ------------------------------------------
# Abre app da lista de apps
# ------------------------------------------

# Abre Scanner
device.shell("input tap {} {}".format(660, 1560))
time.sleep(2)

device.shell("input tap {} {}".format(630, 1160))
time.sleep(2)

# Inicia gravação
device.shell("input tap {} {}".format(330, 1160))

# Monkey Test (y / 70 - 1500 x / 0 - 720)
monkey.startTest(0, 720, 70, 1500)

# Puxa tela para baixo
device.shell("input swipe {} {} {} {} {}".format(166, 15, 150, 1255, 1000))
time.sleep(2)

# Desliga gravação e compartilha no telegram
device.shell("input tap {} {}".format(630, 1160))
time.sleep(3)
device.shell("input tap {} {}".format(600, 90))
time.sleep(3)
device.shell("input tap {} {}".format(400, 1360))
time.sleep(3)
device.shell("input tap {} {}".format(240, 360))
device.shell("input tap {} {}".format(640, 1420))
time.sleep(3)

# Retorna a tela inicial e oculta Scanner
device.shell("input tap {} {}".format(350, 1530))
device.shell("input tap {} {}".format(660, 1560))

# # ------------------------------------------
# # Abre app da lista de apps
# # ------------------------------------------
