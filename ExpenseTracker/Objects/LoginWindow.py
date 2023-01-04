from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox
from PIL import ImageTk, Image
class LoginWindow:
    def __init__(self, win, dbcursor, mydb, Connection):
        self.win = win
        self.mydb = mydb
        self.IsLoged = False
        self.showImage = ImageTk.PhotoImage(Image.open('./ExpenseTracker/Images/show.png'))
        self.hideImage = ImageTk.PhotoImage(Image.open('./ExpenseTracker/Images/hide.png'))
        #Background
        backgroundImg = ImageTk.PhotoImage(Image.open("./ExpenseTracker/Images/LoginBackground.jpg").resize((1300,750),Image.ANTIALIAS))

        self.Canvas = Canvas(self.win, width=1300, height=750, highlightthickness=0)
        self.Canvas.pack()
        self.Canvas.background = backgroundImg
        bg = self.Canvas.create_image(0, 0, anchor=NW, image=backgroundImg)

        #Login fields
        self.dbcursor = dbcursor

        self.loginFrame = Frame(self.win, width=375, height=650, background="#3b3b3b")
        self.loginFrame.pack_propagate(0)

        self.loginLabelTitle = Label(self.loginFrame, text="Please enter login details", background="#3b3b3b", foreground="#ffffff", font=('Colibri', 15))

        self.labelSpace1 = Label(self.loginFrame, text="", background="#3b3b3b")

        self.labelUsername = Label(self.loginFrame, text="Username", background="#3b3b3b", foreground="#ffffff", font=('Colibri', 13))

        self.loginUsernameEntryFrame = Frame(self.loginFrame, background="#3b3b3b")

        usernameIcon = ImageTk.PhotoImage(Image.open('./ExpenseTracker/Images/username_icon.png'))
        self.username_icon_label = Label(self.loginUsernameEntryFrame, image=usernameIcon, bg='#3b3b3b')
        self.username_icon_label.image = usernameIcon

        self.loginUsernameEntry = Entry(self.loginUsernameEntryFrame, highlightthickness=0, relief=FLAT, textvariable="username", background="#3b3b3b", foreground="#ffffff")

        self.username_icon_label_space = Label(self.loginUsernameEntryFrame, width=2, bg='#3b3b3b')

        self.loginUsernameLine = Canvas(self.loginFrame, width=185, height=1.0, bg="#bdb9b1", highlightthickness=0)

        self.labelSpace2 = Label(self.loginFrame, text="", background="#3b3b3b")

        self.loginPasswordEntryFrame = Frame(self.loginFrame, background="#3b3b3b")

        self.labelPassword = Label(self.loginFrame, text="Password", background="#3b3b3b", foreground="#ffffff", font=('Colibri', 13))

        passwordIcon = ImageTk.PhotoImage(Image.open('./ExpenseTracker/Images/password_icon.png'))
        self.password_icon_label = Label(self.loginPasswordEntryFrame, image=passwordIcon, bg='#3b3b3b')
        self.password_icon_label.image = passwordIcon

        self.loginPasswordEntry = Entry(self.loginPasswordEntryFrame, highlightthickness=0, relief=FLAT, textvariable="password", show= '*', background="#3b3b3b", foreground="#ffffff")

        self.loginShowButton = Button(self.loginPasswordEntryFrame, image=self.showImage, command=self.LoginHide, relief=FLAT, highlightthickness=0, activebackground="white", borderwidth=0, background="#3b3b3b", cursor="hand2")
        self.loginHideButton = Button(self.loginPasswordEntryFrame, image=self.hideImage, command=self.LoginShow, relief=FLAT, highlightthickness=0, activebackground="white", borderwidth=0, background="#3b3b3b", cursor="hand2")

        self.loginPasswordLine = Canvas(self.loginFrame, width=185, height=1.0, bg="#bdb9b1", highlightthickness=0)

        self.labelSpace3 = Label(self.loginFrame, text="", background="#3b3b3b")

        self.loginButtonValidate = Button(self.loginFrame, text="Login",    width=10, height=1, background="#3b3b3b", foreground="#ffffff", command = self.LoginValidate)
        self.loginButtonRegister = Button(self.loginFrame, text="register", width=10, height=1, background="#3b3b3b", foreground="#ffffff", command = self.RegisterWindowGenerate)

        #Register fields
        self.registerFrame = Frame(self.win, width=375, height=650, background="#3b3b3b")
        self.registerFrame.pack_propagate(0)

        self.registerLabelTitle = Label(self.registerFrame, text="Enter details to Register Account", background="#3b3b3b", foreground="#ffffff", font=('Colibri', 15))

        self.registerLabelSpace1 = Label(self.registerFrame, text="", background="#3b3b3b", foreground="#ffffff")

        self.registerLabelUsername = Label(self.registerFrame, text="Username",background="#3b3b3b", foreground="#ffffff", font=('Colibri', 13))

        self.registerUsernameEntry = Entry(self.registerFrame, textvariable="username", background="#3b3b3b", foreground="#ffffff")

        self.registerLabelSpace2 = Label(self.registerFrame, text="", background="#3b3b3b", foreground="#ffffff")

        self.registerLabelEmail = Label(self.registerFrame, text="Email",background="#3b3b3b", foreground="#ffffff", font=('Colibri', 13))

        self.registerEmailEntry = Entry(self.registerFrame, textvariable="email",background="#3b3b3b", foreground="#ffffff")

        self.registerLabelSpace3 = Label(self.registerFrame, text="", background="#3b3b3b", foreground="#ffffff")

        self.registerLabelPassword = Label(self.registerFrame, text="Password", background="#3b3b3b", foreground="#ffffff", font=('Colibri', 13))

        self.registerPasswordEntry = Entry(self.registerFrame, textvariable="password", show= '*', background="#3b3b3b", foreground="#ffffff")

        self.registerLabelSpace4 = Label(self.registerFrame, text="", background="#3b3b3b", foreground="#ffffff")

        self.registerButtonValidate = Button(self.registerFrame, text="Register", width=10, height=1, command = self.RegisterValidate, background="#3b3b3b", foreground="#ffffff")
        self.registerButtonLogin = Button(self.registerFrame, text="Login", width=10, height=1, command = self.LoginWindowGenerate, background="#3b3b3b", foreground="#ffffff")

        #No Conntection
        self.nologinFrame = Frame(self.win, width=375, height=155, background="#3b3b3b")
        self.nologinFrame.pack_propagate(0)
        self.ConnectionLabel = Label(self.nologinFrame, background="#3b3b3b", foreground="#ffffff", font=('Colibri', 13), text="\nError, no connection with our database\nPossible reasons:\n- No internet connection\n- Database maintenance ")
    def LoginShow(self):
        self.loginHideButton.pack_forget()
        self.loginShowButton.pack(side=LEFT)
        self.loginPasswordEntry.config(show='*')
    def LoginHide(self):
        self.loginShowButton.pack_forget()
        self.loginHideButton.pack(side=LEFT)
        self.loginPasswordEntry.config(show='')
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
    def LoginWindowGenerate(self):
        self.win.title("Login")
        try:
            self.Canvas.delete(self.RegisterWindow)
        except:
            pass
        self.LoginWindow = self.Canvas.create_window(650 - 375 / 2, 375 - 650 / 2, anchor=NW, window=self.loginFrame)
        self.loginLabelTitle.pack()
        self.labelSpace1.pack()
        self.labelUsername.pack()
        self.loginUsernameEntryFrame.pack()
        self.username_icon_label.pack(side=LEFT)
        self.loginUsernameEntry.pack(side=LEFT)
        self.username_icon_label_space.pack(side=LEFT)
        self.loginUsernameLine.pack()
        self.labelSpace2.pack()
        self.labelPassword.pack()
        self.loginPasswordEntryFrame.pack()
        self.password_icon_label.pack(side=LEFT)
        self.loginPasswordEntry.pack(side=LEFT)
        self.loginShowButton.pack(side=LEFT)
        self.loginPasswordLine.pack(pady=2)
        self.labelSpace3.pack()
        self.loginButtonValidate.pack()
        self.loginButtonRegister.pack()
    def RegisterWindowGenerate(self):
        self.win.title("Register")
        self.RegisterWindow = self.Canvas.create_window(650 - 375 / 2, 375 - 650 / 2, anchor=NW, window=self.registerFrame)
        self.Canvas.delete(self.LoginWindow)
        self.registerLabelTitle.pack()
        self.registerLabelSpace1.pack()
        self.registerLabelUsername.pack()
        self.registerUsernameEntry.pack()
        self.registerLabelSpace2.pack()
        self.registerLabelEmail.pack()
        self.registerEmailEntry.pack()
        self.registerLabelSpace3.pack()
        self.registerLabelPassword.pack()
        self.registerPasswordEntry.pack()
        self.registerLabelSpace4.pack()
        self.registerButtonValidate.pack()
        self.registerButtonLogin.pack()
    def NoConnection(self):
        self.win.title("No connection")
        self.LoginWindow = self.Canvas.create_window(650 - 375 / 2, 375 - 180 / 2, anchor=NW, window=self.nologinFrame)
        self.ConnectionLabel.pack()
    def LoginValidate(self):
        from tkinter import messagebox
        login = self.loginUsernameEntry.get()
        passw = self.loginPasswordEntry.get()

        if login == "" and passw == "":
            messagebox.showerror("Error","No Data Entered!")
        elif passw == "":
            messagebox.showerror("Error","Enter Password!")
        elif login == "":
            messagebox.showerror("Error","Enter Username!")
        else:
            self.dbcursor.execute("SELECT Login, Passw, UserID FROM user WHERE Login = '%s'" % (login))

            try:
                dbresult = self.dbcursor.fetchone()
                Login    = dbresult[0]
                Passw    = dbresult[1]
                UserID   = dbresult[2]

                if Login == login and Passw == passw:
                    self.Login   = Login
                    self.Passw   = Passw
                    self.UserID  = UserID
                    self.IsLoged = True
                    self.Canvas.pack_forget()
                else:
                    messagebox.showerror("Error","Wrong Password!")
            except:
                messagebox.showerror("Error","User doesn't exist!")
    def RegisterValidate(self):
        from tkinter import messagebox
        login = self.registerUsernameEntry.get()
        passw = self.registerPasswordEntry.get()
        email = self.registerEmailEntry.get()

        if login == "" and passw == "" and email == "":
            messagebox.showerror("Error","No Data Entered!")
        elif login == "":
            messagebox.showerror("Error","Enter Username!")
        elif email == "":
            messagebox.showerror("Error","Enter Your Email!")
        elif passw == "":
            messagebox.showerror("Error","Enter Password!")
        else:
            self.dbcursor.execute("SELECT Login, Passw, UserID FROM user WHERE Login = '%s'" % (login))
            if len(self.dbcursor.fetchall()) != 0:
                messagebox.showerror("Error","Account with that username already exists!")
            else:
                if len(passw) < 8:
                    messagebox.showerror("Error","Password should have at least 8 characters")
                elif len(passw) > 20:
                    messagebox.showerror("Error","Password should not be longer than 20 characters")
                elif not any(char.isdigit() for char in passw) and not any(char.islower() for char in passw) and not any(char.isupper() for char in passw):
                    messagebox.showerror("Error","Password should have at least one digit, Lower and Upper character")
                else:
                    self.dbcursor.execute("INSERT INTO `user` (`UserID`, `Login`, `Passw`, `Email`) VALUES (NULL, '%s', '%s', '%s')" % (login, passw, email))
                    self.mydb.commit()
                    self.dbcursor.execute("SELECT Login, Passw, UserID FROM user WHERE Login = '%s'" % (login))
                    result = self.dbcursor.fetchone()
                    self.dbcursor.execute("INSERT INTO `account` (`AccountID`, `Title`, `Money`, `Description`, `Type`, `Goal`, `StocksLine`, `UserID`) VALUES (NULL, 'First Account', '0', 'Your first account!', 1, 'null','null','%s')" % (result[2]))
                    self.mydb.commit()
                    self.Login   = result[0]
                    self.Passw   = result[1]
                    self.UserID  = result[2]
                    self.IsLoged = True
                    self.Canvas.pack_forget()
