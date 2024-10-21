from datetime import datetime
from threading import Thread
from time import sleep


def write_words(word_count, file_name):
    with open(file_name, 'w+') as file:
        for counter in range(1, word_count):
            file.write(f"Какое-то слово №{counter}")
            sleep(0.1)
    print(f"Завершилась запись в файл {file_name}")


first_start_time = datetime.now()

write_words(10, "example1.txt")
write_words(30, "example2.txt")
write_words(200, "example3.txt")
write_words(100, "example4.txt")

first_end_time = datetime.now()
time_without_threads = first_end_time - first_start_time

second_start_time = datetime.now()

thread_first = Thread(target=write_words, args=(10, "example5.txt"))
thread_second = Thread(target=write_words, args=(30, "example6.txt"))
thread_third = Thread(target=write_words, args=(200, "example7.txt"))
thread_fourth = Thread(target=write_words, args=(100, "example8.txt"))

thread_first.start()
thread_second.start()
thread_third.start()
thread_fourth.start()

thread_first.join()
thread_second.join()
thread_third.join()
thread_fourth.join()


second_end_time = datetime.now()

print(f"witout Threads {first_end_time - first_start_time}")
print(f"with Threads {second_end_time - second_start_time}")
