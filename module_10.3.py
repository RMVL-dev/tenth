from threading import Thread
import time
from threading import Lock
import random


class Bank:

    balance = 0
    lock = Lock()

    def deposit(self):
        for i in range(100):
            deposite = random.randint(50, 500)
            self.balance += deposite
            print(f"Пополнение: {deposite}. Баланс: {self.balance}")
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            time.sleep(0.001)

    def take(self):
        for i in range(100):
            taken_money = random.randint(50, 500)
            print(f"Запрос на {taken_money}")

            if taken_money <= self.balance:
                self.balance -= taken_money
                print(f"Снятие: {taken_money}. Баланс: {self.balance}")
            else:
                print(f"Запрос отклонён, недостаточно средств" )
                self.lock.acquire()
            time.sleep(0.001)


bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')


