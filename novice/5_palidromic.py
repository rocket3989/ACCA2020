def isPalindrome(n):
    n = str(n)
    return n == n[::-1]
while True:
    num = input().strip()
    if num == '0': break
    
    if not isPalindrome(num):
        print(f'{num} is not a palindrome')
        continue
    
    sumOf = 0
    for digit in num:
        sumOf += int(digit)
    
    if not isPalindrome(sumOf):
        print(f'{num} is a palindrome')
        continue
    
    sumOf = 0
    for digit in num:
        sumOf += int(digit) ** 2
    
    if not isPalindrome(sumOf):
        print(f'{num} is a sum palindrome')
        continue
    print(f'{num} is a sum square palindrome')
    