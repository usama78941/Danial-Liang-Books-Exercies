# (Find the two highest scores) Write a program that prompts the user to enter the
# number of students and each student’s name and score, and finally displays the
# student with the highest score and the student with the second-highest score.


def two_highest_scores():
    highest_score = 0
    high_name = ""
    second_highest_score = 0
    second_name = ""
    students_count = int(input("Enter the number of students: "))
    start = 0
    while start < students_count:
        curr_name = input("Enter the name of the student: ")
        curr_score = int(input("Enter the student score: "))
        if curr_score > highest_score:
            second_highest_score = highest_score
            second_name = high_name
            highest_score = curr_score
            high_name = curr_name

    print("The student with the highest score is: ", highest_score, " and his name is: ", high_name)
    print("The student with the second highest score is: ", second_highest_score, " and his name is: ", second_name)


two_highest_scores()
