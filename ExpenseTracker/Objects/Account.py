class Account:
    def __init__(self, title, money, desc, accountID, dbcursor, mydb):
        self.Title = title
        self.Money = money
        self.Desc = desc
        self.dbcursor = dbcursor
        self.AccountID = accountID
        self.mydb = mydb
    def UpdateAccount(self):
        self.dbcursor.execute("UPDATE account SET Money = %s WHERE (Title = '%s') AND (Description = '%s')" % (self.Money, self.Title, self.Desc))
        self.mydb.commit()
