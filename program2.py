# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Luca Maddaleni, 330001030
# Section:     273
# Assignment:  Label Me
# Date:        11/04/20

def address():
    name = input("Enter your name: ")
    address1 = input("Enter Address 1: " )
    address2 = input("Enter Address 2: ")
    city = input("Enter your city: ")
    state = input("Enter your state: ")
    zipcode = input("Enter your zipcode: ")
    print(name)
    print(address1)
    if address2 != "":
        print(address2)
    print(city + ",", state, zipcode)

address()