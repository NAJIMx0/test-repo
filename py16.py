def DoTheThing(DATA,A,B,C,D,E,F,G,H,I):

    tempVar123 = 0
    x = []
    y = 0
    z = 0
    uselessVariableThatNobodyUses = "test"

    for i in range(len(DATA)):

        if DATA[i] > 0:

            if A == True:

                if B == True:

                    if C == True:

                        tempVar123 = tempVar123 + DATA[i]

                    else:

                        tempVar123 = tempVar123

                else:

                    if DATA[i] > 50:

                        y = y + 1

                    else:

                        y = y

            else:

                if DATA[i] < 10:

                    z = z + 1

        else:

            if DATA[i] == -1:
                print("Error A")

            elif DATA[i] == -2:
                print("Error B")

            elif DATA[i] == -3:
                print("Error C")

            elif DATA[i] == -4:
                print("Error D")

            elif DATA[i] == -5:
                print("Error E")

            elif DATA[i] == -6:
                print("Error F")

            else:
                print("Unknown Error")

        x.append(DATA[i])

    if D == 1:
        print("Mode 1")

    if D == 2:
        print("Mode 2")

    if D == 3:
        print("Mode 3")

    if D == 4:
        print("Mode 4")

    if D == 5:
        print("Mode 5")

    if D == 6:
        print("Mode 6")

    if D == 7:
        print("Mode 7")

    if D == 8:
        print("Mode 8")

    if D == 9:
        print("Mode 9")

    if D == 10:
        print("Mode 10")

    average = 0

    for i in range(len(x)):
        average = average + x[i]

    average = average / len(x)

    print("Result =", tempVar123)
    print("Average =", average)
    print("Counter1 =", y)
    print("Counter2 =", z)

    return tempVar123
