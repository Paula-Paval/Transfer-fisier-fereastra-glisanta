import select
import socket
import sender_ui

class Socket:
    receiveRunning=False
    sendRunning=False

    def creare(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        self.s.bind(('0.0.0.0', int(sender_ui.Sender_ui.porturi[0])))
        print(sender_ui.Sender_ui.porturi[0])

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
                if(str(data)=="b'stop'"):##se va schimba odata cu implementarea
                    print("Stop threads")
                    self.sendRunning=False


    def send_fct(self):
        print("Send function")
        print(sender_ui.Sender_ui.porturi[1])
        print(sender_ui.Sender_ui.dip)
   #     while self.sendRunning:
        data=sender_ui.Sender_ui.jsonContenToSend
        ##algoritm
        if(data=="stop"):
            print("Stop threads")

            self.sendRunning = False
        else:
            self.s.sendto(bytes(data, encoding="ascii"), (sender_ui.Sender_ui.dip, sender_ui.Sender_ui.porturi[1]))






