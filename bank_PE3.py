import pickle
import random
from savingsaccount import SavingsAccount

class Bank:
    def __init__(self, fileName=None):
        self.accounts = {}
        self.fileName = fileName
        if fileName != None:
            with open(fileName, 'rb') as fileObj:
                while True:
                    try:
                        account = pickle.load(fileObj)
                        self.add(account)
                    except Exception:
                        break

    def __str__(self):
        sorted_accounts = sorted(self.accounts.values(), key=lambda account: account.getName())
        return "\n".join(map(str, sorted_accounts))

    def makeKey(self, name, pin):
        return name + "/" + pin

    def add(self, account):
        key = self.makeKey(account.getName(), account.getPin())
        self.accounts[key] = account

    def remove(self, name, pin):
        key = self.makeKey(name, pin)
        return self.accounts.pop(key, None)

    def get(self, name, pin):
        key = self.makeKey(name, pin)
        return self.accounts.get(key, None)

    def computeInterest(self):
        total = 0
        for account in self.accounts.values():
            total += account.computeInterest()
        return total

    def save(self, fileName=None):
        if fileName != None:
            self.fileName = fileName
        elif self.fileName == None:
            return
        with open(self.fileName, 'wb') as fileObj:
            for account in self.accounts.values():
                pickle.dump(account, fileObj)

def createBank(numAccounts=1):
    names = ("Venida", "Dela Cruz", "Labrador", "Taylar", "Noxus")
    bank = Bank()
    upperPin = numAccounts + 1000
    for pinNumber in range(1000, upperPin):
        name = random.choice(names)
        balance = float(random.randint(100, 1000))
        bank.add(SavingsAccount(name, str(pinNumber), balance))
    return bank

def testAccount():
    account = SavingsAccount("Ken", "1000", 500.00)
    print(account)
    print(account.deposit(100))
    print("Expect 600:", account.getBalance())
    print(account.deposit(-50))
    print("Expect 600:", account.getBalance())
    print(account.withdraw(100))
    print("Expect 500:", account.getBalance())
    print(account.withdraw(-50))
    print("Expect 500:", account.getBalance())
    print(account.withdraw(100000))
    print("Expect 500:", account.getBalance())

def main(number=10, fileName=None):
    testAccount()
    if fileName:
        bank = Bank(fileName)
    else:
        bank = createBank(number)
    print(bank)

if _name_ == "_main_":
    main()

def testBankOutput():
    print()
    print("Test for PE 3")
    bank = Bank()
    bank.add(SavingsAccount("Venida", "4967", 5000.00))
    bank.add(SavingsAccount("Dela Cruz", "3543", 3000.00))
    bank.add(SavingsAccount("Labrador", "1234", 7000.00))
    bank.add(SavingsAccount("Taylar", "7482", 10500.00))
    bank.add(SavingsAccount("Noxus", "0201", 2015.00))

    print(bank)

testBankOutput()
