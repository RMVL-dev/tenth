import random
import time
from threading import Thread
from queue import Queue


class Table:

    def __init__(self, number, guest=None):
        self.number = number
        self.guest = guest


class Guest(Thread):

    def __init__(self, name):
        Thread.__init__(self)
        self.name = name

    def run(self):
        wait_time = random.randint(3, 10)
        time.sleep(wait_time)


class Cafe:

    def __init__(self, *tables):
        self.queue = Queue()
        self.tables = tables

    def guest_arrival(self, *guests):
        for guest in guests:
            table = next((item for item in self.tables if item.guest is None), None)
            if table is not None:
                table.guest = guest
                guest.start()
                print(f"{guest.name} сел(-а) за стол номер {table.number}")
            else:
                self.queue.put(guest)
                print(f"{guest.name} в очереди")

    def discuss_guests(self):
        while not self.queue.empty() or next((item for item in self.tables if item.guest is not None),
                                             None) is not None:
            table = next((item for item in self.tables if item.guest is not None), None)
            if table is not None:
                if not table.guest.is_alive():
                    print(f"{table.guest.name} покушал(-а) и ушёл(ушла)")
                    print(f"Стол номер {table.number} свободен")
                    table.guest = None
                    if not self.queue.empty():
                        guest = self.queue.get()
                        table.guest = guest
                        print(f"{guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}")
                        table.guest.start()


# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()
