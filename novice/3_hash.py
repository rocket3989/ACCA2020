while True:
    sIn = input().strip()
    lis = sIn.split()
    
    wordVal = 0
    hashOf = 0
    for word in lis:
        hashOf += wordVal
        wordVal = 0
        vowelC = 1
        for letter in word:
            wordVal += ord(letter)
                
        hashOf += wordVal
        
    for char in sIn:
        if char == ' ':
            hashOf += ord(char)
            
    print(f'The hash is {hashOf % 100}.')

    if input().strip() == 'n': break