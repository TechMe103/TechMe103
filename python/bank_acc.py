class Account:
    def __init__(self , bal , acc):
        self.balance=bal
        self.acc_no=acc
    def debit(self , amount):
        self.balance-=amount
        print("Rs, " , "amount was debited" )
        print("Total bal=" , self.get_balance())
    def credit(self , amount):
        self.balance+=amount
        print("Rs," "Amount was credited" )
        print("Total bal=" , self.get_balance())
    def get_balance(self):
        return self.balance
    
acc1=Account(1000 , 57687)
acc1.debit(1000)
acc1.credit(500)
print(acc1.balance)
print(acc1.acc_no) 