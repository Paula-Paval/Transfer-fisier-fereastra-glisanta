import json
import select
import socket
import threading
import sender_ui

class Socket:
    receiveRunning=False
    sendRunning=False
    index=0
    ak=1
    last=0
    list = []  # fereasra
    dim = 3  # dimensiune fereastra se va citi din ui
    left=1

    def creare(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        self.s.bind(('0.0.0.0', int(sender_ui.Sender_ui.porturi[0])))
        print(sender_ui.Sender_ui.porturi[0])

    def receive_fct(self):
        print("Receive function")
        print("Receive")
        while self.receiveRunning:
            timer = threading.Timer(900, self.notreceived, args = None, kwargs = None)
            r, _, _ = select.select([self.s], [], [], 1)
            if r :
               # print("Exista ceva in buffer")
                timer.start()
                data, address = self.s.recvfrom(1024)
                strings = str(data).split("b'")
                split = strings[1].split("'")
                #print("S-a receptionat ", split[0], " de la ", address)
                left=str(json.loads(split[0])['nr_pachet'])
                drept=str(self.last+1)
                print("Primit="+left)
                print("Ultimul="+drept)

                if(left==drept):
                   # print("********************************************************")
                    timer.cancel()
                    self.last = self.last + 1
                    self.ak = 1
                else:
                   # print("intra pe else")
                    self.ak=0
            print(self.last)
            print(len(sender_ui.Sender_ui.jsonContenToSend))
            if (self.last == len(sender_ui.Sender_ui.jsonContenToSend)):
                print("Stop")
                self.sendRunning = False


    def send_fct(self):
        print("Send function")
        print(sender_ui.Sender_ui.porturi[1])
        print(sender_ui.Sender_ui.dip)

        while(self.last<len(sender_ui.Sender_ui.jsonContenToSend)-self.dim):
            if(self.ak==1):
                print("Ak=1")
                print("Creare fereastra")
                i = 0
                contor=self.last
                if(len(self.list)==3):
                    self.list=[]
                while(i<3):
                    print("Put element!")
                    print(sender_ui.Sender_ui.jsonContenToSend[contor])
                    self.list.append(sender_ui.Sender_ui.jsonContenToSend[contor]) #tinem minte toate pachetele in tranzit fereastra
                    i=i+1
                    contor=contor+1
                element = json.dumps(self.list[0])
                self.s.sendto(bytes(element, encoding="ascii"),(sender_ui.Sender_ui.dip, sender_ui.Sender_ui.porturi[1]))
                self.ak=2
            else:
                if (self.ak==0):
                    print("ak=0")
                    self.notreceived()

        while(self.left<=self.dim-1):
            if(self.ak==1):
                element = json.dumps(self.list[self.left])
                self.s.sendto(bytes(element, encoding="ascii"),(sender_ui.Sender_ui.dip, sender_ui.Sender_ui.porturi[1]))
                self.ak = 2
                self.left=self.left+1
            else:
                if (self.ak == 0):
                    print("ak=0")
                    self.notreceived()
        print(self.last)
        print(len(sender_ui.Sender_ui.jsonContenToSend))
        if(self.last==len(sender_ui.Sender_ui.jsonContenToSend)):
            print("Stop")
            self.sendRunning=False


    def notreceived(self):
      print("Not received")
      for element in self.list:
           text = json.dumps(element)
           self.s.sendto(bytes(text, encoding="ascii"), (sender_ui.Sender_ui.dip, sender_ui.Sender_ui.porturi[1]))









