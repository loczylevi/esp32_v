import machine
import time

sw = machine.Pin(0,machine.Pin.IN)

led = machine.Pin(2, machine.Pin.OUT)

def blinking_leds(num, t_on, t_off, msg):
    for _ in range(num):
        led.on()
        time.sleep(t_on)
        led.off()
        time.sleep(t_off)
    print(msg)
    

while True:
    if sw.value() == 0:
        blinking_leds(15, 0.5, 0.5, "END")
        
        
    
