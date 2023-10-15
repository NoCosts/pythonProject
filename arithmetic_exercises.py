import random


def find_summands(summ_value: int) -> str:
    s = summ_value
    l = len(str(summ_value)) - 1
    r = random.randint(10 ** (l - 1), (10 ** l) - 1)
    b = summ_value - r
    return str(b) + ' + ' + str(r)


print(find_summands(5261))
