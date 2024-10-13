class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_houlder = account_holder
        self.balance = balance
        self.is_active = True

# para realizar un deposito
    def deposit(self, amount):
        if self.is_active:
            self.balance += amount
            print(f"Se ha depositado {amount}, saldo Actual {self.balance}")
        else:
            print("No se puede depositar, Cuenta inactiva")
# 
    def withdraw(self, amount):
        if self.is_active:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Se ha retirado {amount}, Saldo actual {self.balance}")

    def desactivate_account(self):
        self.is_active = False
        print("La cuenta ha sido desactivada")
    
    def activate_account(self):
        self.is_active = True
        print("La cuenta ha sido activada")
#objetos
account1 = BankAccount("Vivi", 500)
account2 = BankAccount("Marcela", 1000)

#Llamada a los metodos 
account1.deposit(200)
account2.deposit(100)
account1.desactivate_account()
account1.deposit(50)
account1.activate_account()
account1.deposit(50)