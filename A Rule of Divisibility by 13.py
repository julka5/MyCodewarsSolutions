def thirt(n):
    lst = [1, 10, 9, 12, 3, 4]
    i = 0
    sumn = n
    ind = True
    while ind:
        lofnum = [int(i) for i in str(sumn)[::-1]]
        for j in range(len(lofnum)):
            if i >= len(lst):
                i=0
            lofnum[j] = lofnum[j]*lst[i]
            i += 1
        i = 0
        if sum(lofnum) == sumn:
            ind = False
        sumn = sum(lofnum)

    return sumn

