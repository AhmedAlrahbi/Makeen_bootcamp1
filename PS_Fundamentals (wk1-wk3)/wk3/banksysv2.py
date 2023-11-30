#ICA
class BankAccount:
    def __init__(self, balance, accountNum):
        self.__balance = balance
        self.__accountNum = accountNum
    def deposit(self, deposit_amount):
        self.__balance +=deposit_amount
        BankAccount.display(self)
    def withdrawal(self,withdrawal_amount):
        if (withdrawal_amount < self.__balance):
            self.__balance -=withdrawal_amount
        else:
            print("You dont have that amount of money")
        BankAccount.display(self)
    def display(self):
        print(f"Your account ({self.__accountNum}) balance is {self.__balance}")
try1 = BankAccount(1000, 989)
#try1.deposit(500)
withdrawal = True
while(withdrawal):
    withdrawal = int(input("Enter the Amount to withdrawal: "))
    if (withdrawal < 0):
        try:
            Error = "Should be positive"
            raise Error

            #myError = ValueError('should be a positive number')
        except:
            print(Error)
            break
    else:
        try1.withdrawal(withdrawal)
        break



#try1.display()
