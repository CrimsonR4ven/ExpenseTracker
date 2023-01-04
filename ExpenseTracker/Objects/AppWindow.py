from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox
import Objects
class AppWindow:
    def __init__(self, win, dbcursor, mydb, accountUsed):
        #Variables - Args
        self.win      = win
        self.dbcursor = dbcursor
        self.mydb     = mydb
        self.user     = accountUsed

        #Variables - Creating Account
        self.NewAccountType = 1

        #Main Window - Main Frames
        self.mainMenuBarFrame   = Frame(win, background="#ff2b05", width=1500, height=50)
        self.mainSideBar        = Frame(win, background="#cccccc", width=350,  height=850)
        self.mainScreenFrame    = Frame(win, background="#eeeeee", width=1150, height=850)

        self.mainMenuBarFrame.pack_propagate(0)
        self.mainSideBar.pack_propagate(0)
        self.mainScreenFrame.pack_propagate(0)

        #Main Window - Containers
        self.mainScreenCanvas          = Canvas(self.mainScreenFrame, width=1150, height=850, background="#eeeeee", highlightthickness=0)
        self.mainScreenScrollableFrame = Frame(self.mainScreenCanvas, width=1150, height=850, background="#eeeeee")

        #Main Window - Scrollbars
        self.mainScreenScrollbar = ttk.Scrollbar(self.mainScreenFrame, orient="vertical", command=self.mainScreenCanvas.yview)


        #Main Window - Configuration
        self.mainScreenScrollableFrame.bind(
            "<Configure>",
            lambda e: self.mainScreenCanvas.configure(scrollregion = self.mainScreenCanvas.bbox("all"))   
        )
        self.mainScreenCanvas.configure(yscrollcommand=self.mainScreenScrollbar.set)

        #Main Window - Account Presenter
        self.AP = Objects.AccountPresenter
        self.APlist = []
        self.FrameCreate = Frame(self.mainScreenScrollableFrame, height=250, width=300, background="#b3b3b3")
        self.FrameCreate.pack_propagate(0)
        self.AccountName = Label(self.FrameCreate, text = "Create new account", background="#b3b3b3")
        self.FrameCreate.bind("<Button-1>",lambda event: self.GenerateCreateAccountWindow(event))

        #Creating Account - Containers
        self.CreateAccountScrollableFrame = Frame(self.mainScreenCanvas, width=1150, height=850, background="#eeeeee")

        #Creating Account - Form
        self.BoxAccountTypeNormal  = Frame( self.CreateAccountScrollableFrame, width=300, height=50, background="#b3b3b3")
        self.BoxAccountTypeSavings = Frame( self.CreateAccountScrollableFrame, width=300, height=50, background="#b3b3b3")
        self.BoxAccountTypeStocks  = Frame( self.CreateAccountScrollableFrame, width=300, height=50, background="#b3b3b3")
        self.TypeLabelNormal       = Label( self.BoxAccountTypeNormal,         text = "Normal",      font = ('Colibri',13),background="#ff2b05")
        self.TypeLabelSavings      = Label( self.BoxAccountTypeSavings,        text = "Savings",     font = ('Colibri',13),background="#b3b3b3")
        self.TypeLabelStocks       = Label( self.BoxAccountTypeStocks,         text = "Stocks",      font = ('Colibri',13),background="#b3b3b3")
        self.EntryLabelTitle       = Label( self.CreateAccountScrollableFrame, text = "Title",       font = ('Colibri',13),background="#eeeeee")
        self.EntryLabelDescription = Label( self.CreateAccountScrollableFrame, text = "Description", font = ('Colibri',13),background="#eeeeee")
        self.EntryLabelGoal        = Label( self.CreateAccountScrollableFrame, text = "Goal",        font = ('Colibri',13),background="#eeeeee")
        self.TitleEntry            = Entry( self.CreateAccountScrollableFrame, highlightthickness=1, relief=FLAT, textvariable="Account title",       background="#3b3b3b", foreground="#ffffff")
        self.DescriptionEntry      = Entry( self.CreateAccountScrollableFrame, highlightthickness=1, relief=FLAT, textvariable="Account description", background="#3b3b3b", foreground="#ffffff")
        self.GoalEntry             = Entry( self.CreateAccountScrollableFrame, highlightthickness=1, relief=FLAT, textvariable="Account goal",        background="#3b3b3b", foreground="#ffffff")
        self.CancelButtonCreation  = Button(self.CreateAccountScrollableFrame, text="cancel",        width=10,    height=1, background="#3b3b3b",     foreground="#ffffff", command = lambda: self.BackToMainWindow(self.CreateAccountWindow))
        self.CreateButtonCreation  = Button(self.CreateAccountScrollableFrame, text="create",        width=10,    height=1, background="#3b3b3b",     foreground="#ffffff", command = self.CreateAccount)

        #Creating Account - Configuration
        self.BoxAccountTypeNormal.pack_propagate(0)
        self.BoxAccountTypeSavings.pack_propagate(0)
        self.BoxAccountTypeStocks.pack_propagate(0)
        self.BoxAccountTypeNormal.bind( "<Button-1>",self.SetTypeNormal)
        self.BoxAccountTypeSavings.bind("<Button-1>",self.SetTypeSavings)
        self.BoxAccountTypeStocks.bind( "<Button-1>",self.SetTypeStocks)

        #Account Menu - Containers
        self.AccountMenuScrollableFrame = Frame(self.mainScreenCanvas, width=1150, height=850, background="#eeeeee")

        #Account Menu - Menu
        self.TitleAccount          = Label( self.AccountMenuScrollableFrame,background="#3b3b3b", foreground="#ffffff", font=('Colibri', 13))
        self.DescAccount           = Label( self.AccountMenuScrollableFrame,background="#3b3b3b", foreground="#ffffff", font=('Colibri', 13))
        self.BalanceAccount        = Label( self.AccountMenuScrollableFrame,background="#3b3b3b", foreground="#ffffff", font=('Colibri', 13))
        self.HistoryButtonAccount  = Button(self.AccountMenuScrollableFrame, text="History",         width=10,    height=1,                background="#3b3b3b", foreground="#ffffff", command = self.BackToMainWindow)
        self.NewTransactionButton  = Button(self.AccountMenuScrollableFrame, text="New Transaction",         width=10,    height=1,                background="#3b3b3b", foreground="#ffffff", command = self.CreateAccount)
        self.DeleteButtonAccount   = Button(self.AccountMenuScrollableFrame, text="Delete Account",         width=10,    height=1,                background="#3b3b3b", foreground="#ffffff", command = self.AccountDelete)
        
    def prop(self,n):
        return 360.0 * n / 1000
    def getAccounts(self):
        self.APlist.clear()
        x = 0
        print(self.user.Accounts)
        for account in self.user.Accounts:
            self.APlist.append(self.AP.AccountPresent(self.mainScreenScrollableFrame, account))
            id = self.APlist[x].ID
            self.APlist[id].Frame.bind("<Button-1>",lambda event, ac=self.APlist[id].Account: self.AccountWindow(event,ac))
            x = x + 1
    def GenerateMainWindow(self):
        self.mainScreenWindow = self.mainScreenCanvas.create_window((0, 0), window=self.mainScreenScrollableFrame, anchor="nw")
        self.getAccounts()
        self.win.geometry("1500x900+-1+0")
        self.mainMenuBarFrame.pack()
        self.mainSideBar.pack(side=LEFT)
        self.mainScreenFrame.pack(side=LEFT)
        self.mainScreenScrollbar.pack(side=RIGHT, fill = Y)
        self.mainScreenCanvas.pack(expand=True)
        for ob in self.APlist:
            ob.pack()
        self.FrameCreate.place(x = 60 * (((self.APlist[len(self.APlist)-1].ID + 1) % 3)+1) + 300 * ((self.APlist[len(self.APlist)-1].ID + 1) % 3), y=20 * (int((self.APlist[len(self.APlist)-1].ID + 1)/ 3)+1) + 250 * int((self.APlist[len(self.APlist)-1].ID + 1)/ 3))
        self.AccountName.pack(pady=100)

    def BackToMainWindow(self,From):
        self.mainScreenCanvas.delete(From)
        self.mainScreenWindow = self.mainScreenCanvas.create_window((0, 0), window=self.mainScreenScrollableFrame, anchor="nw")

        for ob in self.APlist:
            ob.pack_forget()
        self.FrameCreate.place_forget()
        self.AccountName.pack_forget()
        Objects.PresentBoxAccount.ID = -1

        self.user.UpdateAccounts()
        self.getAccounts()
        for ob in self.APlist:
            ob.pack()
        self.FrameCreate.place(x = 60 * (((self.APlist[len(self.APlist)-1].ID + 1) % 3)+1) + 300 * ((self.APlist[len(self.APlist)-1].ID + 1) % 3), y=20 * (int((self.APlist[len(self.APlist)-1].ID +1)/ 3)+1) + 250 * int((self.APlist[len(self.APlist)-1].ID + 1)/ 3))
        self.AccountName.pack(pady=100)

    def GenerateCreateAccountWindow(self,event):
        self.NewAccountType = 1
        self.mainScreenCanvas.delete(self.mainScreenWindow)
        self.CreateAccountWindow = self.mainScreenCanvas.create_window((0, 0), window=self.CreateAccountScrollableFrame, anchor="nw")
        self.BoxAccountTypeNormal.place(x = 62, y = 20)
        self.BoxAccountTypeNormal.config(background="#ff2b05")
        self.BoxAccountTypeSavings.place(x = 424, y = 20)
        self.BoxAccountTypeSavings.config(background="#b3b3b3")
        self.BoxAccountTypeStocks.place(x = 786, y = 20)
        self.BoxAccountTypeStocks.config(background="#b3b3b3")
        self.TypeLabelNormal.pack()
        self.TypeLabelSavings.pack()
        self.TypeLabelStocks.pack()
        self.TypeLabelNormal.config(background="#ff2b05")
        self.TypeLabelSavings.config(background="#b3b3b3")
        self.TypeLabelStocks.config(background="#b3b3b3")
        self.EntryLabelTitle.place(x = 350,y = 100)
        self.EntryLabelDescription.place(x = 350,y = 130)
        self.TitleEntry.place(x = 500,y = 100)
        self.DescriptionEntry.place(x = 500,y = 130)
        self.CancelButtonCreation.place(x = 520,y = 160)
        self.CreateButtonCreation.place(x = 520,y = 190)

    def SetTypeNormal(self, event):
        self.BoxAccountTypeNormal.config(background="#ff2b05")
        self.BoxAccountTypeSavings.config(background="#b3b3b3")
        self.BoxAccountTypeStocks.config(background="#b3b3b3")
        self.TypeLabelNormal.config(background="#ff2b05")
        self.TypeLabelSavings.config(background="#b3b3b3")
        self.TypeLabelStocks.config(background="#b3b3b3")
        if self.NewAccountType == 2:
            self.GoalEntry.place_forget()
            self.EntryLabelGoal.place_forget()
            self.CancelButtonCreation.place(x = 520,y = 160)
            self.CreateButtonCreation.place(x = 520,y = 190)

        self.NewAccountType = 1
    def SetTypeSavings(self, event):
        self.BoxAccountTypeNormal.config(background="#b3b3b3")
        self.BoxAccountTypeSavings.config(background="#ff2b05")
        self.BoxAccountTypeStocks.config(background="#b3b3b3")
        self.TypeLabelNormal.config(background="#b3b3b3")
        self.TypeLabelSavings.config(background="#ff2b05")
        self.TypeLabelStocks.config(background="#b3b3b3")
        if self.NewAccountType != 2:
            self.GoalEntry.place(x=500, y=160)
            self.EntryLabelGoal.place(x = 350,y = 160)
            self.CancelButtonCreation.place(x = 520,y = 190)
            self.CreateButtonCreation.place(x = 520,y = 220)
        self.NewAccountType = 2

    def SetTypeStocks(self, event):
        self.BoxAccountTypeNormal.config(background="#b3b3b3")
        self.BoxAccountTypeSavings.config(background="#b3b3b3")
        self.BoxAccountTypeStocks.config(background="#ff2b05")
        self.TypeLabelNormal.config(background="#b3b3b3")
        self.TypeLabelSavings.config(background="#b3b3b3")
        self.TypeLabelStocks.config(background="#ff2b05")
        if self.NewAccountType == 2:
            self.GoalEntry.place_forget()
            self.EntryLabelGoal.place_forget()
            self.CancelButtonCreation.place(x = 520,y = 160)
            self.CreateButtonCreation.place(x = 520,y = 190)
        self.NewAccountType = 3

    def CreateAccount(self):
        from tkinter import messagebox
        self.dbcursor.execute("SELECT Title FROM account WHERE Title = '%s'" % (self.TitleEntry.get()))
        if len(self.dbcursor.fetchall()) != 0:
            messagebox.showerror("Error","Account with that title already exists!")
        else:
            if self.NewAccountType == 1:
                self.dbcursor.execute("INSERT INTO `account` (`AccountID`, `Title`, `Money`, `Description`, `Type`, `Goal`, `StocksLine`, `UserID`) VALUES (NULL, '%s', '0', '%s', '%s', 'null','null','%s')" % (self.TitleEntry.get(),self.DescriptionEntry.get(),self.NewAccountType, self.user.UserID))
            elif self.NewAccountType == 2:
                self.dbcursor.execute("INSERT INTO `account` (`AccountID`, `Title`, `Money`, `Description`, `Type`, `Goal`, `StocksLine`, `UserID`) VALUES (NULL, '%s', '0', '%s', '%s', '%s','null','%s')" % (self.TitleEntry.get(),self.DescriptionEntry.get(),self.NewAccountType, self.GoalEntry.get(), self.user.UserID))
            elif self.NewAccountType == 3:
                self.dbcursor.execute("INSERT INTO `account` (`AccountID`, `Title`, `Money`, `Description`, `Type`, `Goal`, `StocksLine`, `UserID`) VALUES (NULL, '%s', '0', '%s', '%s', 'null','%s','%s')" % (self.TitleEntry.get(),self.DescriptionEntry.get(),self.NewAccountType,"{\"stock\": \"yes\"}", self.user.UserID))
            self.mydb.commit()
            self.BackToMainWindow(self.CreateAccountWindow)

    def AccountWindow(self,event,account):
        self.mainScreenCanvas.delete(self.mainScreenWindow)
        self.AccountMenuWindow = self.mainScreenCanvas.create_window((0, 0), window=self.AccountMenuScrollableFrame, anchor="nw")
        self.NewTransactionButton.config(command= lambda a=account:self.AccountNewTransaction(a))
        self.NewTransactionButton.pack() 
        self.HistoryButtonAccount.config(command= lambda a=account:self.AccountHistory(a))
        self.HistoryButtonAccount.pack()
        self.DeleteButtonAccount.config(command= lambda a=account:self.AccountDeleteTopLevel(a))
        self.DeleteButtonAccount.pack()
        print("funny ah " + account.Title)
        pass

    def AccountHistory(self,account):
        self.TopLevelHistory = Toplevel(self.win)

    def AccountNewTransaction(self,account):
        self.TopLevelNewTransaction     = Toplevel(self.win)
        self.BoxTransactionTypeInternal = Frame( self.CreateAccountScrollableFrame, width=300, height=50, background="#b3b3b3")
        self.BoxTransactionTypeExternal = Frame( self.CreateAccountScrollableFrame, width=300, height=50, background="#b3b3b3")
        self.TitleTransactionEntry      = Entry( self.CreateAccountScrollableFrame, highlightthickness=1,  relief=FLAT, textvariable="Transaction Title", background="#3b3b3b", foreground="#ffffff")
        self.AmountTransactionEntry     = Entry( self.CreateAccountScrollableFrame, highlightthickness=1,  relief=FLAT, textvariable="Transaction Amount", background="#3b3b3b", foreground="#ffffff")
        self.GoalEntry             = Entry( self.CreateAccountScrollableFrame, highlightthickness=1,  relief=FLAT, textvariable="Account goal", background="#3b3b3b", foreground="#ffffff")
        self.CancelButtonCreation  = Button(self.CreateAccountScrollableFrame, text="cancel",         width=10,    height=1,                background="#3b3b3b", foreground="#ffffff", command = lambda: self.BackToMainWindow(self.CreateAccountWindow))
        self.CreateButtonCreation  = Button(self.CreateAccountScrollableFrame, text="create",         width=10,    height=1,                background="#3b3b3b", foreground="#ffffff", command = self.CreateAccount)

        

    def AccountDeleteTopLevel(self,account):
        self.TopLevelDelete = Toplevel(self.win)
        self.TopLevelLabel = Label(self.TopLevelDelete, text=f"Do you really want to delete '{account.Title}' account?",background="#3b3b3b", foreground="#ffffff", font=('Colibri', 13))
        self.TopLevelButton1 = Button(self.TopLevelDelete, text="Not really",        width=15, height=2, background="#3b3b3b", foreground="#ffffff", command = self.AccountNotDelete)
        self.TopLevelButton2 = Button(self.TopLevelDelete, text="YES, MAKE IT BURN", width=15, height=2, background="#3b3b3b", foreground="#ffffff", command = lambda: self.AccountDelete(account))
        self.TopLevelLabel.pack()
        self.TopLevelButton1.pack()
        self.TopLevelButton2.pack()

    def AccountNotDelete(self): 
        self.TopLevelDelete.destroy()
        self.TopLevelDelete.update()

    def AccountDelete(self,account):
        self.dbcursor.execute("DELETE FROM `account` WHERE Title = '%s' AND AccountID = '%s'" % (account.Title, account.AccountID))
        self.mydb.commit()
        self.TopLevelDelete.destroy()
        self.TopLevelDelete.update()
        self.BackToMainWindow(self.AccountMenuWindow)

    def __FinalizeTransaction(self, account):
        from tkinter import messagebox
        if not all(char.isdigit() for char in self.AmountTransactionEntry.get()):
            messagebox.showerror("Error", "Amount needs to be a number!")
        else:
            self.transaction = Objects.Transaction(self.TitleTransactionEntry.get(), self.AmountTransactionEntry.get())
            if self.isPayment == True:
                self.account.Money = self.account.Money - self.transaction.Amount
                self.account.UpdateAccount()
            else:
                self.account.Money = self.account.Money + self.transaction.Amount
                self.account.UpdateAccount()
            self.dbcursor.execute("INSERT INTO transaction (Title, Amount, DateOfTransaction, AccountID) VALUES ('%s', '%s', '%s', '%s')" % (self.transaction.Title, self.transaction.Amount, self.transaction.TimeFormat, self.account.AccountID))
            self.mydb.commit()