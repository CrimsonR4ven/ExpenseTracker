from tkinter import *

class Account:
    def __init__(self, title, money, desc, accountID, dbcursor, mydb):
        self.Title = title
        self.Money = money
        self.Desc = desc
        self.dbcursor = dbcursor
        self.AccountID = accountID
        self.mydb = mydb
        self.Type = "Normal"

    def UpdateAccount(self):
        self.dbcursor.execute("UPDATE account SET Money = %s WHERE (Title = '%s') AND (Description = '%s')" % (self.Money, self.Title, self.Desc))
        self.mydb.commit()

class StockAccount(Account):
    def __init__(self, title, money, desc, accountID, dbcursor, mydb):
        super().__init__(title, money, desc, accountID, dbcursor, mydb)
        self.StockDict = dict()
        self.Type = "Stock"

    def GetStocksDict():
        pass

    def GetStocksLine():
        pass

    def UpdateAccount(self):
        self.dbcursor.execute("UPDATE stockAccount SET Money = %s WHERE (Title = '%s') AND (Description = '%s')" % (self.Money, self.Title, self.Desc))
        self.mydb.commit()

class SavingsAccount(Account):
    def __init__(self, title, money, desc, accountID, goal, dbcursor, mydb):
        super().__init__(title, money, desc, accountID, dbcursor, mydb)
        self.Goal = goal
        self.Type = "Savings"

    def UpdateAccount(self):
        self.dbcursor.execute("UPDATE savingsAccount SET Money = %s, Goal = %s WHERE (Title = '%s') AND (Description = '%s')" % (self.Money, self.goal, self.Title, self.Desc))
        self.mydb.commit()

class PresentBoxAccount:

    ID = -1

    def __init__(self, root, account):
        PresentBoxAccount.ID = PresentBoxAccount.ID + 1
        self.ID = PresentBoxAccount.ID
        self.Account = account
        self.Frame = Frame(root, height=250, width=300, background="#b3b3b3")
        self.Frame.pack_propagate(0)
        self.AccountName = Label(self.Frame, text = self.Account.Title)
        if   self.Account.Type == "Normal":
            self.c = Canvas(self.Frame, width=154, height=154, background="#eeeeee",highlightthickness=0)
            self.c.create_arc((2,2,152,152), fill="#FAF402", outline="#FAF402", start=self.prop(0),   extent = self.prop(200))
            self.c.create_arc((2,2,152,152), fill="#2BFFF4", outline="#2BFFF4", start=self.prop(200), extent = self.prop(400))
            self.c.create_arc((2,2,152,152), fill="#E00022", outline="#E00022", start=self.prop(600), extent = self.prop(50) )
            self.c.create_arc((2,2,152,152), fill="#7A0871", outline="#7A0871", start=self.prop(650), extent = self.prop(200))
            self.c.create_arc((2,2,152,152), fill="#294994", outline="#294994", start=self.prop(850), extent = self.prop(150))
        elif self.Account.Type == "Stock":
            pass
        elif self.Account.Type == "Savings":
            pass
        self.AccountBalance = Label(self.Frame, text = f"Balance: {self.Account.Money} pln", background="#b3b3b3")
    def prop(self,n):
        return 360.0 * n / 1000
    def pack(self):

        self.Frame.place(x=60 * ((self.ID % 3) + 1) + 300 * (self.ID % 3), y=20 * (int(self.ID / 3) + 1) + 250 * int(self.ID / 3))
        self.AccountName.place(x=5, y=2)
        self.c.place(x=5, y=20)
        self.AccountBalance.place(x=5, y=180)
        pass

class AccountPresenter:
    def __init__(self):
        pass
    def AccountPresent(root, Account):
        pba = PresentBoxAccount(root, Account)
        return pba
