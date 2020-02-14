# (Repeat additions) Listing 5.4, SubtractionQuizLoop.java, generates five random
# subtraction questions. Revise the program to generate ten random addition questions
# for two integers between 1 and 15 . Display the correct count and test time


import random
import datetime


def subtraction_quiz():
    current_time = datetime.datetime.now()
    print("Quiz started at: ", current_time.strftime("%H:%M:%S"))
    marks = 0
    for i in range(1, 11):
        print("Question#", i)
        num_one = random.randint(1, 15)
        num_two = random.randint(1, 15)
        result_actual = num_one - num_two
        result_got = (int(input("What is the result of " + str(num_one) + " - " + str(num_two) + ": ")))
        if result_actual != result_got:
            print("Wrong answer")
        else:
            marks += 1
            print("Right Answer")
    time = datetime.datetime.now()
    time_taken = time.second - current_time.second
    print("Total marks earned: ", marks)
    print("Total time taken: %s" % time_taken)


subtraction_quiz()
