import os
import time

import LinkedList
import ArrayList

import concurrent.futures as multiproc


def create_random_values(rlength=100):
    import random
    values = []
    for i in range(rlength):
        values.append(random.randint(0, 10000)) #nrs range
    return values


def main():
    llist = LinkedList.LinkedList()
    alist = ArrayList.ArrayList()
    val = create_random_values()
    llist.adding_random(val)
    alist.adding_elem(val)
    print("Linked-List: ")
    llist.output()
    print("Array-List: ")
    alist.output()
    print("Menu Linked-List: ")
    llist.menu()
    print("Menu Array-List: ")
    alist.menu()


def rubneroutput(time, text, olist):
    print(" ")
    print(text + str(time))
    olist.output()


def maintest(unn=1):
    messungen = {}
    llist = LinkedList.LinkedList()
    alist = ArrayList.ArrayList()
    perf_time = time.perf_counter()
    val = create_random_values(10000)
    perf_time = time.perf_counter() - perf_time


    perf_time = time.perf_counter()
    llist.adding_random(val)
    perf_time = time.perf_counter() - perf_time

    messungen["llistadd"] = perf_time

    perf_time = time.perf_counter()
    alist.adding_elem(val)
    perf_time = time.perf_counter() - perf_time

    messungen["alistadd"] = perf_time
    # Llist sort
    perf_time = time.perf_counter()
    llist.insertionSortAsc()
    perf_time = time.perf_counter() - perf_time

    messungen["llistsort"] = perf_time

    perf_time = time.perf_counter()
    alist.sortAsc()
    perf_time = time.perf_counter() - perf_time

    messungen["alistsort"] = perf_time
    return messungen



def testing():
    max_work = os.cpu_count()
    tester = []
    arr_size = []
    for i in range(10):
       arr_size.append(1)
    max_work = 7 if max_work > 7 else max_work
    perftime= time.perf_counter()
    with multiproc.ProcessPoolExecutor(max_workers=max_work) as executor:
        for messung in executor.map(maintest, arr_size):
           tester.append(messung)
    perftime = time.perf_counter()-perftime
    print(tester)
    print("performance time:"+str(perftime))\



if __name__ == '__main__':
    print(maintest())
