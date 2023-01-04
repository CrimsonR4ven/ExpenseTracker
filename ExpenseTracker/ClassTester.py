from tkinter import *
from tkinter import ttk
import Objects
from TransactionService import *
from PIL import ImageTk, Image

import time
import threading
import mysql.connector
import datetime

try:
    mydb = mysql.connector.connect(
    host="sql7.freesqldatabase.com",
    port="3306",
    user="sql7586811",
    password="caaxv2mJum",
    database="sql7586811"
    )
    dbcursor = mydb.cursor()
    NoConnection = False
except:
    dbcursor = False
    NoConnection = True


win = Tk()

photo = ImageTk.PhotoImage(Image.open('./ExpenseTracker/Images/Raven.png'))
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
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y - int(y/3)))
    win.deiconify()

#To tak na przyszłość, kiedyś się tego użyje
#po co? bo fajne

#def toggle_fullscreen(event=None):
#    win.attributes("-fullscreen", True)

#def end_fullscreen(event=None):
#    win.attributes("-fullscreen", False)

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
    appVar = Objects.AppWindow(win, dbcursor, mydb, Objects.User(loginWin.Login, loginWin.Passw, loginWin.UserID, dbcursor, mydb))
    appVar.GenerateMainWindow()
    Center()

win.configure(background="#ffffff")
win.geometry("1300x750+-1+0")
win.resizable(0, 0)
#win.bind("<Tab>", toggle_fullscreen)
#win.bind("<Escape>", end_fullscreen)
x = threading.Thread(target=catchLogInThread)
loginWin = Objects.LoginWindow(win, dbcursor, mydb, NoConnection)
x.start()
if NoConnection == True:
    loginWin.NoConnection()
else:
    loginWin.LoginWindowGenerate()
Center()
# To do list:

# WYWAL LOGOWANIE/REJESTRACJE DO INNEGO PLIKU - Done
# Wybrać paletę barw - Done
# Nałożyć design, zastosować obiekty frame - Done
# Ikony i nazwy okienek - Done

# Dodawanie Kont
# Konto Normalne
# Konto Stockowe
# Konto oszczędnościowe (SQL POŁĄCZENIE Z account) (Klasa) (Obsługa w programie)
# System akcji (Znajdź API) (Kup/Sprzedaj) (SQL POŁĄCZENIE Z account)
# System modyfikacji Transakcji, kont i innych obiektów

# Brzydki kod, popraw - impossible 

win.mainloop()