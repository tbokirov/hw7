class Bank:
    def __init__(self, money, name):
        self.__money = money
        self.__name = name
    def setmoney(self, money):
        self.__money = money
    def getmoney(self):
        return self.__money
    def setname(self, name):
        self.__name = name
    def getname(self):
        return self.__name
    def moneyX(self):
        user = input('Введите сумму:')
        return f'Сумма введена корректно.\nВаш счет:{self.getmoney() + int(user)}'
    def _kill(self):
        return f'Счёт успешно обнулен \nВаш счет:{self.getmoney() - self.getmoney()}'
    def __jackpot(self):
        return f'Ваш лицевой счёт увилечен в 10 раз! \nВаш счет:{self.__money * 10}'

bruh = Bank(0, 'Optima')
bruh.setname('Capital')
bruh.setmoney(890)
print(f'Имя клиента:{bruh.getname()} \nСчёт клиента:{bruh.getmoney()}')
print(bruh.moneyX())
print(bruh._kill())
print(bruh._Bank__jackpot())