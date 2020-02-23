def neighbors(pair):
    r, c = pair
    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        if r + dr < 0 or r + dr > 8 or c + dc < 0 or c + dc > 8:
            continue
        yield (r + dr, c + dc)
        
for tc in range(int(input())):
    mat = []
    for i in range(9):
        mat.append([int(x) for x in input().split()])
    curr = None
    for i in range(9):
        for j in range(9):
            if mat[i][j] == 1:
                curr = (i, j)
                break
        if curr != None: break
    num = 1
    while num < 81:
        for r, c in neighbors(curr):
            if mat[r][c] == num + 1:
                num += 1
                curr = (r, c)
                break
        else:
            print('invalid')
            break
    else:
        print('valid')
        
    