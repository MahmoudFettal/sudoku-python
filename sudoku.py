def exist(L,x):
    for i in L:
        if i == x:
            return True
    return False
def remove(L,x):
    while L.count(x) != 0 :
        L.remove(x)
    return L 
def indexpossible_in_bloc(G,b,r):
    i = (b//3)*3 + r//3
    j = (b%3)*3 + r%3
    return G[i][j]
def possible_in_line(G,i):
    possible = [i for i in range(1,10)]
    for j in range(9):
        remove(possible,G[i][j])
    return possible
def possible_in_column(G,j):
    possible = [i for i in range(1,10)]
    for i in range(9):
        remove(possible,G[i][j])
    return possible    
def possible_in_bloc(G,n):
    possible = [i for i in range(1,10)]
    for i in range(9):
        remove(possible,indexpossible_in_bloc(G,n,i))
    return possible
def possibles(G,i,j):
    possible = []
    pligne   = possible_in_line(G,i)
    pcolumn  = possible_in_column(G,j)
    pbloc    = possible_in_bloc(G, 3*(i//3) + j//3)
    for x in range(1,10):
        if exist(pligne,x) and exist(pcolumn,x) and exist(pbloc,x):
            possible.append(x)            
    return possible
def solution(G):
    while True:
        switchs = 0
        for i in range(9):
            for j in range(9):
                possib = possibles(G,i,j)
                if len(possib)== 1 and  G[i][j] == 0:
                    switchs += 1
                    G[i][j] = possib[0]
        if switchs == 0:
            break
def solve(G,n=0):
    for i in range(9):
        for j in range(9):
            if G[i][j] == 0:
                for k in range(1,10):
                    if k in possibles(G,i,j):
                        G[i][j] = k
                        solve(G,n)
                        G[i][j] = 0
                return

    print('solution')
    show(G)
def show(G):
    fill       = '|   '
    separation  = [u'\u251C']
    separation2 = [u'\u251C'] 
    for k in range(1,9):
        if k%3 == 0:
            fill += u'\u2503'+'   '
            separation += [u'\u2500'+u'\u2500'+u'\u2500'+u'\u254B']
            separation2 += [u'\u2501'+u'\u2501'+u'\u2501'+u'\u254B']
        else: 
            fill += '|   '
            separation += [u'\u2500'+u'\u2500'+u'\u2500'+u'\u253C']
            separation2 += [u'\u2501'+u'\u2501'+u'\u2501'+u'\u253C']
    fill += '|'
    fill = list(fill)
    separation  += [u'\u2500'+u'\u2500'+u'\u2500'+u'\u2524']
    separation2 += [u'\u2501'+u'\u2501'+u'\u2501'+u'\u2524']
    top        = [u'\u250C'] + [u'\u2500'+u'\u2500'+u'\u2500'+u'\u252C' for i in range(8) ] + [u'\u2500'+u'\u2500'+u'\u2500'+u'\u2510']
    bottom     = [u'\u2514'] + [u'\u2500'+u'\u2500'+u'\u2500'+u'\u2534' for i in range(8) ] + [u'\u2500'+u'\u2500'+u'\u2500'+u'\u2518']
    presentation = [top]
    for i in range(8):
        fill1 = fill.copy()
        for j in range(9):
            if G[i][j] != 0:
                fill1[2+ j*4] =str(G[i][j])
        presentation.append(fill1)
        if i%3 == 2:
            presentation.append(separation2)
        else:
            presentation.append(separation)
    for j in range(9):
        if G[8][j] != 0:
            fill[2+ j*4] =str(G[8][j])
    presentation.append(fill) 
    presentation.append(bottom)
    for i in presentation:
        print(''.join(i))  
G = [[0,0,9,6,1,0,3,0,5],
     [0,0,0,7,0,0,0,9,6],
     [6,0,0,0,0,9,8,1,0],
     [0,0,0,3,6,0,9,8,0],
     [2,8,0,9,0,0,0,5,0],
     [9,3,0,0,5,0,7,0,0],
     [0,0,0,0,8,5,1,0,0],
     [0,0,7,2,0,3,5,0,0],
     [0,9,0,1,7,0,0,0,2]]
print('input')
show(G)
solve(G)
