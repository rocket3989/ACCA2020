i = 1
while True:
    mat1 = [['' for i in range(101)] for i in range(101)]
    mat2 = [['' for i in range(101)] for i in range(101)]
    
    direct = {1: (-1, 0), 2: (0, 1), 3: (1, 0), 4: (0, -1)}
    
    first = [int(x) for x in input().split()]
    if first[0] == 0: break
    
    second = [int(x) for x in input().split()]
    
    y, x = (first[0], first[1])
    
    mat1[y][x] = '*'
    for instr in first[2:-1]:
        y, x = y + direct[instr][0], x + direct[instr][1]
        mat1[y][x] = '*'
    
    y, x = (second[0], second[1])
    
    mat2[y][x] = '*'
    for instr in second[2:-1]:
        y, x = y + direct[instr][0], x + direct[instr][1]
        mat2[y][x] = '*'
    failed = False
    
    for row1, row2 in zip(mat1, mat2):
        for el1, el2 in zip(row1, row2):
            if el1 != el2:
                print(f'Figure {i}: Different')   
                failed = True
                break
        if failed: break
    else:
        print(f'Figure {i}: Same')

    i += 1