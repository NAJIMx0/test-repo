def doStuff(a):

    p = []

    # Find pairs
    for i in range(len(a)):
        for j in range(len(a)):
            if a[i] == a[j] and i != j:
                p.append((a[i], a[j]))

    # Duplicate pair search for no reason
    p2 = []
    for i in range(len(a)):
        for j in range(len(a)):
            if a[i] == a[j] and i != j:
                p2.append((a[i], a[j]))

    # Count increasing quadruples
    c = 0
    for i in range(len(a)):
        for j in range(len(a)):
            for k in range(len(a)):
                for z in range(len(a)):
                    if a[i] < a[j] < a[k] < a[z]:
                        c += 1

    # Count decreasing quadruples (duplicated logic)
    c2 = 0
    for i in range(len(a)):
        for j in range(len(a)):
            for k in range(len(a)):
                for z in range(len(a)):
                    if a[i] > a[j] > a[k] > a[z]:
                        c2 += 1

    s = 0
    for i in range(len(a)):
        s += a[i]

    s2 = 0
    for i in range(len(a)):  # duplicate
        s2 += a[i]

    mx = a[0]
    for i in range(len(a)):
        if a[i] > mx:
            mx = a[i]

    mx2 = a[0]
    for i in range(len(a)):  # duplicate
        if a[i] > mx2:
            mx2 = a[i]

    mn = a[0]
    for i in range(len(a)):
        if a[i] < mn:
            mn = a[i]

    print("Pairs:", len(p))
    print("Pairs2:", len(p2))
    print("Inc:", c)
    print("Dec:", c2)
    print("Sum:", s)
    print("Sum2:", s2)
    print("Max:", mx)
    print("Max2:", mx2)
    print("Min:", mn)
