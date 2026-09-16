'''
CLASS deep diving:
    1. ENCAPSULATION
    2. INHERITANCE
    3. POLIMORPHISM
'''
print("_____ENCAPSULATION_____")
'''
C++, JAVA > public, private, protected
PHP Typescript > public, private, protected
Python > public, __private, _protected
'''


class Account():
    # state
    description = "The class makes bank accounts"
    # constructor

    def __init__(self, owner, amount):
        self.__owner = owner
        self.__amount = amount

    # method
    def get_balance(self):
        print(f"The owner {self.__owner} has {self.__amount} usd")

    def deposit(self, amount):
        print("* Deposit:", amount)
        self.__amount += amount

    def withdraw(self, amount):
        print("* Withdraw:", amount)
        self.__amount -= amount

    @property
    def holder(self):
        return self.__owner
    # Bu holat getter deb ataladi chunki ma'lumotlarni olganligimiz uchun

    @holder.setter
    def holder(self, new_owner):
        print("Holder.setter:", new_owner)
        self.__owner = new_owner

    def change_ownership(self, new_owner):
        print("Change ownership executed")
        self.__owner = new_owner


my_account = Account("Joseph", 1000)
my_account.get_balance()

print("_____")
# my_account.deposit(3500)
# my_account.withdraw(400)
# my_account.get_balance()

# my_account.amount = 1000000
# my_account.owner = "Martin"
# my_account.get_balance()

try:
    result = my_account.__amount
    print("Result", result)
except Exception as err:
    print("No target state found")

account_owner = my_account.holder
print("Account owner", account_owner)

# my_account.change_ownership("Martin")
my_account.holder = "Martin"
