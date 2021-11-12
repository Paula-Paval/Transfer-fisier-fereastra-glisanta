import tkinter
from tkinter import *
class Sender_ui:
    def __init__(self, nume):
        self.fereastra=Tk(className=nume)

    def getConnectionInfo (self):
        self.sport = int(self.entry1.get())
        self.dport =int(self.entry2.get())
        self.dip = self.entry3.get()
        var = IntVar()
        self.fereastra.after(3000, var.set, 1)
        print("waiting...")
        self.fereastra.wait_variable(var)
        print("done")
        return
    def getText(self):
        self.text=self.entry4.get()
        print(self.text)
        return
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
        bunttonSubmit=tkinter.Button(self.fereastra,text="Submit", command=self.getConnectionInfo ).place(x=300, y=110)
        self.l4=Label(self.fereastra, text="Mesaj de trimis")
        self.l4.place(x=60, y=160)
        self.entry4=tkinter.Entry(self.fereastra,width="40")
        self.entry4.place(x=160, y=160)
        bunttonSend =tkinter.Button(self.fereastra,text="Send", command=self.getText).place(x=350, y=190)
        self.fereastra.mainloop()
