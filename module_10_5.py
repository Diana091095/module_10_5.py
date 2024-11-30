import datetime
import multiprocessing


def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as file:
        line = file.readline().strip()
        while line:
            all_data.append(line)
            line = file.readline().strip()
    file.close()


files = [f'./file {i}.txt' for i in range(1, 5)]

if __name__ == '__main__':

    start = datetime.datetime.now()
    for file in files:
        read_info(file)
    finish = datetime.datetime.now()
    res = finish - start
    print(f'{res} (линейный)')

    with multiprocessing.Pool(multiprocessing.cpu_count()) as Pool:
        start1 = datetime.datetime.now()
        Pool.map(read_info, files)
        Pool.close()
        Pool.join()
    finish1 = datetime.datetime.now()
    res1 = finish1 - start1
    print(f'{res1} (многопроцессный)')
