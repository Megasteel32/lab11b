# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Luca Maddaleni, 330001030
# Section:     273
# Assignment:  Perfect Numbers
# Date:        11/04/20

def perfectnumber():
    number = int(input("Enter a number to test: "))
    while number < 0:
        number = int(input("Enter a number to test: "))
    proper_divisors = []
    for x in range(number):
        if x > 0 and number % x == 0:
            proper_divisors.append(x)
    if sum(proper_divisors) == number:
        print("{} is a proper number!".format(number))
    else:
        print("{} is not a proper number!".format(number))

perfectnumber()