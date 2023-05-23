import machine  #root könyvtár
import time

print(dir(machine))

led = machine.Pin(2, machine.Pin.OUT)  #OUT = kimenet 

bemenet = machine.Pin(0, machine.Pin.IN, machine.Pin.PULL_UP)  # IN = bemenet 

def villogtato():
    for szam in range(0,20):
        led.on()
        time.sleep(0.1)
        led.off()
        time.sleep(0.1)
    
bemenet.irq(trigger=machine.Pin.IRQ_FALLING, handler =lambda t: print("༼ つ ◕_◕ ༽つ"))



"""
for szam in range(0,20):
    overflow.on()
    time.sleep(1)
    overflow.off()
    time.sleep(1)
"""


"""
import esp32
while True:
    time.sleep(2)
    homerseklet = esp32.raw_temperature()
    atvaltas = (homerseklet - 32) / 1.8
    print(atvaltas)
    time.sleep(2)
"""

