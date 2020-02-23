from collections import defaultdict
while True:
    vals = input().split()
    counter = defaultdict(int)
    for val in vals:
        sumOf = 0
        for digit in val:
            sumOf += int(digit)
        counter[sumOf] += 1
    for k, v in sorted(counter.items()):
        print(k, v)
    if input().strip() == 'n': break