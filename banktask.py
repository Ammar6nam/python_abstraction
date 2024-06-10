from abc import ABC, abstractmethod

class bankAccount (ABC): #parent class
    def __init__(self,name,balance,accountNum) -> None:
        self.accountNumber=accountNum
        self.balance=balance
        self.accountHolderName=name

    @abstractmethod
    def deposit(self,amount):
        self.balance+=amount
        print(f'new balance is {self.balance}')

    @abstractmethod
    def withdraw(self,amount):
        if amount<self.balance:
            self.balance-=amount
            print(f'your {self.__class__.__name__} now contains {self.balance}')
            return amount
        else:
            return 'There are not enough funds in your account to withdraw this amount'

    @abstractmethod
    def accountType (self):
        pass

class savingAccount(bankAccount): #child class
    def __init__(self, name, balance, accountNum,interestRate) -> None:
        super().__init__(name, balance, accountNum)
        self.interestRate=interestRate

    def deposit(self,amount):
        interest=self.addInterest(amount)
        print(f'\n you are depositing {amount}.\n your added interest is {interest}\n')
        return super().deposit(amount+interest)

    def withdraw(self,amount):
        pass # super().withdraw(800)

    def accountType (self):
        pass

    def addInterest(self):
        pass

class checkingAccount(bankAccount):
    def deposit(self, amount) -> None:
        super().deposit(amount)
  
    def withdraw(self,amount):
        pass

    def accountType (self):
        pass
    def addInterest(self):
        pass

class businessAccount(bankAccount):
    def __init__(self, name, balance, accountNum,interestRate) -> None:
        super().__init__(name, balance, accountNum)
        self.interestRate=interestRate

    def deposit(self,amount):
        pass

    def withdraw(self,amount):
        pass

    def accountType (self):
        return 'Business Account'
    
    def addInterest(self):
        pass


    

mySaving=savingAccount('Ammar',500,12345,8)
#mySaving2=bankAccount('Nammour',400,12345)
# print(mySaving.balance)

mycheckingAccount=checkingAccount('Nammour',400,244)
# print(mycheckingAccount.balance)

# mybusinessAccount=businessAccount('Ammar2',420,554,9)
# print(mybusinessAccount.accountType())

# print(mySaving.accountHolderName)
# print(mySaving.accountType)
# print(f'Balance: {mySaving.balance}$')
# print(f'Interest Rate: {mySaving.interestRate} %')


while True:
    print('1) view balance')
    print('2)deposit money')
    print('3) withdraw money')
    print('4 Return Card')

    choice=int(input('Please select your option (1-4): '))

    match choice:
        case 1:
            print(f'View balance {mySaving.balance}')
        case 2:
            amount=float(input('How much would you like to withdraw? '))
            print(f'View deposit {mySaving.deposit(amount)} ')
        case 3:
            amount=float(input('How much would you like to withdraw? '))
            print(f'View withdraw {mySaving.withdraw(amount)}')
        case 4:
            print('View End')
            break
        case _:
            print('Please select a number between 1-4: ')