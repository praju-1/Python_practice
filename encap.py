class Bank:
    def __init__(self, name, acc_no, balance):
        self.name = name
        self.acc_no = acc_no
        self.__balance = balance

    def info(self):
        print("Name of account holder : ", self.name)
        print("Accout number is : ", self.acc_no)
        print("Account Balance is  : ", self.__balance)

    def deposite(self, amt):
        self.__balance += amt

    def withdrawl(self, amt):
        self.__balance -= amt

    def updated_balance(self):
        print("Updated balance is  : ", self.__balance)

b = Bank("John", 12345, 5000)
b.info()
b.deposite(2000)
b.updated_balance()
b.withdrawl(2000)
b.updated_balance()
