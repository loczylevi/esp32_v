import machine  #root könyvtár
import time

print(dir(machine))

overflow = machine.Pin(2, machine.Pin.OUT)

for szam in range(0,20):
    overflow.value(not overflow.value())  #ha a valueban nem rakunk semmilyen értéket akkor lekéri az állapotát és NOT-al ellentétes állapotba lökjük
    time.sleep(1)
    

"""
for szam in range(0,20):
    overflow.on()
    time.sleep(1)
    overflow.off()
    time.sleep(1)
"""
