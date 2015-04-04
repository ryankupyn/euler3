import math
def primechecker(num):
    prime = True
    for x in range(2, int(math.sqrt(num))+1):
        if num % x == 0:
            prime = False
    return prime