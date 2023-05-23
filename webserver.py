import network
import time as t
import socket
import machine
import urandom
sta = network.WLAN(network.STA_IF)

sta.active(1)

sta.connect(
    "ha","3.1415926")

while not sta.isconnected():
    print("!",end="")
    t.sleep(0.1)
    


print("Devices is connected")


for ssid in sta.scan():
    print(ssid[0])
    

html = """<!DOCTYPE html>
<html lang="hu">
<meta charset="UTF-8">
<title>fürdősó</title>
<meta name="viewport" content="width=device-width,initial-scale=1">
<style>
    h1{
    color: green;
    }
</style>
<body>
 <h1>yamate yamato</h1>
 <p>This is a paragraph.</p>
 <p>This is another paragraph.</p>
</body>
</html>"""

addres = socket.getaddrinfo('0.0.0.0',80)[0][-1]

zokni = socket.socket()

zokni.bind(addres)

zokni.listen(1)
stop= machine.Pin(0,machine.Pin.IN,machine.Pin.PULL_UP)
szinek = ["red","yellow","brown","blue","black","orange","#391069"]

while stop.value():
    cl, addr = zokni.accept()
    cl_file = cl.makefile("rwb",0)
    while True:
        line = cl_file.readline()
        if not line or line == b'\r\n':
            break
    szeletelo = html.split("\n")
    veletlen = urandom.choice(szinek)
    reg = ""
    for elem in szeletelo:
        if "color:" in elem:
            elem = "    color: " + veletlen + ";"
        reg = reg + elem + "\n"
    cl.send(reg)
    cl.close()
    
