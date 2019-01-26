class Account():

    def __init__(self, owner, balance):

        self.owner = owner
        self.balance = balance


    def deposit(self, amount):

        self.balance = self.balance+amount
        print ("deposit accepted")

    def withdraw(self, amount):

        if self.balance > amount :
            self.balance = self.balance-amount
            print ("withdraw accepted")
        else:
            print ("Funds Unavailable!")

    def __str__(self):
        return ("Owner of account is {} and current balance is {}".format(self.owner, self.balance))
    
