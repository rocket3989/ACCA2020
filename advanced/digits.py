from collections import defaultdict
while True:
    vals = input().split()
    lis = []
    sums = defaultdict(int)
    for val in vals:
        if len(val) > 9:
            print(val, "is too big, ignored.")
            continue
        if val[0] == '-':
            print(val, "is negative, ignored.")
            continue
        sumOf = 0
        for digit in val:
            sumOf += int(digit)
        lis.append((sumOf, int(val)))
        sums[sumOf] += 1
    lis.sort()
    for el in lis:
        print(el[1])
    for el in sorted(list(sums)):
        print(el, sums[el])
    if input().strip() == 'n': break