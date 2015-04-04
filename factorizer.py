import math
def factorizer(num):
    factorlist = []
    for checknum in range(1, int(math.sqrt(num))+1):
        if num % checknum == 0:
            factorlist.append(checknum)
    return factorlist