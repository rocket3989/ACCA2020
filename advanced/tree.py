from collections import defaultdict
class node:
    def __init__(self):
        self.right = -1
        self.left = -1 
        self.val = -1
    
def getInd(char, S):
    for i, char1 in enumerate(S):
        if char == char1:
            return i

while True:
    nodes = defaultdict(node)
    sIn = input().strip()
    if sIn == "EXIT": exit()
    inOrder, postOrder = sIn.split()
    root = postOrder[-1]
    
    nodes[root].val = getInd(root, inOrder)
    
    def add(val, char, curr):
        if val > nodes[curr].val:
            if nodes[curr].right == -1:
                nodes[curr].right = char
                return
            add(val, char, nodes[curr].right)
        else:
            if nodes[curr].left == -1:
                nodes[curr].left = char
                return
            add(val, char, nodes[curr].left)
                
    for char in reversed(postOrder[:-1]):
        nodes[char].val = getInd(char, inOrder)
        add(getInd(char, inOrder), char, root)
    
    def dfs(node):
        if node == -1: return
        print(node, end='')
        dfs(nodes[node].left)
        dfs(nodes[node].right)

    dfs(root)
    
    print()