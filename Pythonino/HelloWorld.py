from pyfirmata import Arduino, util
import time

Mega = Arduino('COM5')
ledPin = 13

print('Hello World!')

while True:
    Mega.digital[13].write(1)
    print('LED ligado')
    time.sleep(0.1)

    Mega.digital[ledPin].write(0)
    print('LED desligado')
    time.sleep(0.1)