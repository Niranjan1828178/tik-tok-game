import random

slate={1:'   ',2:'   ',3:'   ',4:'   ',5:'   ',6:'   ',7:'   ',8:'   ',9:'   ',}
print("player = X\tA.I = O\nPlayer goes first")
playercount=0
computercount=0
Winstate=False
turn='player'
countx=0
counto=0
def check(playercount, computercount):
    for i in [[1,2,3],[1,4,7],[1,5,9],[2,5,8],[3,6,9],[3,5,7],[4,5,6],[7,8,9]]:
        playercount=0
        for j in i:
            if slate[j]==' X ':
                playercount+=1
                
                if playercount>=3:
                    print("Player wins")
                    exit()
            else:
                playercount=0
        if playercount>=3:
            return True    
    for i in [[1,2,3],[1,4,7],[1,5,9],[2,5,8],[3,6,9],[3,5,7],[4,5,6],[7,8,9]]:
        computercount=0
        for j in i:
            if slate[j]==' O ':
                computercount+=1
                if computercount>=3:
                    print("computer wins")
                    exit()
            else:
                computercount=0
        if computercount>=3:
            return True

def Print_matrix():
    print(slate[1] + '|' + slate[2] + '|' + slate[3])
    print('-----------')
    print(slate[4] + '|' + slate[5] + '|' + slate[6])
    print('-----------')
    print(slate[7] + '|' + slate[8] + '|' + slate[9])

Print_matrix()

while True:
    if turn=='player':
        position=int(input("Player's turn\nEnter the position to draw X: "))
        if position<=9 and slate[position]=='   ':
            slate[position]=' X '
            Print_matrix()
            Winstate = check(playercount, computercount)
            turn='computer'
        else:
            if position>9 or slate[position]!='   ':
                print("Invalid Position, Try again!")
        boardfull=[]
        for q in range(0,9):
            if slate[q+1] != '   ':
                boardfull.append(q)
            if len(boardfull)>=9:
                print("Game Over")
                exit()
                
    if turn=='computer':
        print("Computer's turn now")
        turnover=False
        countx=0
        for i in [1,2,3,4,5,6,7,8,9]:
            if slate[i]==' O ' and not turnover:
                counto+=1
                poss={1:[[2,3],[4,7],[5,9]],2:[[1,3],[5,8]],3:[[1,2],[5,7],[6,9]],
                      4:[[5,6],[1,7]],5:[[1,9],[4,6],[2,8],[3,7]],6:[[3,9],[4,5]],7:[[1,4],[5,3],[8,9]],8:[[2,5],[7,9]],9:[[1,5],[7,8],[3,6]]}
                temp=poss[i]
                for j in temp:
                    sub=j
                    if slate[sub[0]]==' O ' or slate[sub[1]]==' O ':
                        if slate[sub[0]]==' O ' and slate[sub[1]]=='   ':
                                slate[sub[1]]=' O '
                                turn='player'
                                turnover=True
                                countx=0
                        if slate[sub[1]]==' X ' and slate[sub[0]]=='   ':
                                slate[sub[0]]=' O '
                                turn='player'
                                turnover=True
                                countx=0
        for i in [1,2,3,4,5,6,7,8,9]:
            if slate[i]==' X ' and not countx>=3 and not turnover:
                countx=1
                poss={1:[[2,3],[4,7],[5,9]],2:[[1,3],[5,8]],3:[[1,2],[5,7],[6,9]],
                      4:[[5,6],[1,7]],5:[[1,9],[4,6],[2,8],[3,7]],6:[[3,9],[4,5]],7:[[1,4],[5,3],[8,9]],8:[[2,5],[7,9]],9:[[1,5],[7,8],[3,6]]}
                temp=poss[i]
                for j in temp:
                    sub=j
                    if slate[sub[0]]==' X ' or slate[sub[1]]==' X ':
                        if slate[i]==' X ' and slate[sub[0]]==' X ' and slate[sub[1]]=='   ':
                                slate[sub[1]]=' O '
                                turn='player'
                                turnover=True
                                countx+=1
                        if slate[i]==' X ' and slate[sub[1]]==' X ' and slate[sub[0]]=='   ':
                                slate[sub[0]]=' O '
                                turn='player'
                                turnover=True
                                countx+=1
           
        if countx<2 and not turnover:
            
            inserted=False
            while not(inserted):
                pos=random.randint(1,9)
                if slate[pos]==' X ' or slate[pos]==' O ':
                    pos=random.randint(1,9)
                else:
                    slate[pos] = ' O '
                    inserted=True
                    turnover=True
                    turn='player'
                
        Print_matrix()
        Winstate = check(playercount, computercount)
        turn='player'
        boardfull=[]
        for q in range(0,9):
            if slate[q+1] != '   ':
                boardfull.append(q)
            if len(boardfull)>=9:
                print("Game Over")
                exit()
        
    



