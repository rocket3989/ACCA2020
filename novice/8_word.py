while True:
    strIn = input().strip()
    if strIn == 'All done': break
    
    lis = []
    last = 0
    for i, char in enumerate(strIn):
        if char.isalpha(): continue
        if i - last > 0:
            lis.append(strIn[last:i].upper())
        last = i + 1
        
    if strIn[-1].isalpha():
        lis.append(strIn[last:].upper())
        
    for a, b in zip(lis, reversed(lis)):
        if a != b:
            print(f"'{strIn}' is NOT a word palindrome")
            break
    else:
        print(f"'{strIn}' IS a word palindrome")
    