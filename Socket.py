import select
import socket

import receiver_ui


class Socket:
    receiveRunning=False
    sendRunning=False

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
                data, address = self.s.recvfrom(1024)
                print("S-a receptionat ", str(data), " de la ", address)
                print("Contor= ", contor)
                self.s.sendto(bytes(str(data), encoding="ascii"),(receiver_ui.Receiver_ui.dip, receiver_ui.Receiver_ui.porturi[1]))
                if(str(data)=="b'stop'"):
                    print("Stop threads")
                    self.sendRunning=False



