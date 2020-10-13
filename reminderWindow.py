import tkinter as tk
from tkinter import ttk
from tkinter import *
class MainPopup():
    def __init__(self,popupInfo):
        self.info = popupInfo
        self.tk = tk.Tk()
        self.tk.lift()
        #self.tk.attributes('-zoomed', True)  # This just maximizes it so we can see the window. It's nothing to do with fullscreen.
        self.tk.attributes("-fullscreen",True)
        self.tk.configure(background='green')
        self.tk.attributes("-transparentcolor","green")
        self.frame = Frame(self.tk)
        self.frame.pack()
        self.state = False
        
        
        
        self.msg = self.generateMessage()
        self.createGui()

    def generateMessage(self):
        outstring = ""
        for k in self.info.keys():
            if (k == "Water"):
                outstring+= "Drink Some Water! "
            if (k == "Standing" and len(self.info) > 1):
                outstring+= "Also - go for a walk!"
            elif (k =="Standing"):
                outstring+="Go for a walk!"
        return outstring
    def createGui(self):
        # frame1 = tk.LabelFrame(self,text="ddfjjkdf",width=300,height=130,bd=5)
        # frame1.grid(row=0,column=0,columnspan=3,padx=8)
        #
        self.label =ttk.Label(self.tk, text =self.msg,font="Verdana")
        #self.label.pack(side="top",fill="x",pady=10)
        self.label.place(x=1000,y=500,anchor="center")
        self.B1 = ttk.Button(self.tk,text="Okay", command = self.tk.destroy)
        self.B1.place(x=1000,y=550,anchor="center")
        #self.B1.pack()


def generatePopup(popupInfo):
    p = MainPopup(popupInfo)
    p.tk.mainloop()
#testdict = {"Water":[20,30],"Standing":100}
#generatePopup(testdict)