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