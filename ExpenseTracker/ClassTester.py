from tkinter import *
from tkinter import ttk
import Objects
from TransactionService import *
from PIL import ImageTk, Image

import time
import threading
import mysql.connector
import datetime

mydb = mysql.connector.connect(
  host="localhost",
  port="3307",
  user="root",
  password="",
  database="tracker"
)
dbcursor = mydb.cursor()

win = Tk()

photo = ImageTk.PhotoImage(Image.open('./Images/Raven.png'))
win.wm_iconphoto(True, photo)

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
""" def RegisterWindow():
    win.geometry("1200x600")
    Center()
    win.attributes("-fullscreen", True)

    label = ttk.Label(win, text="Da tracker", font=("Courier 22"))
    label.grid(row = 0, column = 0)

    label2 = ttk.Label(win, text="ye", font=("Courier 22"))
    label2.grid(row = 1, column = 0)
    global accountList
    accountList = []
    
    for x in .Accounts:
        accountList.append(x.Title)
    global comboboxAccounts
    comboboxAccounts = Combobox(win, values = accountList)
    comboboxAccounts.grid(row = 2, column = 1)

    btn = ttk.Button(win, text ="Create Transaction", command = testbutton)
    btn.grid(row = 1, column = 1)
    isLoged = True """

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

def catchLogInThread():
    while(not loginWin.IsLoged):
        time.sleep(0)
    global appVar
    appVar = Objects.AppWindow(win,dbcursor,Objects.User(loginWin.Login, loginWin.Passw, loginWin.UserID, dbcursor, mydb))
    appVar.GenerateMainWindow()

win.configure(background="#ffffff")
win.geometry("1300x750+-1+0")
win.resizable(0, 0)
win.bind("<Tab>", toggle_fullscreen)
win.bind("<Escape>", end_fullscreen)
x = threading.Thread(target=catchLogInThread)
loginWin = Objects.LoginWindow(win, dbcursor)
x.start()
loginWin.LoginWindowGenerate()

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