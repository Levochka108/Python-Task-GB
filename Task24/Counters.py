#  Блок подсчета, добаваления

def Count_program(array):
    array_count = list()

    for i in range(len(array) - 1):
        array_count.append(array[i - 1] + array[i] + array[i + 1])

    array_count.append(array[-2] + array[-1] + array[0])
    result = array_count
    return result
