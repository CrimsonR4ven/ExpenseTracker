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

    def GetStocksList():
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