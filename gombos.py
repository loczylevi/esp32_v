import machine
import time

sw = machine.Pin(0,machine.Pin.IN)

a = 0
while a < 100:
    time.sleep(0.5)
    if sw.value() == 1:
        print(sw.value()," True...")
    else:
        print(sw.value()," False...")
    time.sleep(0.5)
    a = a + 1
    
    

