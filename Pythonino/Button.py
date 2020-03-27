from pyfirmata import Arduino, util
import time

Mega = Arduino('COM5')
it = util.Iterator(Mega)
it.start()
button = Mega.get_pin('d:2:i')
buttonOldState = True
contador = 0

while True:
    time.sleep(0.05)

    buttonState = button.read()

    if buttonState == 0 and buttonOldState :
        contador += 1
        print(contador)

    if contador >= 5 :
        Mega.digital[13].write(1)
    else:
        Mega.digital[13].write(0)

    buttonOldState = buttonState
