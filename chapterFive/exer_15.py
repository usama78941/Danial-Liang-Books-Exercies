# (Display the ASCII character table) Write a program that prints the characters in
# the ASCII character table from ! to ~ . Display ten characters per line. The ASCII
# table is shown in Appendix B. Characters are separated by exactly one space.


def display_ascii():
    start = 33
    count = 1
    while start <= 126:
        print(chr(start), end=" ")
        if count % 10 == 0:
            count = 0
            print(end="\n")

        start += 1
        count += 1


display_ascii()

