import json
import select
import socket
import time

import random

import receiver_ui


class Socket:
    receiveRunning=False
    sendRunning=False
    list=[]
    last=1

    def creare(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        self.s.bind(('0.0.0.0', int(receiver_ui.Receiver_ui.porturi[0])))
        print(receiver_ui.Receiver_ui.porturi[0])

    def receive_fct(self):
        print("Receive function")
        contor = 0

        while self.receiveRunning:
            # Apelam la functia sistem IO -select- pentru a verifca daca socket-ul are date in bufferul de receptie
            # Stabilim un timeout de 1 secunda
            r, _, _ = select.select([self.s], [], [], 1)
            if not r:
                contor = contor + 1
            else:
                 #Se va crea lista de pachete
                 data, address = self.s.recvfrom(1024)
                 strings=str(data).split("b'")
                 split=strings[1].split("'")
                 dic = {"nr_pachet": json.loads(split[0])['nr_pachet'], "data": json.loads(split[0])['data'], "numar_pachete": json.loads(split[0])['numar_pachete']}
                 #print(str(split[0]))
                 pachet = json.loads(split[0])['nr_pachet']
                 totalPachete=json.loads(split[0])['numar_pachete']
                 confirm={'nr_pachet': pachet}
                 x = random.random()
                 ultimul=self.last
                 nrPachet=int(pachet)
                 if (x > receiver_ui.Receiver_ui.probabilitate and  ultimul==nrPachet):
                    self.last=self.last+1
                    print(x)
                    print("Lista noastra are:")
                    self.list.append(dic)
                    for x in self.list:
                        print(x)
                    self.s.sendto(bytes(json.dumps(confirm), encoding='ascii'),(receiver_ui.Receiver_ui.dip, receiver_ui.Receiver_ui.porturi[1]))
                    print(json.dumps(confirm))
                    if(str(pachet)==str(totalPachete)):
                         receiver_ui.Receiver_ui.lista_json=self.list
                         self.receiveRunning=False
                         self.sendRunning=False
                 else:
                    print(x)
                    print(ultimul)
                    print(nrPachet)
                    print("Nu am primit")









