import json
import select
import socket
import threading
import sender_ui
import time

class Socket:
    receiveRunning=False
    sendRunning=False
    ak=1
    last=0
    list = []  # fereasra
    dim =0 # dimensiune fereastra se va citi din ui



    def creare(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        self.s.bind(('0.0.0.0', int(sender_ui.Sender_ui.porturi[0])))
        print(sender_ui.Sender_ui.porturi[0])
        self.dim = sender_ui.Sender_ui.dimensiune



    def receive_fct(self):
        print("Receive function")
        print("Receive")

        while self.receiveRunning:
            r, _, _ = select.select([self.s], [], [], 1)
            self.timer = threading.Timer(sender_ui.Sender_ui.timp, self.notreceived, args=None, kwargs=None)
            self.timer.start()
            if r :
                data, address = self.s.recvfrom(1024)
                strings = str(data).split("b'")
                split = strings[1].split("'")
                left=str(json.loads(split[0])['nr_pachet'])
                drept=str(self.last+1)
                print("Primit="+left)
                print("Ultimul="+drept)
                if(left==drept):
                    self.timer.cancel()
                    self.last = self.last + 1
                    self.ak = 1
                else:
                    if(drept<left): ## daca primesc un pachet dupa cel pierdut
                        self.timer.cancel()
            print(self.last)
            print(len(sender_ui.Sender_ui.jsonContenToSend))
            if (self.last == len(sender_ui.Sender_ui.jsonContenToSend)):
                print("Stop")
                self.sendRunning = False


    def send_fct(self):
        print("Send function")
        print(sender_ui.Sender_ui.porturi[1])
        print(sender_ui.Sender_ui.dip)
        while(self.last<len(sender_ui.Sender_ui.jsonContenToSend)-self.dim):#punem toate ferestrele si trimitem tot timpul primul element din fereastra
            if(self.ak==1):
                print("Ak=1")
                print("Creare fereastra")
                i = 0
                contor=self.last
                if(len(self.list)==0):
                  print("Lista este goala")
                  while(i<self.dim):
                     print("Put element!")
                     print(sender_ui.Sender_ui.jsonContenToSend[contor])
                     element = json.dumps(sender_ui.Sender_ui.jsonContenToSend[contor])
                     self.s.sendto(bytes(element, encoding="ascii"),(sender_ui.Sender_ui.dip, sender_ui.Sender_ui.porturi[1]))
                     self.list.append(sender_ui.Sender_ui.jsonContenToSend[contor]) #tinem minte toate pachetele in tranzit fereastra
                     i=i+1
                     contor=contor+1
                else:
                    print("Avem pachete in tranzit")
                    self.list=[]
                    while (i < self.dim):
                        print("Put element!")
                        print(sender_ui.Sender_ui.jsonContenToSend[contor])
                        self.list.append(sender_ui.Sender_ui.jsonContenToSend[contor])  # tinem minte toate pachetele in tranzit fereastra
                        i = i + 1
                        contor = contor + 1

                    element = json.dumps(self.list[self.dim-1])
                    print("Se trimite ultimul:")
                    print(element)
                    self.s.sendto(bytes(element, encoding="ascii"),(sender_ui.Sender_ui.dip, sender_ui.Sender_ui.porturi[1]))

                self.ak=2
            else:
                if (self.ak==0):
                    print("ak=0")
                    self.notreceived()





    def notreceived(self):
        print("Not received")
        self.timer.cancel()
        i=0
        if(len(self.list)!=0):
            while(i<self.dim):
                 element = json.dumps(self.list[i])
                 print(element)
                 self.s.sendto(bytes(element, encoding="ascii"),(sender_ui.Sender_ui.dip, sender_ui.Sender_ui.porturi[1]))
                 i=i+1
                 self.ak=2













