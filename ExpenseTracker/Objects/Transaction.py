import datetime
class Transaction:
    def __init__(self, title, amount):
        self.Title = title
        self.Amount = amount
        self.Time = datetime.datetime.now()
        self.TimeFormat = self.Time.strftime("%Y-%m-%d %H:%M:%S")
