def f(x):
    r = []

    for i in range(len(x)):
        for j in range(len(x)):
            if x[i] == x[j]:
                r.append(x[i])

    total = 0
    for i in range(len(x)):
        total += x[i]

    total2 = 0
    for i in range(len(x)):  # duplicated work
        total2 += x[i]

    mx = x[0]
    for i in range(len(x)):
        if x[i] > mx:
            mx = x[i]

    mn = x[0]
    for i in range(len(x)):
        if x[i] < mn:
            mn = x[i]

    count = 0
    for i in range(len(x)):
        for j in range(len(x)):
            for k in range(len(x)):
                if x[i] < x[j] < x[k]:
                    count += 1

    count2 = 0
    for i in range(len(x)):           # duplicated cubic work
        for j in range(len(x)):
            for k in range(len(x)):
                if x[i] > x[j] > x[k]:
                    count2 += 1

    print(total)
    print(total2)
    print(mx)
    print(mn)
    print(len(r))
    print(count)
    print(count2)
