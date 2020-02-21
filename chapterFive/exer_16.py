# (Find the factors of an integer) Write a program that reads an integer and displays
# all its smallest factors in increasing order. For example, if the input integer is
# 120 , the output should be as follows: 2 , 2 , 2 , 3 , 5 .


def factors():
    number = int(input("Enter the number: "))
    divisor = 2
    while True:
        while True:
            if number % divisor == 0:
                print(divisor, end=" ")
                break
            divisor += 1
        number = number / divisor
        if number == 1:
            break
        divisor = 2


factors()
