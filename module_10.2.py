import threading
import time
from threading import Thread


class Knight(Thread):

    def __init__(self, name, power):
        Thread.__init__(self)
        self.name = name
        self.power = power
        self.days = 0

    def run(self):
        print(f"{self.name}, на нас напали!")
        enemies = 100
        while enemies > 0:
            enemies -= self.power
            time.sleep(1)
            self.days += 1
            print(f"{self.name} сражается {self.days}..., осталось {enemies} воинов.")
        if self.days > 4:
            print(f"{self.name} одержал победу спустя {self.days} дней!")
        else:
            print(f"{self.name} одержал победу спустя {self.days} дня!")


# Создание класса
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
# Запуск потоков и остановка текущего
second_knight.start()
first_knight.start()
# Вывод строки об окончании сражения
second_knight.join()
first_knight.join()
