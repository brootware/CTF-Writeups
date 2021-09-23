import luhn


for i in range(5432100000001234, 5432109999991234, 10000):
    if i % 123457 == 0 and luhn.verify(str(i)):
        print("CTFlearn{{{}}}".format(i))

""" 
from itertools import *
def convertTuple(tup):
    str = ''.join(tup)
    return str


for i in product('0123456789', repeat=6):
    str = convertTuple(i)
    number = '543210' + str + '1234'
    mulnum = int(number)
    if (verify(number)) and (mulnum % 123457 == 0):
        print("CTFlearn{{{}}}".format(number)) """
