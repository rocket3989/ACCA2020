for tc in range(int(input())):
    print(input())
    
    aggression, cuteness = 10, 10
    for change in range(int(input())):
        if input() == 'tickle':
            cuteness += 2
            aggression -= 1
        else:
            cuteness -= 1
            aggression += 2
        cuteness = max(min(cuteness, 100), 0)
        aggression = max(min(aggression, 100), 0)
        
    print(cuteness, aggression)
        
    