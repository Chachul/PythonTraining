from numpy import random

list = random.randint(100, size=40)

print(list)


def bubblesort(unsorted_list):
    length = len(unsorted_list) - 1
    sorted = False

    while not sorted:
        sorted = True
        for i in range(0, length):
            if unsorted_list[i] < unsorted_list[i + 1]:
                sorted = False
                unsorted_list[i], unsorted_list[i + 1] = unsorted_list[i + 1], unsorted_list[i]


bubblesort(list)

print(list)

for i in range(0, len(list)):
    if (list[i] % 2) == 0:
        list[i] = 0

print(list)
