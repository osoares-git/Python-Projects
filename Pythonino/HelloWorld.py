from pyfirmata import Arduino, util
import time

Mega = Arduino('COM6')

print('Hello World!')

while True:
    Mega.digital[13].write(1)
    print('LED ligado')
    time.sleep(1)

    Mega.digital[13].write(0)
    print('LED desligado')
    time.sleep(1)