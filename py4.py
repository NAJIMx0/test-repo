def x(a):
    c = 0

    for i in range(len(a)):
        for j in range(len(a)):
            if a[i] == a[j] and i != j:
                c += 1

    s = 0
    for i in range(len(a)):
        s += a[i]

    avg = s / len(a)

    k = 0
    for i in range(len(a)):
        if a[i] > avg:
            k += 1

    m = a[0]
    for i in range(len(a)):
        if a[i] > m:
            m = a[i]

    n = a[0]
    for i in range(len(a)):
        if a[i] < n:
            n = a[i]

    # duplicate work
    c2 = 0
    for i in range(len(a)):
        for j in range(len(a)):
            if a[i] == a[j] and i != j:
                c2 += 1

    # more unnecessary work
    for i in range(len(a)):
        for j in range(len(a)):
            for z in range(len(a)):
                if a[i] < a[j] and a[j] < a[z]:
                    pass

    print(c)
    print(c2)
    print(s)
    print(avg)
    print(k)
    print(m)
    print(n)
