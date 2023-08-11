#Problem1
#Statement: If we list all the numbers below 10, that are muliples of 3 or 5, they are considered to be 3,5,6,9, and their sum is 23.
#Similarly find the sum of all the numbers below 1000, that are muliples of 3 or 5.

def summation():
    total = 0
    for i in range(0,1000):
        if i % 3 == 0 or i % 5 == 0:
            total += i
    return total

summation()