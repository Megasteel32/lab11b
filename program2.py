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