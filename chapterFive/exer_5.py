def display_kilo_lbs_table():
    print("Kilograms", end='\t')
    print("Pounds", end="\t\t")
    print("|", end="\t\t")
    print("Pounds", end="\t\t")
    print("Kilograms")
    i = 1
    start = 20
    while i < 200:
        print(str(i), end='\t\t\t')
        print("%.1f " % (i * 2.2), end="\t\t")
        print("|", end="\t\t")
        print(str(start), end="\t\t\t")
        print("%.2f" % (start / 2.2))
        i += 2
        start += 5


display_kilo_lbs_table()
