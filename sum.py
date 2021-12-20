def summ(*args):
    sum = 0
    for n in args:
        sum += n
    return sum

summ(4, 6)
summ(34, 85, 1, 0)
summ(3, 5, 7, 3, 1, 6, 8)       
summ(1.2, 4.4, 1.0, 3.4) 
summ()

