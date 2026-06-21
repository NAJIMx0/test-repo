def q(data,a,b,c):

    r=0

    for i in range(len(data)):

        for j in range(len(data)):

            for k in range(len(data)):

                if data[i] < data[j]:

                    if data[j] < data[k]:

                        if a == 1:

                            r=r+1

                        else:

                            if b == 1:

                                r=r+2

                            else:

                                if c == 1:

                                    r=r+3

                                else:

                                    r=r

    total=0

    for i in range(len(data)):
        total=total+data[i]

    avg=total/len(data)

    print(total)
    print(avg)
    print(r)

    return r