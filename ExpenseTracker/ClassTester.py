from tkinter import *
from tkinter import ttk
from Objects.Transaction import *
from Objects.Account import *
from Objects.User import *
from Objects.LoginWindow import *
from TransactionService import *
import mysql.connector
import datetime
from PIL import ImageTk, Image
#DB connection
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="tracker"
)
dbcursor = mydb.cursor()
win = Tk()
isLoged = False
backgroundImg = ImageTk.PhotoImage(Image.open("./Images/LoginBackground.jpeg"))

mydb.commit()
def Center():
    win.update_idletasks()
    width = win.winfo_width()
    frm_width = win.winfo_rootx() - win.winfo_x()
    win_width = width + 2 * frm_width
    height = win.winfo_height()
    titlebar_height = win.winfo_rooty() - win.winfo_y()
    win_height = height + titlebar_height + frm_width
    x = win.winfo_screenwidth() // 2 - win_width // 2
    y = win.winfo_screenheight() // 2 - win_height // 2
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    win.deiconify()
def RegisterWindow():
    pass

def LoginValidator():
    from tkinter import messagebox
    from tkinter.ttk import Combobox
    global isLoged
    login = username_login_entry.get()
    passw = password__login_entry.get()
    dbcursor.execute("SELECT Login, Passw, UserID FROM user")
    dbresult = dbcursor.fetchall()
    for x in dbresult:
        Login = x[0]
        Passw = x[1]
        userID = x[2]
        if passw == "":
            messagebox.showerror("Error","Enter Password!")
            break;
        elif login == "":
            messagebox.showerror("Error","Enter Username!")
            break;
        elif Login == login and Passw == passw:
            loginFrame.destroy()
            global userLoged
            userLoged = User(Login, Passw, userID, dbcursor, mydb)
            userLoged.ListAccounts()
            #Add to User List of Accounts

            win.geometry("1200x600")
            Center()
            win.attributes("-fullscreen", True)

            label = ttk.Label(win, text="Da tracker", font=("Courier 22"))
            label.grid(row = 0, column = 0)

            label2 = ttk.Label(win, text="ye", font=("Courier 22"))
            label2.grid(row = 1, column = 0)
            global accountList
            accountList = []
            for x in userLoged.Accounts:
                accountList.append(x.Title)
            global comboboxAccounts
            comboboxAccounts = Combobox(win, values = accountList)
            comboboxAccounts.grid(row = 2, column = 1)

            btn = ttk.Button(win, text ="Create Transaction", command = testbutton)
            btn.grid(row = 1, column = 1)
            isLoged = True
            break;
    if isLoged == False:
        messagebox.showerror("Error","Wrong username or/and password!")

def toggle_fullscreen(event=None):
    win.attributes("-fullscreen", True)

def end_fullscreen(event=None):
    win.attributes("-fullscreen", False)

def testbutton():
    accountUsed = comboboxAccounts.get()
    for x in userLoged.Accounts:
        if x.Title == accountUsed:
            ac = x
    asa = TransactionService(win, dbcursor, ac, mydb)
    asa.CreateTransaction()
    btn2 = ttk.Button(win, text ="show")
    btn2.grid(row = 2, column = 1)
    btn2.bind("<Button>", lambda e: funny(asa.transaction))

def funny(a):
    print(a.TimeFormat + " " + a.Title + " " + a.Amount + "$")

win.geometry("200x200+-1+0")
win.bind("<Tab>", toggle_fullscreen)
win.bind("<Escape>", end_fullscreen)
loginWin = LoginWindow(win, dbcursor, 5, mydb)
loginWin.LoginWindowGenerate()
""" loginFrame = Frame(win)
loginFrame.pack()

labelTitle = Label(loginFrame, text="Please enter login details")
labelTitle.pack()

labelSpace1 = Label(loginFrame, text="")
labelSpace1.pack()

labelUsername = Label(loginFrame, text="Username")
labelUsername.pack()

username_login_entry = Entry(loginFrame, textvariable="username")
username_login_entry.pack()

labelSpace2 = Label(loginFrame, text="")
labelSpace2.pack()

labelPassword = Label(loginFrame, text="Password")
labelPassword.pack()

password__login_entry = Entry(loginFrame, textvariable="password", show= '*')
password__login_entry.pack()

labelSpace3 = Label(loginFrame, text="")
labelSpace3.pack()

buttonLogin = Button(loginFrame, text="Login", width=10, height=1, command = LoginValidator)
buttonLogin.pack() """
Center()

# To do list:

# WYWAL LOGOWANIE/REJESTRACJE DO INNEGO PLIKU
# Ikony i nazwy okienek
# Wybrać paletę barw
# Dodawanie Kont
# Konto oszczędnościowe (SQL POŁĄCZENIE Z account) (Klasa) (Obsługa w programie)
# System akcji (Znajdź API) (Kup/Sprzedaj) (SQL POŁĄCZENIE Z account)
# System modyfikacji Transakcji, kont i innych obiektów
# Brzydki kod, popraw
# Nałożyć design, zastosować obiekty frame
# Napraw Połączenie z gitem

win.mainloop()
