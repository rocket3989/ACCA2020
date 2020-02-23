vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
punc = set(['.', '!', '?', ' '])
while True:
    sIn = input().strip()
    lis = []
    last = 0
    for i, char in enumerate(sIn):
        if char in punc:
            if i - last > 0:
                lis.append(sIn[last: i])
            last = i + 1
            
    if sIn[-1] not in punc:
        lis.append(sIn[last:])
    
    wordVal = 0
    hashOf = 0
    for word in lis:
        hashOf += wordVal
        wordVal = 0
        vowelC = 1
        for letter in word:
            if letter in vowels:
                wordVal += vowelC
                vowelC += 1
            else:
                wordVal += ord(letter)
                
        hashOf += wordVal
        
    if sIn[-1] in punc:
        hashOf += wordVal
        
    for char in sIn:
        if char in punc:
            hashOf += ord(char)
            
    print(f'The hash is {hashOf % 100}.')

    if input().strip() == 'n': break