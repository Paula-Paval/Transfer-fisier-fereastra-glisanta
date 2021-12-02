import threading
import tkinter
from tkinter import *

from Socket import Socket


class Sender_ui:
    porturi=[0, 0]
    dip=""
    text=""
    def __init__(self, nume):
        self.fereastra=Tk(className=nume)

    def setConnectionInfo (self):
        Sender_ui.porturi[0] = int(self.entry1.get())
        Sender_ui.porturi[1] =int(self.entry2.get())
        Sender_ui.dip = self.entry3.get()
        self.s = Socket()
        self.s.creare()
        try:
            self.s.receiveRunning = True
            print("Create  threads")
            self.receive_thread = threading.Thread(target=self.s.receive_fct)
            self.receive_thread.start()
        except:
            print("Eroare la pornirea   thread‐urilor")
            sys.exit()

    def getText(self):
        Sender_ui.text=self.entry4.get()
        print(Sender_ui.text)
        try:
            self.s.sendRunning = True
            print("Create  threads")
            self.send_thread = threading.Thread(target=self.s.send_fct)
            self.send_thread.start()

        except:
            print("Eroare la pornirea   thread‐urilor")
            sys.exit()
        return
    def Disconnect(self):
        self.s.receiveRunning=False

    def afisare(self):
        self.fereastra.geometry("500x500")
        self.l1 = Label(self.fereastra, text="Port sursa")
        self.l1.place(x=95, y=40)
        self.entry1 = tkinter.Entry(self.fereastra, width="15")
        self.entry1.place(x=150, y=40)
        self.l2 = Label(self.fereastra, text="Port  destinatie")
        self.l2.place(x=67, y=60)
        self.entry2 = tkinter.Entry(self.fereastra, width="15")
        self.entry2.place(x=150, y=60)
        self.l3 = Label(self.fereastra, text="Ip destinatie")
        self.l3.place(x=80, y=80)
        self.entry3 = tkinter.Entry(self.fereastra, width="30")
        self.entry3.place(x=150, y=80)
        bunttonConnect=tkinter.Button(self.fereastra,text="Connect", command=self.setConnectionInfo ).place(x=300, y=110)
        bunttonDisconnect = tkinter.Button(self.fereastra, text="Disconnect", command=self.Disconnect).place(x=100,y=110)
        self.l4=Label(self.fereastra, text="Mesaj de trimis")
        self.l4.place(x=60, y=160)
        self.entry4=tkinter.Entry(self.fereastra,width="40")
        self.entry4.place(x=160, y=160)
        bunttonSend =tkinter.Button(self.fereastra,text="Send", command=self.getText).place(x=350, y=190)
        self.fereastra.mainloop()




