y, x = 0, 0
step = [0 for i in range(1000)]

def change(depth):
    global x, y
    if step[depth] == 4:
        step[depth] = 0
        step[depth + 1] += 1
        change(depth + 1)
        
    curr = step[depth]
    if curr % 2 == 1: 
        x += depth
    else:
        x -= depth
        
    if curr == 2:
        y += depth
    if curr == 0:
        y -= depth
    

for move in range(1, 1 + int(input())):
    print(x, y)
    step[1] += 1
    change(1)
    
            