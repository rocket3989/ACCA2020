depth = int(input())

level = set([(10, 10)])
nextLevel = set()
for d in range(depth):
    for pair in level:
        nextLevel.add((max(pair[0] - 1, 0),   min(pair[1] + 2, 100)))
        nextLevel.add((min(pair[0] + 2, 100), max(pair[1] - 1, 0)))
        
    level = nextLevel
    nextLevel = set()

for tc in range(int(input())):
    tarL, tarR = [int(x) for x in input().split()]
    
    if (tarL, tarR) in level:
        print("possible")
    else:
        print("impossible")