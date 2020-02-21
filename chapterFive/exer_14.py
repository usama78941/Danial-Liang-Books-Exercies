# (Compute the greatest common divisor) Another solution for Listing 5.9 to find
# the greatest common divisor of two integers n1 and n2 is as follows: First find d
# to be the minimum of n1 and n2 , then check whether d , d-1 , d-2 , . . . , 2 , or 1 is
# a divisor for both n1 and n2 in this order. The first such common divisor is the
# greatest common divisor for n1 and n2 . Write a program that prompts the user to
# enter two positive integers and displays the gcd.


def greatest_common_divisor():
    number_one = int(input("Enter number one: "))
    number_two = int(input("Enter number two: "))

    if number_one > number_two:
        number_one = number_one + number_two
        number_two = number_one - number_two
        number_one = number_one - number_two

    divisor = number_one - 1

    while True:
        if (number_one % divisor == 0) & (number_two % divisor == 0):
            if divisor != 1:
                print("Greatest common divisor would be:", divisor)
            else:
                print("No greatest common divisor found")
            break
        divisor -= 1


greatest_common_divisor()
