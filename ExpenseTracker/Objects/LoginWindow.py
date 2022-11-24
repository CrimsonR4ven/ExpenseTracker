from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox
class TransactionService:
    def __init__(self, win, dbcursor, accountUsed, mydb, alter = None):
        self.LoginWindow = Toplevel(win)
        self.LoginWindow.geometry("200x200+-1+0")
        __LoginWindow()

    def __LoginWindow(self):
        self.LoginFrame = Frame(self.LoginWindow)
        self.LoginFrame.pack()

        self.labelTitle = Label(self.LoginFrame, text="Please enter login details")
        self.labelTitle.pack()

        self.labelSpace1 = Label(self.LoginFrame, text="")
        self.labelSpace1.pack()

        self.labelUsername = Label(self.LoginFrame, text="Username")
        self.labelUsername.pack()

        self.usernameLoginEntry = Entry(self.LoginFrame, textvariable="username")
        self.usernameLoginEntry.pack()

        self.labelSpace2 = Label(self.LoginFrame, text="")
        self.labelSpace2.pack()

        self.labelPassword = Label(self.LoginFrame, text="Password")
        self.labelPassword.pack()

        self.passwordLoginEntry = Entry(self.LoginFrame, textvariable="password", show= '*')
        self.passwordLoginEntry.pack()

        self.labelSpace3 = Label(self.LoginFrame, text="")
        self.labelSpace3.pack()

        self.buttonLogin = Button(self.LoginFrame, text="Login", width=10, height=1, command = )
        #add command return
        self.buttonLogin.pack()
    def __LoginReturn(self):
        login = self.usernameLoginEntry.get()
        passw = self.passwordLoginEntry.get()
        dbcursor.execute("SELECT Login, Passw, UserID FROM user")
        dbresult = dbcursor.fetchall()
        for x in dbresult:
            Login = x[0]
            Passw = x[1]
            userID = x[2]
            if Login == login and Passw == passw:
                self.User = x
    def __DestroyLoginWindow(self):
        self.LoginFrame.destroy()
        pass
    def __RegisterWindow(self):
        pass
    def __DestroyRegisterWindow(self):
        pass
    def GetUser(self):
        return self.User
