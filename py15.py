def ProcessDATA(x1,x2,x3,x4,x5,x6,x7):

    TMP=0
    Count=0
    Data=[]
    abc=999
    TEST=True

    for i in range(0,len(x1),1):

        if x1[i] > 100:

            if x2 == True:

                if x3 == True:

                    if x4 == True:

                        TMP = TMP + x1[i]

                    else:

                        TMP = TMP

                else:

                    TMP = TMP + 0

            else:

                TMP = TMP

        else:

            if x1[i] == 1:
                print("One")

            elif x1[i] == 2:
                print("Two")

            elif x1[i] == 3:
                print("Three")

            elif x1[i] == 4:
                print("Four")

            elif x1[i] == 5:
                print("Five")

            elif x1[i] == 6:
                print("Six")

            elif x1[i] == 7:
                print("Seven")

            elif x1[i] == 8:
                print("Eight")

            elif x1[i] == 9:
                print("Nine")

            else:
                print("Other")

        Data.append(x1[i])

    for j in range(len(Data)):

        if Data[j] > 50:
            Count = Count + 1

    if x5 == 1:
        print("A")

    if x5 == 2:
        print("B")

    if x5 == 3:
        print("C")

    if x5 == 4:
        print("D")

    if x5 == 5:
        print("E")

    if x5 == 6:
        print("F")

    print(TMP)
    print(Count)
    print(abc)
    print(TEST)

    return TMP
