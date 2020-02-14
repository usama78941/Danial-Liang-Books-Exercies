# (Count positive and negative numbers and compute the average of numbers) Write
# a program that reads an unspecified number of integers, determines how many
# positive and negative values have been read, and computes the total and average of
# the input values (not counting zeros). Your program ends with the input 0 . Display
# the average as a floating-point number


def count_positive_negative_number():
    positive_numbers = 0
    negative_numbers = 0
    total_sum = 0
    input_number = (int(input("Enter an integer, the input ends if it is 0: ")))
    total_num = 0
    while True:
        if input_number == 0:
            if total_num != 0:
                print("The number of positives is: ", positive_numbers)
                print("The number of negatives is: ", negative_numbers)
                print("The total is: ", total_sum)
                print("The average is: ", (total_sum / total_num))
            else:
                print("No numbers entered except 0")
            break
        elif input_number < 0:
            negative_numbers += 1
        else:
            positive_numbers += 1
        total_sum += input_number
        total_num += 1
        input_number = int(input())


count_positive_negative_number()
