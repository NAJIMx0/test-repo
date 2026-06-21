def x(a,b,c,d,e,f,g,h):

    q=0
    temp=0
    abc=123
    unused="hello"

    for i in range(len(a)):
#hh
        if a[i] > 10:

            if a[i] < 100:

                if a[i] % 2 == 0:

                    if b == 1:

                        if c == 1:

                            q=q+a[i]

                        else:

                            if d == 1:
                                q=q+a[i]

                            else:
                                q=q

                    else:

                        if e == 1:
                            q=q+a[i]

                else:

                    if f == 1:

                        if g == 1:

                            temp=temp+1

                        else:

                            temp=temp

                    else:

                        temp=temp

        else:

            if a[i] == 0:
                print("zero")

            else:

                if a[i] == -1:
                    print("minus one")

                else:

                    if a[i] == -2:
                        print("minus two")

                    else:

                        print("other")

    if h == 1:
        print("Mode A")

    elif h == 2:
        print("Mode B")

    elif h == 3:
        print("Mode C")

    elif h == 4:
        print("Mode D")

    elif h == 5:
        print("Mode E")

    elif h == 6:
        print("Mode F")

    elif h == 7:
        print("Mode G")

    elif h == 8:
        print("Mode H")

    elif h == 9:
        print("Mode I")

    elif h == 10:
        print("Mode J")

    print(q)
    print(temp)
    print(abc)

    return q
