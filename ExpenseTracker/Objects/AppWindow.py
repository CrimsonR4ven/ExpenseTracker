from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox
import Objects
class AppWindow:
    def __init__(self, win, dbcursor, accountUsed):
        #Variables - Args
        self.win = win
        self.dbcursor = dbcursor
        self.user = accountUsed

        #Variables -

        #Main Window - Main Frames
        self.mainMenuBarFrame   = Frame(win, background="#ff2b05", width=1500, height=50)
        self.mainSideBar        = Frame(win, background="#cccccc", width=350,  height=850)
        self.mainScreenFrame    = Frame(win, background="#eeeeee", width=1150, height=850)

        self.mainMenuBarFrame.pack_propagate(0)
        self.mainSideBar.pack_propagate(0)
        self.mainScreenFrame.pack_propagate(0)

        #Main Window - Containers
        self.mainScreenCanvas          = Canvas(self.mainScreenFrame, width=1150, height=850, background="#eeeeee", highlightthickness=0)
        self.mainScreenScrollableFrame = Frame(self.mainScreenCanvas, width=1150, height=850, background="#eeeeee")

        #Main Window - Scrollbars
        self.mainScreenScrollbar = ttk.Scrollbar(self.mainScreenFrame, orient="vertical", command=self.mainScreenCanvas.yview)

        #Main Window - Configuration
        self.mainScreenScrollableFrame.bind(
            "<Configure>",
            lambda e: self.mainScreenCanvas.configure(scrollregion = self.mainScreenCanvas.bbox("all"))   
        )
        self.mainScreenCanvas.create_window((0, 0), window=self.mainScreenScrollableFrame, anchor="nw")
        self.mainScreenCanvas.configure(yscrollcommand=self.mainScreenScrollbar.set)

        #Test space
        self.AP = Objects.AccountPresenter
        self.APlist = []
        x = 0
        for account in self.user.Accounts:
            self.APlist.append(self.AP.AccountPresent(self.mainScreenScrollableFrame, account))
            id = self.APlist[x].ID
            self.APlist[id].Frame.bind("<Button-1>",lambda event, ac=self.APlist[id].Account: self.AccountWindow(event,ac))
            x = x + 1
        
    def prop(self,n):
        return 360.0 * n / 1000

    def GenerateMainWindow(self):
        self.win.geometry("1500x900+-1+0")
        self.mainMenuBarFrame.pack()
        self.mainSideBar.pack(side=LEFT)
        self.mainScreenFrame.pack(side=LEFT)
        self.mainScreenScrollbar.pack(side=RIGHT, fill = Y)
        self.mainScreenCanvas.pack(expand=True)
        for ob in self.APlist:
            ob.pack()
    def AccountWindow(self,event,account):

        print("funny ah" + account.Title)
        pass