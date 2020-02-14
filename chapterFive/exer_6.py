def display_miles_kilo_table_dual():
    print("Miles", end='\t')
    print("Kilometers", end="\t\t")
    print("|", end="\t\t")
    print("Kilometers", end="\t\t")
    print("Miles")
    i = 1
    start = 20
    while i < 11:
        print(i, end='\t\t\t')
        print("%.3f " % (i * 1.609), end="\t\t")
        print("|", end="\t\t")
        print(str(start), end="\t\t\t\t")
        print("%.3f" % (start / 1.609))
        i += 1
        start += 5


display_miles_kilo_table_dual()
