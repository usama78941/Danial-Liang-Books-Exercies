# (Find the highest score) Write a program that prompts the user to enter the num-
# ber of students and each student’s name and score, and finally displays the name
# of the student with the highest score.


def highest_score():
    total_students = (int(input("Enter the total number of students: ")))
    max_score = 0
    final_name = ""
    for i in range(1, total_students):
        name = input("Enter the student name of student " + str(i) + ": ")
        score = (float(input("Enter Score: ")))
        if score > max_score:
            max_score = score
            final_name = name
    print("The student with maximums score is: " + final_name + " with a score of: " + str(max_score))


highest_score()
