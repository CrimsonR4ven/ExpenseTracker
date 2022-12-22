from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox
class AppWindow:
    def __init__(self, win, dbcursor, accountUsed):
        #Variables - Args
        self.win = win
        self.dbcursor = dbcursor
        self.account = accountUsed

        #Variables -

        #Main Window - Main Frames
        self.mainMenuBarFrame   = Frame(win, background="#ff2b05", width=1500, height=50)
        self.mainSideBar        = Frame(win, background="#dddddd", width=350,  height=850)
        self.mainScreenFrame    = Frame(win, background="#eeeeee", width=1150, height=850)

        self.mainMenuBarFrame.pack_propagate(0)
        self.mainSideBar.pack_propagate(0)
        self.mainScreenFrame.pack_propagate(0)

        #Main Window - Containers
        self.mainScreenCanvas          = Canvas(self.mainScreenFrame)
        self.mainScreenScrollableFrame = Frame(self.mainScreenCanvas)

        #Main Window - Scrollbars
        self.mainScreenScrollbar = ttk.Scrollbar(self.mainScreenFrame, orient="vertical", command=self.mainScreenCanvas.yview)

        #Main Window - Configuration
        self.mainScreenScrollableFrame.bind(
            "<Configure>",
            lambda e: self.mainScreenCanvas.configure(scrollregion = self.mainScreenCanvas.bbox("all"))   
        )
        self.mainScreenCanvas.create_window((0, 0), window=self.mainScreenScrollableFrame, anchor="nw")
        self.mainScreenCanvas.configure(yscrollcommand=self.mainScreenScrollbar.set)

    def GenerateMainWindow(self):
        self.win.geometry("1500x900+-1+0")
        self.mainMenuBarFrame.pack()
        self.mainSideBar.pack(side=LEFT)
        self.mainScreenFrame.pack(side=LEFT)
        self.mainScreenScrollbar.pack(side=RIGHT, fill = Y)
        for i in range(0,150):
            l = Label(self.mainScreenFrame, text = "Fact of the Day")
            l.pack()