# (Find the smallest n such that n 2 7 12,000) Use a while loop to find the smallest
# integer n such that n 2 is greater than 12,000
from math import sqrt


def smallest_number():
    while True:
        square_root = sqrt(12000)
        square_root = int(square_root)
        square_root += 1
        print(square_root)
        break


smallest_number()
# didn't do by brute force

