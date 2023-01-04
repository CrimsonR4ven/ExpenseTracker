from Objects.Account import *
class User:
    def __init__(self, login, passw, userID, dbcursor, mydb):
        self.Login    = login
        self.Passw    = passw
        self.UserID   = userID
        self.DBcursor = dbcursor
        self.Accounts = []
        self.mydb = mydb
        self.ListAccounts()
    def ListAccounts(self):
        self.DBcursor.execute('SELECT Title, Money, Description, AccountID, Type FROM account INNER JOIN user ON account.UserID = user.UserID WHERE user.UserID = \'%s\';' % (self.UserID))
        dbresult = self.DBcursor.fetchall()
        for x in dbresult:
            newAccount = Account(x[0], x[1], x[2], x[3], self.DBcursor, self.mydb)
            self.Accounts.append(newAccount)
    def UpdateAccounts(self):
        self.Accounts.clear()
        self.DBcursor.execute('SELECT Title, Money, Description, AccountID, Type, Goal, StocksLine FROM account INNER JOIN user ON account.UserID = user.UserID WHERE user.UserID = \'%s\';' % (self.UserID))
        dbresult = self.DBcursor.fetchall()
        for x in dbresult:
            if x[4] == 1:
                newAccount = Account(x[0], x[1], x[2], x[3], self.DBcursor, self.mydb)
            elif x[4] == 2:
                newAccount = SavingsAccount(x[0], x[1], x[2], x[3], x[5], self.DBcursor, self.mydb)
            elif x[4] == 3:
                newAccount = StockAccount(x[0], x[1], x[2], x[3], self.DBcursor, self.mydb, x[6])
            self.Accounts.append(newAccount)
