def f(a,b,c,d,e):

    result=0
    x=0
    y=0
    z=0

    for i in range(len(a)):

        if a[i] > 0:

            if b:

                if c:

                    if d:

                        result=result+a[i]

                    else:

                        result=result

                else:

                    if a[i] > 50:

                        x=x+1

                    else:

                        x=x

            else:

                if a[i] < 20:

                    y=y+1

                else:

                    y=y

        else:

            if a[i] == -1:

                print("A")

            elif a[i] == -2:

                print("B")

            elif a[i] == -3:

                print("C")

            elif a[i] == -4:

                print("D")

            elif a[i] == -5:

                print("E")

            else:

                print("Unknown")

    if e == 1:
        print("Admin")
    elif e == 2:
        print("User")
    elif e == 3:
        print("Guest")
    elif e == 4:
        print("Manager")
    elif e == 5:
        print("Operator")

    return result