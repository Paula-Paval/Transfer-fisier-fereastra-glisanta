import socket
import sys
import select
import threading

from sender_ui import Sender_ui


def receive_fct():
    global running
    contor = 0
    while running:
        # Apelam la functia sistem IO -select- pentru a verifca daca socket-ul are date in bufferul de receptie
        # Stabilim un timeout de 1 secunda
        r, _, _ = select.select([s], [], [], 1)
        if not r:
        	contor = contor + 1
        else:
            data, address = s.recvfrom(1024)
            print("S-a receptionat ", str(data), " de la ", address)
            print("Contor= ", contor)

#citere valori de conectare
gui=Sender_ui("sender")
gui.afisare()
sport=gui.sport()
dport=gui.dport()
dip=gui.dip()
print(sport)
print(dport)
print(dip)

# Creare socket UDP
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)

s.bind(('0.0.0.0', int(sport)))

running = True

try:
    receive_thread = threading.Thread(target=receive_fct)
    receive_thread.start()
except:
    print("Eroare la pornirea thread‐ului")
    sys.exit()

while True:
    try:
        data = gui.text()
        s.sendto(bytes(data, encoding="ascii"), (dip, int(dport)))
    except KeyboardInterrupt:
        running = False
        print("Waiting for the thread to close...")
        receive_thread.join()
        break

