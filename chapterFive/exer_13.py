# (Find the largest n such that n 3 6 12,000) Use a while loop to find the largest
# integer n such that n 3 is less than 12,000.


def largest_number():
    start = 1
    while True:
        if start ** 3 > 12000:
            print(start - 1)
            break
        start += 1


largest_number()
