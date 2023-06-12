import machine
import time
import random
sw = machine.Pin(0,machine.Pin.IN)
led = machine.Pin(2, machine.Pin.OUT)
hangszoro = machine.Pin(26, machine.Pin.OUT)

pwm = machine.PWM(hangszoro)
pwm.freq(500)
pwm.duty(0)

def handle_interrupt(pin):
    print("\n______________\tMorze kód elindult\t______________\n")
    leforditando = "...---..."
    for betu in leforditando:
        if betu == ".":
            pwm.duty(100)
            time.sleep(0.10)
            pwm.duty(0)
        elif betu == "-":
            pwm.duty(100)
            time.sleep(0.25)
            pwm.duty(0)
        time.sleep(0.10)
        print("!",end="")


sw.irq(trigger=machine.Pin.IRQ_FALLING, handler=handle_interrupt)  #ha fut egy loop és ez aktiválodik akkor leállít mindentés ezt futtatja szoval abba hagyja a randomdolgok kiválasztását a listából és elkezdi prioritássalkiirni a '!' jeleket

lista = ["morze fos","NE PINGELJÉ MÁ'","bojler eladó ugyanitt","BUKSI HOL VAGY?","kiesett az aranyhal az akváriumból","mind megbukunk let's gooo","carpe diem","deus ex machine","divide et impara","cuius regio eius religio","in medium res","panem et cirsensen","Si vis pacem, para bellum.","Alea iacta est.","Ave Caesar, morituri te salutant!","Cogito, ergo sum","Dum spiro, spero","Nomen est omen","Repetitio est mater studiorum.","Veni, Vidi, Vici!"]
while True:
    print("\ngomb lenyomása esetén morze leforditása hangra, továbbá pár oldsaying\t", random.choice(lista))
    time.sleep(0.1)
    
