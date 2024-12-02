import datetime
import multiprocessing


def read_info(file_name):
    with open(file_name, 'r') as file:
        all_data = []
        data = file.readline()
        while data != "" and data is not None:
            all_data.append(data)
            data = file.readline()


file_names = [f'./file {number}.txt' for number in range(1, 5)]

#lin call
"""
start_time = datetime.datetime.now()
read_info(file_names[0])
read_info(file_names[1])
read_info(file_names[2])
read_info(file_names[3])
end_time = datetime.datetime.now()

dif_time = end_time - start_time
print(dif_time)
"""

#multiprocess calling
if __name__ == '__main__':
    start_time = datetime.datetime.now()
    with multiprocessing.Pool() as pool:
        pool.map(read_info, file_names)
    end_time = datetime.datetime.now()
    print(end_time - start_time)


"""
if __name__ == '__main__':
    start_time = datetime.datetime.now()
    process1 = multiprocessing.Process(target=read_info, args=("./file 1.txt",))
    process2 = multiprocessing.Process(target=read_info, args=("./file 2.txt",))
    process3 = multiprocessing.Process(target=read_info, args=("./file 3.txt",))
    process4 = multiprocessing.Process(target=read_info, args=("./file 4.txt",))

    process1.start()
    process2.start()
    process3.start()
    process4.start()

    end_time = datetime.datetime.now()
    dif_time = end_time - start_time
    print(dif_time)
"""

