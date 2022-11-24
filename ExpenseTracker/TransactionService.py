from tkinter import *
from tkinter import ttk
from Objects.Transaction import *
from tkinter.ttk import Combobox
class TransactionService:
    def __init__(self, win, dbcursor, accountUsed, mydb, alter = None):
        if alter:
            pass
        else:
            self.mydb = mydb
            self.newWindow = Toplevel(win)
            self.account = accountUsed
            self.dbcursor = dbcursor

            self.label = ttk.Label(self.newWindow, text="Create Transaction", font=("Courier 22"))
            self.label.grid(row = 0, column = 1)

            self.label2 = ttk.Label(self.newWindow, text="Title", font=("Courier 16"))
            self.label2.grid(row = 1, column = 0)

            self.label3 = ttk.Label(self.newWindow, text="amount", font=("Courier 16"))
            self.label3.grid(row = 2, column = 0)

            self.EntryTitle = ttk.Entry(self.newWindow, width= 40)
            self.EntryTitle.grid(row = 1, column = 1)

            self.EntryAmount = ttk.Entry(self.newWindow, width= 40)
            self.EntryAmount.grid(row = 2, column = 1)

            self.data = ("Payment", "Profit")
            self.cb=Combobox(self.newWindow, values = self.data)

            self.btn = ttk.Button(self.newWindow, text = "Create")
            self.btn.grid(row = 3, column = 2)
            self.btn.bind("<Button>", lambda e: self.CreateTransaction())

            self.isPayment = True
    def CreateTransaction(self):
        from tkinter import messagebox

        amount = int(self.EntryAmount.get())
        title = self.EntryTitle.get();

        if title == "":
            messagebox.showerror("Error","Title cannot be empty!")
        elif amount <= 0:
            messagebox.showerror("Error","Amount cannot be lower than 1$")
        else:
            self.transaction = Transaction(title, amount)
            self.__FinalizeTransaction()
            self.__AddDBTransaction()
            self.newWindow.destroy()
            self.newWindow.update()

    def __FinalizeTransaction(self):
        if self.isPayment == True:
            self.account.Money = self.account.Money - self.transaction.Amount
            self.account.UpdateAccount()
        else:
            self.account.Money = self.account.Money + self.transaction.Amount
            self.account.UpdateAccount()

    def __AddDBTransaction(self):
        self.dbcursor.execute("INSERT INTO transaction (Title, Amount, DateOfTransaction, AccountID) VALUES ('%s', '%s', '%s', '%s')" % (self.transaction.Title, self.transaction.Amount, self.transaction.TimeFormat, self.account.AccountID))
        self.mydb.commit()
