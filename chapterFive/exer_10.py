# (Find numbers divisible by 5 and 6) Write a program that displays all the num-
# bers from 100 to 1,000, ten per line, that are divisible by 5 and 6. Numbers are
# separated by exactly one space.


def numbers_divisible_by_five_and_six():
    start_value = 100
    count = 1
    while start_value <= 1000:
        if (start_value % 5 == 0) & (start_value & 6 == 0):
            print(start_value, end=" ")
            count += 1

        if count % 10 == 0:
            count = 1
            print(end="\n")

        start_value += 1


numbers_divisible_by_five_and_six()
