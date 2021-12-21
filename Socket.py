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

    def creare(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        self.s.bind(('0.0.0.0', int(sender_ui.Sender_ui.porturi[0])))
        print(sender_ui.Sender_ui.porturi[0])

    def receive_fct(self):
        print("Receive function")
        while self.receiveRunning:
            timer = threading.Timer(2, self.notreceived, args = None, kwargs = None)
            timer.start()
            r, _, _ = select.select([self.s], [], [], 1)
            if r :
                timer.cancel()
                data, address = self.s.recvfrom(1024)
                print("S-a receptionat ", str(data), " de la ", address)
                self.last=self.last+1
                self.ak=1

            else:
                 self.ak=0

            if (self.index==len(sender_ui.Sender_ui.jsonContenToSend)):
                print("Stop threads")
                self.sendRunning = False


    def send_fct(self):
        print("Send function")
        print(sender_ui.Sender_ui.porturi[1])
        print(sender_ui.Sender_ui.dip)
        dim=3 # dimensiune fereastra se va citi din ui
        while(self.last<len(sender_ui.Sender_ui.jsonContenToSend)-dim):
            if(self.ak==1):
                i = 0
                contor=self.last
                while(i<3):
                    self.list.append(sender_ui.Sender_ui.jsonContenToSend[contor]) #tinem minte toate pachetele in tranzit fereastra
                    element = json.dumps((sender_ui.Sender_ui.jsonContenToSend[contor]))
                    self.s.sendto(bytes(element, encoding="ascii"),(sender_ui.Sender_ui.dip, sender_ui.Sender_ui.porturi[1]))
                    i=i+1
                    contor=contor+1
            else:
                if (self.ak==0):
                    self.notreceived()
        if(self.last==len(sender_ui.Sender_ui.jsonContenToSend)-dim):
            self.sendRunning=False


    def notreceived(self):
      for element in self.list:
           self.s.sendto(bytes(element, encoding="ascii"), (sender_ui.Sender_ui.dip, sender_ui.Sender_ui.porturi[1]))









