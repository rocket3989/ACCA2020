def isPali(n):
    n = str(n)
    for a, b in zip(n, reversed(n)):
        if a != b:
            return False
    return True


while True:
    N = int(input())
    if N == 0: break
    test = 0
    while test < 100:
        if isPali(N):
            break
        temp = N
        rev = 0
        while temp:
            rev = rev * 10 + (temp % 10)
            temp //= 10
        N += rev
        test += 1
    if test == 0:
        print("Already a palindrome")
    elif test == 100:
        print("Not palindrome after 100 iterations")
    else:
        print("Palindrome", N, test, "iterations")
    