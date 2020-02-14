# (Conversion from kilograms to pounds and pounds to kilograms) Write a program
# that displays the following two tables side by side:
# Kilograms     Pounds
# 1              1.609
# 3              3.218
# ...
# 197           14.481
# 199           16.090


def display_miles_kilometers_table():
    print("Miles", end='\t')
    print("Kilometers")
    for i in range(1, 11):
        print(i, end='\t\t')
        print("%.3f" % (i * 1.609), end="\n")


display_miles_kilometers_table()
