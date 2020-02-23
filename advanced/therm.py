directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
class thermometer:
    def __init__(self, y, x, direct, length):
        self.y = y
        self.x = x
        self.direct = direct
        self.length = length
    def nextNode(self, curr):
        return (self.y + curr * directions[self.direct][0], self.x + curr * directions[self.direct][1])
    def __repr__(self):
        return f'{self.y}, {self.x}, {self.direct}, {self.length}'

r, c = [int(x) for x in input().split()]

rowClues = [int(x) for x in input().split()]
colClues = [int(x) for x in input().split()]

mat = [['.' for i in range(c)] for i in range(r)]

parentOf = [[-1 for i in range(c)] for i in range(r)]

thermometers = []

def getNext(therm, curr):
    if therm == len(thermometers):
        return -1
    if curr + 1 <= thermometers[therm].length:
        return (thermometers[therm].nextNode(curr + 1), therm, curr + 1)
    if therm + 1 == len(thermometers):
        return -1
    return (thermometers[therm + 1].nextNode(0), therm + 1, 0)


for therm in range(int(input())):
    br, bc, tr, tc = [int(x) for x in input().split()]
    if br == tr:
        if tc > bc:
            thermometers.append(thermometer(br, bc, 0, tc - bc))
        else:
            thermometers.append(thermometer(br, bc, 1, bc - tc))
    else:
        if tr > br:
            thermometers.append(thermometer(br, bc, 2, tr - br))
        else:
            thermometers.append(thermometer(br, bc, 3, br - tr))


backtracks = 0
def solve(data):
    if data == -1:
        # for row in mat:
        #     print(*row, sep='')
        # print(colClues, rowClues)
        # input()
        
        fail = False
        for clue in colClues:
            if clue != 0:
                fail = True
                break
        for clue in rowClues:
            if clue != 0:
                fail = True
                break
        return not fail
        
    pos, therm, curr = data
        
    if colClues[pos[1]] == 0 or rowClues[pos[0]] == 0:
        return solve(getNext(therm + 1, -1))
    
    colClues[pos[1]] -= 1
    rowClues[pos[0]] -= 1
    
    mat[pos[0]][pos[1]] = 'x'
    
    if solve(getNext(therm, curr)):
        return True
    
    colClues[pos[1]] += 1
    rowClues[pos[0]] += 1
    
    mat[pos[0]][pos[1]] = '.'
    global backtracks
    backtracks += 1
    return solve(getNext(therm + 1, -1))

solve(getNext(0, -1))

for row in mat:
    print(*row, sep='')

print(f'backtracked {backtracks} times')