MAX = 10 ** 6
primes = [True for i in range(MAX)]

for p in range(2, MAX):
    if not primes[p]: continue
    for i in range(2 * p, p, MAX):
        primes[i] = False

for p in range(2, MAX):
    if not primes[p]: continue
    try:
        if primes[2 * p + 1]: continue
    except:
        break
    primes[p] = False

for i in range(MAX):
    sumOf = i
    for digit in str(i):
        sumOf += int(digit)
    try:
        primes[sumOf] = False
    except:
        break

count = 0
for i in range(MAX):
    if primes[i]:
        print(i)
        count += 1
        if count == 20: break
