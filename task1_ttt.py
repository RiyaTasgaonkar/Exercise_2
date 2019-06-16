# tic tac toe
a=[[0,0,0],[0,0,0],[0,0,0]]
print('For player 1 symbol is x')
print('For player 2 symbol is o')
game=0
for i in range(5):
    if game==1:
        break
    # player 1
    print('For player 1:')
    x=int(input("Enter row no. :"))
    y=int(input("Enter column no. :"))
    if (a[x][y]==0 and a[x][y]!='o'):
        a[x][y]='x'
    else:
        print('Enter correct input')
        x=int(input("Enter row no. :"))
        y=int(input("Enter column no. :"))
        a[x][y]='x'
    for l in a:
        for m in l:
            print(m,end=' ')
        print()
    if(i==5):
        break
    #check
    for l in range(3):
        y=0
        for m in range(3):
            if a[l][m]=='x':
                y=y+1
        if y==3:
            print('Player 1 is winner')
            game=1
    for l in range(3):
        y=0
        for m in range(3):
            if a[m][l]=='x':
                y=y+1
        if y==3:
                print('Player 1 is winner')
                game=1
    if (a[0][0]=='x'and a[1][1]=='x' and a[2][2]=='x'):
        print('Player 1 is winner')
        game=1
    if (a[0][2]=='x'and a[1][1]=='x' and a[2][0]=='x'):
        print('Player 1 is winner')
        game=1
    if game==1:
        break       

    #player 2
    print('For player 2:')
    x=int(input("Enter row no. :"))
    y=int(input("Enter column no. :"))
    if (a[x][y]==0 and a[x][y]!='x'):
        a[x][y]='o'
    else:
        print('Enter correct input')
        x=int(input("Enter row no. :"))
        y=int(input("Enter column no. :"))
        a[x][y]='o'
    for l in a:
        for m in l:
            print(m,end=' ')
        print() 
    #check
    for l in range(3):
        p=0
        for m in range(3):
            if a[l][m]=='o': 
                p=p+1
        if p==3:
            print('Player 2 is winner')
            game=1
    for l in range(3):
        p=0
        for m in range(3):
            if a[m][l]=='o':
                p=p+1
        if p==3:
            print('Player 2 is winner')
            game=1
    if (a[0][0]=='o'and a[1][1]=='o' and a[2][2]=='0'):
        print('Player 2 is winner')
        game=1
    if (a[0][2]=='o'and a[1][1]=='0' and a[2][0]=='o'):
        print('Player 2 is winner')
        game=1
    