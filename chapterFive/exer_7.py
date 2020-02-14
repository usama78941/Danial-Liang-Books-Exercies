# (Financial application: compute future tuition) Suppose that the tuition for a university
# is $10,000 this year and increases 5% every year. In one year, the tuition
# will be $10,500. Write a program that computes the tuition in ten years and the
# total cost of four years’ worth of tuition after the tenth year.


def tuition_calculator():
    tuition = 10000
    four_years = 0
    for i in range(1, 15):
        tuition = (tuition * 5) / 100 + tuition
        if i < 11:
            print("Tuition fee for year ", str(i), "is: %d" % tuition)
        else:
            four_years += tuition
    print("The total tuition fee after 10 years of four years would be: %d" % tuition)


tuition_calculator()
