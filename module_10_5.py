import multiprocessing
import datetime
def read_info(name):
    all_data = []
    with open(name,'r',encoding='utf-8') as file:
        while file.readline():
            all_data.append(file.readline())

filenames = [f'./file {number}.txt' for number in range(1, 5)]

# Линейный вызов --> 0:00:03.063688 (линейный)
start1 = datetime.datetime.now()
for file in filenames:
    read_info(file)
end1 = datetime.datetime.now()
print(f'{end1 - start1} (линейный)')

# Многопроцессный --> 0:00:01.210287 (многопроцессный)
if __name__ == '__main__':
    start2 = datetime.datetime.now()
    with multiprocessing.Pool(processes = 4) as pool:
        pool.map(read_info,filenames)
    end2 = datetime.datetime.now()
    print(f'{end2 - start2} (многопроцессный)')