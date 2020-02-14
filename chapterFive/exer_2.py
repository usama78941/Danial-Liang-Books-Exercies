# (Conversion from kilograms to pounds) Write a program that displays the follow-
# ing table (note that 1 kilogram is 2.2 pounds):
# Kilograms     Pounds
# 1                2.2
# 3                6.6
# ...
# 197             433.4
# 199             437.8


def display_kilo_lbs_table():
    print("Kilograms", end='\t')
    print("Pounds")
    i = 1
    while i < 200:
        print(i, end='\t\t')
        print("%.1f" % (i * 2.2), end="\n")
        i += 2


display_kilo_lbs_table()
