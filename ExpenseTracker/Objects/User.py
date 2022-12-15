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
        self.DBcursor.execute('SELECT Title, Money, Description, AccountID FROM account INNER JOIN user ON account.UserID = user.UserID WHERE user.UserID = \'%s\';' % (self.UserID))
        dbresult = self.DBcursor.fetchall()
        for x in dbresult:
            newAccount = Account(x[0], x[1], x[2], x[3], self.DBcursor, self.mydb)
            self.Accounts.append(newAccount)
