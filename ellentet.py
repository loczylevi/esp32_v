import machine
import time

sw = machine.Pin(0,machine.Pin.IN)

led = machine.Pin(2, machine.Pin.OUT)

def handle_innerrupt(pin):
    led.value(not led.value())
sw.irq(rtrigger=machine.Pin.IRQ_FALLING, handler=handle_interrupt)
