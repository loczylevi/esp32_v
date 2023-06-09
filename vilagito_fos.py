import machine
import time

sw = machine.Pin(0,machine.Pin.IN)

led = machine.Pin(2, machine.Pin.OUT)

while True:
    if sw.value() == 1:
        led.on()
    else:
        led.off()
        
    
