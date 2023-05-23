
import machine
import time

led = machine.Pin(2, machine.Pin.OUT)


def blinking(hanyszor,szunet,szoveg):
    c = 0
    while c < hanyszor:
        led.on()
        time.sleep(szunet)
        led.off()
        time.sleep(szunet)
        c = c + 1
    return szoveg


    

