import machine
import time
import random
sw = machine.Pin(0,machine.Pin.IN)
led = machine.Pin(2, machine.Pin.OUT)
lista = ["ervin","vilmos","Rommel","Lócaj","anya","cumi","tonk","mocárd"]
enabled = True
def handle_interrupt(pin):
    while not sw.value():
        print("!",end="")
        time.sleep(0.1)
    global enabled
    enabled = False

    
        

sw.irq(trigger=machine.Pin.IRQ_FALLING, handler=handle_interrupt)  #ha fut egy loop és ez aktiválodik akkor leállít mindentés ezt futtatja szoval abba hagyja a randomdolgok kiválasztását a listából és elkezdi prioritássalkiirni a '!' jeleket

""" ha fut egy loop és ez aktiválodik akkor leállít mindent
és ezt futtatja szoval abba hagyja a random
dolgok kiválasztását a listából és elkezdi prioritással
kiirni a '!' jeleket"""

while enabled:
    print("\nrandom cuccmok", random.choice(lista))
    time.sleep(0.1)
    

