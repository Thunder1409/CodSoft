number_1 = int(input("Enter first number -: "))
number_2 = int(input("Enter second number -: "))

while True:
    print("\n\n1. + \n2. - \n3. * \n4. / \n50. ALL \n99. EXIT")

    operation = int(input("Enter arithmetic operation (1,2,3,4) -: "))
    print("\n")

    if (operation == 1):
        print("SUM -: ", number_1+number_2)

    elif (operation == 2):
        print("SUBTRACT -: ", number_1 - number_2)

    elif (operation == 3):
        print("PRODUCT -: ", number_1 * number_2)

    elif (operation == 4):
        print("DIVIDE -: ", number_1/number_2)

    elif(operation == 50):
        print("SUM -: ", number_1+number_2)
        print("SUBTRACT -: ", number_1 - number_2)
        print("PRODUCT -: ", number_1 * number_2)
        print("DIVIDE -: ", number_1/number_2)


    elif(operation == 99):
        print("Quiting")
        break

    else:
        print("Worong Operator")