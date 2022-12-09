from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox
class LoginWindow:
    def __init__(self, win, dbcursor, accountUsed, mydb):
        #Login fields
        self.win = win
        self.dbcursor = dbcursor

        self.loginFrame = Frame(self.win)

        self.loginLabelTitle = Label(self.loginFrame, text="Please enter login details")

        self.labelSpace1 = Label(self.loginFrame, text="")

        self.labelUsername = Label(self.loginFrame, text="Username")

        self.loginUsernameEntry = Entry(self.loginFrame, textvariable="username")

        self.labelSpace2 = Label(self.loginFrame, text="")

        self.labelPassword = Label(self.loginFrame, text="Password")

        self.loginPasswordEntry = Entry(self.loginFrame, textvariable="password", show= '*')

        self.labelSpace3 = Label(self.loginFrame, text="")

        self.loginButtonValidate = Button(self.loginFrame, text="Login", width=10, height=1, command = self.LoginReturn)
        self.loginButtonRegister = Button(self.loginFrame, text="register", width=10, height=1, command = self.RegisterWindowGenerate)

        #Register fields
        self.registerFrame = Frame(self.win)

        self.registerLabelTitle = Label(self.registerFrame, text="Please enter login details")

        self.registerLabelSpace1 = Label(self.registerFrame, text="")

        self.registerLabelUsername = Label(self.registerFrame, text="Username")

        self.registerUsernameEntry = Entry(self.registerFrame, textvariable="username")

        self.registerLabelSpace2 = Label(self.registerFrame, text="")

        self.registerLabelPassword = Label(self.registerFrame, text="Password")

        self.registerPasswordEntry = Entry(self.registerFrame, textvariable="password", show= '*')

        self.registerLabelSpace3 = Label(self.registerFrame, text="")

        self.registerButtonValidate = Button(self.registerFrame, text="Register", width=10, height=1, command = self.LoginReturn)
        self.registerButtonLogin = Button(self.registerFrame, text="Login", width=10, height=1, command = self.LoginWindowGenerate)
    def LoginReturn(self):
        login = self.usernameLoginEntry.get()
        passw = self.passwordLoginEntry.get()
        self.dbcursor.execute("SELECT Login, Passw, UserID FROM user WHERE Login = ")
        dbresult = self.dbcursor.fetchall()
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
    def LoginWindowGenerate(self):
        try:
            self.registerFrame.pack_forget()
        except:
            pass
        self.loginFrame.pack()
        self.loginLabelTitle.pack()
        self.labelSpace1.pack()
        self.labelUsername.pack()
        self.loginUsernameEntry.pack()
        self.labelSpace2.pack()
        self.labelPassword.pack()
        self.loginPasswordEntry.pack()
        self.labelSpace3.pack()
        self.loginButtonValidate.pack()
        self.loginButtonRegister.pack()
    def RegisterWindowGenerate(self):
        self.loginFrame.pack_forget()
        self.registerFrame.pack()
        self.registerLabelTitle.pack()
        self.registerLabelSpace1.pack()
        self.registerLabelUsername.pack()
        self.registerUsernameEntry.pack()
        self.registerLabelSpace2.pack()
        self.registerLabelPassword.pack()
        self.registerPasswordEntry.pack()
        self.registerLabelSpace3.pack()
        self.registerButtonValidate.pack()
        self.registerButtonLogin.pack()
