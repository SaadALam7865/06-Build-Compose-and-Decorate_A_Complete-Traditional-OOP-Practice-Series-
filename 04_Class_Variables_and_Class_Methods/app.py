# 4. Class Variables and Class Methods
# Assignment:
# Create a class Bank with a class variable bank_name. Add a class method change_bank_name(cls, name) that allows changing the bank name. Show that it affects all instances.

class Bank:
    bank_name = 'Abc Bank' # Class variable

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

account1 = Bank()
account2 = Bank()
account3 = Bank()

print(f'Account 1 bank name: {account1.bank_name}')
print(f'Account 2 bank name: {account2.bank_name}')
print('Changing bank name...')
Bank.change_bank_name('Meezan Bank')
print(f'Account 1 bank name: {account1.bank_name}')
print(f'Account 2 bank name: {account2.bank_name}')





