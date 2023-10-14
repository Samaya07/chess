board=[['brook   ','0       ','bbishop ','0       ','0       ','bbishop ','bknight ','brook   '],
       ['0       ','bpawn   ','bpawn   ','bpawn   ','0       ','bpawn   ','0       ','bpawn   '],
       ['0       ','0       ','bknight ','0       ','0       ','0       ','bpawn   ','0       '],
       ['wrook   ','0       ','0       ','bking   ','bpawn   ','0       ','0       ','0       '],
       ['bpawn   ','0       ','wpawn   ','0       ','0       ','0       ','0       ','bqueen  '],
       ['wbishop ','wpawn   ','0       ','0       ','wpawn   ','0       ','0       ','wknight '],
       ['wpawn   ','0       ','wqueen  ','wpawn   ','0       ','wpawn   ','wpawn   ','wpawn   '],
       ['0       ','wknight ','0       ','0       ','wking   ','wbishop ','0       ','wrook   ']]

board2=[['brook   ','0       ','bbishop ','0       ','0       ','bbishop ','bknight ','brook   '],
       ['0       ','bpawn   ','bpawn   ','bpawn   ','0       ','bpawn   ','0       ','bpawn   '],
       ['0       ','0       ','bknight ','0       ','0       ','0       ','bpawn   ','0       '],
       ['wrook   ','0       ','0       ','bking   ','bpawn   ','0       ','0       ','0       '],
       ['bpawn   ','0       ','wpawn   ','0       ','0       ','0       ','0       ','bqueen  '],
       ['wbishop ','wpawn   ','0       ','0       ','wpawn   ','0       ','0       ','wknight '],
       ['wpawn   ','0       ','wqueen  ','wpawn   ','0       ','wpawn   ','wpawn   ','wpawn   '],
       ['0       ','wknight ','0       ','0       ','wking   ','wbishop ','0       ','wrook   ']]
 

def move_generator_rook(loc):
    piece=board[loc[0]][loc[1]]
    x=loc[0]
    y=loc[1]
    moves=[]
    checks=0
    if piece[0]=='b':
        for i in range(y+1,8):
            if board[x][i].rstrip()=='0':
                moves.append([x,i])
            else:
                obstacle=board[x][i]
                if obstacle[0]=='b':
                    break
                elif obstacle[0]=='w':
                    if obstacle.rstrip()!='wking':
                        moves.append([x,i])
                    else:
                        checks+=1
                    break
        for i in range(y-1,-1,-1):
            if board[x][i].rstrip()=='0':
                moves.append([x,i])
            else:
                obstacle=board[x][i]
                if obstacle[0]=='b':
                    break
                elif obstacle[0]=='w':
                    if obstacle.rstrip()!='wking':
                        moves.append([x,i])
                    else:
                        checks+=1
                    break
        for i in range(x+1,8):
            if board[i][y].rstrip()=='0':
                moves.append([i,y])
            else:
                obstacle=board[i][y]
                if obstacle[0]=='b':
                    break
                elif obstacle[0]=='w':
                    if obstacle.rstrip()!='wking':
                        moves.append([i,y])
                    else:
                        checks+=1
                    break
        for i in range(x-1,-1,-1):
            if board[i][y].rstrip()=='0':
                moves.append([i,y])
            else:
                obstacle=board[i][y]
                if obstacle[0]=='b':
                    break
                elif obstacle[0]=='w':
                    if obstacle.rstrip()!='wking':
                        moves.append([i,y])
                    else:
                        checks+=1
                    break

    elif piece[0]=='w':
        for i in range(y+1,8):
            if board[x][i].rstrip()=='0':
                moves.append([x,i])
            else:
                obstacle=board[x][i]
                if obstacle[0]=='w':
                    break
                elif obstacle[0]=='b':
                    if obstacle.rstrip()!='bking':
                        moves.append([x,i])
                    else:
                        checks+=1
                    break
        for i in range(y-1,-1,-1):
            if board[x][i].rstrip()=='0':
                moves.append([x,i])
            else:
                obstacle=board[x][i]
                if obstacle[0]=='w':
                    break
                elif obstacle[0]=='b':
                    if obstacle.rstrip()!='bking':
                        moves.append([x,i])
                    else:
                        checks+=1
                    break
        for i in range(x+1,8):
            if board[i][y].rstrip()=='0':
                moves.append([i,y])
            else:
                obstacle=board[i][y]
                if obstacle[0]=='w':
                    break
                elif obstacle[0]=='b':
                    if obstacle.rstrip()!='bking':
                        moves.append([i,y])
                    else:
                        checks+=1
                    break
        for i in range(x-1,-1,-1):
            if board[i][y].rstrip()=='0':
                moves.append([i,y])
            else:
                obstacle=board[i][y]
                if obstacle[0]=='w':
                    break
                elif obstacle[0]=='b':
                    if obstacle.rstrip()!='bking':
                        moves.append([i,y])
                    else:
                        checks+=1
                    break
    return moves,checks
def move_generator_knight(loc):
    piece=board[loc[0]][loc[1]]
    x=loc[0]
    y=loc[1]
    moves=[]
    checks=0
    if piece[0]=='b':
        if x+2<8 and y+1<8:
            obstacle=board[x+2][y+1]
            if obstacle.rstrip()=='0':
                moves.append([x+2,y+1])
            elif obstacle[0]=='w':
                if obstacle[1::].rstrip()!='king':
                    moves.append([x+2,y+1])
                else:
                    checks+=1

        if x+2<8 and y-1>=0:
            obstacle=board[x+2][y-1]
            if obstacle.rstrip()=='0':
                moves.append([x+2,y-1])
            elif obstacle[0]=='w':
                if obstacle[1::].rstrip()!='king':
                    moves.append([x+2,y-1])
                else:
                    checks+=1
        if x-2>=0 and y+1<8:
            obstacle=board[x-2][y+1]
            if obstacle.rstrip()=='0':
                moves.append([x-2,y+1])
            elif obstacle[0]=='w':
                if obstacle[1::].rstrip()!='king':
                    moves.append([x-2,y+1])
                else:
                    checks+=1
        if x-2>=0 and y-1>=0:
            obstacle=board[x-2][y-1]
            if obstacle.rstrip()=='0':
                moves.append([x-2,y-1])
            elif obstacle[0]=='w':
                if obstacle[1::].rstrip()!='king':
                    moves.append([x-2,y-1])
                else:
                    checks+=1
        if x+1<8 and y+2<8:
            obstacle=board[x+1][y+2]
            if obstacle.rstrip()=='0':
                moves.append([x+1,y+2])
            elif obstacle[0]=='w':
                if obstacle[1::].rstrip()!='king':
                    moves.append([x+1,y+2])
                else:
                    checks+=1
        if x+1<8 and y-2>=0:
            obstacle=board[x+1][y-2]
            if obstacle.rstrip()=='0':
                moves.append([x+1,y-2])
            elif obstacle[0]=='w':
                if obstacle[1::].rstrip()!='king':
                    moves.append([x+1,y-2])
                else:
                    checks+=1
        if x-1>=0 and y+2<8:
            obstacle=board[x-1][y+2]
            if obstacle.rstrip()=='0':
                moves.append([x-1,y+2])
            elif obstacle[0]=='w':
                if obstacle[1::].rstrip()!='king':
                    moves.append([x-1,y+2])
                else:
                    checks+=1
        if x-1>=0 and y-2>=0:
            obstacle=board[x-1][y-2]
            if obstacle.rstrip()=='0':
                moves.append([x-1,y-2])
            elif obstacle[0]=='w':
                if obstacle[1::].rstrip()!='king':
                    moves.append([x-1,y-2])
                else:
                    checks+=1
    elif piece[0]=='w':
        if x+2<8 and y+1<8:
            obstacle=board[x+2][y+1]
            if obstacle.rstrip()=='0':
                moves.append([x+2,y+1])
            elif obstacle[0]=='b':
                if obstacle[1::].rstrip()!='king':
                    moves.append([x+2,y+1])
                else:
                    checks+=1
        if x+2<8 and y-1>=0:
            obstacle=board[x+2][y-1]
            if obstacle.rstrip()=='0':
                moves.append([x+2,y-1])
            elif obstacle[0]=='b':
                if obstacle[1::].rstrip()!='king':
                    moves.append([x+2,y-1])
                else:
                    checks+=1
        if x-2>=0 and y+1<8:
            obstacle=board[x-2][y+1]
            if obstacle.rstrip()=='0':
                moves.append([x-2,y+1])
            elif obstacle[0]=='b':
                if obstacle[1::].rstrip()!='king':
                    moves.append([x-2,y+1])
                else:
                    checks+=1
        if x-2>=0 and y-1>=0:
            obstacle=board[x-2][y-1]
            if obstacle.rstrip()=='0':
                moves.append([x-2,y-1])
            elif obstacle[0]=='b':
                if obstacle[1::].rstrip()!='king':
                    moves.append([x-2,y-1])
                else:
                    checks+=1
        if x+1<8 and y+2<8:
            obstacle=board[x+1][y+2]
            if obstacle.rstrip()=='0':
                moves.append([x+1,y+2])
            elif obstacle[0]=='b':
                if obstacle[1::].rstrip()!='king':
                    moves.append([x+1,y+2])
                else:
                    checks+=1
        if x+1<8 and y-2>=0:
            obstacle=board[x+1][y-2]
            if obstacle.rstrip()=='0':
                moves.append([x+1,y-2])
            elif obstacle[0]=='b':
                if obstacle[1::].rstrip()!='king':
                    moves.append([x+1,y-2])
                else:
                    checks+=1
        if x-1>=0 and y+2<8:
            obstacle=board[x-1][y+2]
            if obstacle.rstrip()=='0':
                moves.append([x-1,y+2])
            elif obstacle[0]=='b':
                if obstacle[1::].rstrip()!='king':
                    moves.append([x-1,y+2])
                else:
                    checks+=1
        if x-1>=0 and y-2>=0:
            obstacle=board[x-1][y-2]
            if obstacle.rstrip()=='0':
                moves.append([x-1,y-2])
            elif obstacle[0]=='b':
                if obstacle[1::].rstrip()!='king':
                    moves.append([x-1,y-2])
                else:
                    checks+=1
    return moves,checks
def move_generator_bishop(loc):
    piece=board[loc[0]][loc[1]]
    x=loc[0]
    y=loc[1]
    moves=[]
    checks=0
    if piece[0]=='b':
        i,j=x+1,y+1
        while True:
            if i<8 and j<8:
                if board[i][j].rstrip()=='0':
                    moves.append([i,j])
                else:
                    obstacle=board[i][j]
                    if obstacle[0]=='w':
                        if obstacle[1::].rstrip()!='king':
                            moves.append([i,j])
                        else:
                            checks+=1
                        break
                    elif obstacle[0]=='b':
                        break
                i=i+1
                j=j+1
            else:
                break
        i,j=x-1,y+1
        while True:
            if i>=0 and j<8:
                if board[i][j].rstrip()=='0':
                    moves.append([i,j])
                else:
                    obstacle=board[i][j]
                    if obstacle[0]=='w':
                        if obstacle[1::].rstrip()!='king':
                            moves.append([i,j])
                        else:
                            checks+=1
                        break
                    elif obstacle[0]=='b':
                        break
                i=i-1
                j=j+1
            else:
                break
        i,j=x-1,y-1
        while True:
            if i>=0 and j>=0:
                if board[i][j].rstrip()=='0':
                    moves.append([i,j])
                else:
                    obstacle=board[i][j]
                    if obstacle[0]=='w':
                        if obstacle[1::].rstrip()!='king':
                            moves.append([i,j])
                        else:
                            checks+=1
                        break
                    elif obstacle[0]=='b':
                        break
                i=i-1
                j=j-1
            else:
                break
        
        i,j=x+1,y-1
        while True:
            if i<8 and j>=0:
                if board[i][j].rstrip()=='0':
                    moves.append([i,j])
                else:
                    obstacle=board[i][j]
                    if obstacle[0]=='w':
                        if obstacle[1::].rstrip()!='king':
                            moves.append([i,j])
                        else:
                            checks+=1
                        break
                    elif obstacle[0]=='b':
                        break
                i=i+1
                j=j-1
            else:
                break
    if piece[0]=='w':
        i,j=x+1,y+1
        while True:
            if i<8 and j<8:
                if board[i][j].rstrip()=='0':
                    moves.append([i,j])
                else:
                    obstacle=board[i][j]
                    if obstacle[0]=='b':
                        if obstacle[1::].rstrip()!='king':
                            moves.append([i,j])
                        else:
                            checks+=1
                        break
                    elif obstacle[0]=='w':
                        break
                i=i+1
                j=j+1
            else:
                break
        i,j=x-1,y+1
        while True:
            if i>=0 and j<8:
                if board[i][j].rstrip()=='0':
                    moves.append([i,j])
                else:
                    obstacle=board[i][j]
                    if obstacle[0]=='b':
                        if obstacle[1::].rstrip()!='king':
                            moves.append([i,j])
                        else:
                            checks+=1
                        break
                    elif obstacle[0]=='w':
                        break
                i=i-1
                j=j+1
            else:
                break
        i,j=x-1,y-1
        while True:
            if i>=0 and j>=0:
                if board[i][j].rstrip()=='0':
                    moves.append([i,j])
                else:
                    obstacle=board[i][j]
                    if obstacle[0]=='b':
                        if obstacle[1::].rstrip()!='king':
                            moves.append([i,j])
                        else:
                            checks+=1
                        break
                    elif obstacle[0]=='w':
                        break
                i=i-1
                j=j-1
            else:
                break
        i,j=x+1,y-1
        while True:
            if i<8 and j>=0:
                if board[i][j].rstrip()=='0':
                    moves.append([i,j])
                else:
                    obstacle=board[i][j]
                    if obstacle[0]=='b':
                        if obstacle[1::].rstrip()!='king':
                            moves.append([i,j])
                        else:
                            checks+=1
                        break
                    elif obstacle[0]=='w':
                        break
                i=i+1
                j=j-1
            else:
                break
    return moves,checks
def move_generator_queen(loc):
    moves1,checks1=move_generator_bishop(loc)
    moves2,checks2=move_generator_rook(loc)
    moves=moves1+moves2
    checks=checks1+checks2
    return moves,checks
def move_generator_king(loc):
    piece=board[loc[0]][loc[1]]
    x=loc[0]
    y=loc[1]
    moves=[]
    checks=0
    if piece[0]=='b':
        i,j=x,y+1
        if j<8:
            if board[i][j].rstrip()=='0':
                moves.append([i,j])
            else:
                obstacle=board[i][j]
                if obstacle[0]=='w':
                    if obstacle[1::].rstrip()!='king':
                        moves.append([i,j])
                    else:
                        checks+=1
        i,j=x+1,y+1
        if i<8 and j<8:
            if board[i][j].rstrip()=='0':
                moves.append([i,j])
            else:
                obstacle=board[i][j]
                if obstacle[0]=='w':
                    if obstacle[1::].rstrip()!='king':
                        moves.append([i,j])
                    else:
                        checks+=1
        i,j=x-1,y+1
        if i>=0 and j<8:
            if board[i][j].rstrip()=='0':
                moves.append([i,j])
            else:
                obstacle=board[i][j]
                if obstacle[0]=='w':
                    if obstacle[1::].rstrip()!='king':
                        moves.append([i,j])
                    else:
                        checks+=1
        i,j=x-1,y
        if i>=0:
            if board[i][j].rstrip()=='0':
                moves.append([i,j])
            else:
                obstacle=board[i][j]
                if obstacle[0]=='w':
                    if obstacle[1::].rstrip()!='king':
                        moves.append([i,j])
                    else:
                        checks+=1
        i,j=x+1,y
        if i<8:
            if board[i][j].rstrip()=='0':
                moves.append([i,j])
            else:
                obstacle=board[i][j]
                if obstacle[0]=='w':
                    if obstacle[1::].rstrip()!='king':
                        moves.append([i,j])
                    else:
                        checks+=1
        i,j=x,y-1
        if j>=0:
            if board[i][j].rstrip()=='0':
                moves.append([i,j])
            else:
                obstacle=board[i][j]
                if obstacle[0]=='w':
                    if obstacle[1::].rstrip()!='king':
                        moves.append([i,j])
                    else:
                        checks+=1
        i,j=x-1,y-1
        if i>=0 and j>=0:
            if board[i][j].rstrip()=='0':
                moves.append([i,j])
            else:
                obstacle=board[i][j]
                if obstacle[0]=='w':
                    if obstacle[1::].rstrip()!='king':
                        moves.append([i,j])
                    else:
                        checks+=1
        i,j=x+1,y-1
        if i<8 and j>=0:
            if board[i][j].rstrip()=='0':
                moves.append([i,j])
            else:
                obstacle=board[i][j]
                if obstacle[0]=='w':
                    if obstacle[1::].rstrip()!='king':
                        moves.append([i,j])
                    else:
                        checks+=1
    elif piece[0]=='w':
        i,j=x,y+1
        if j<8:
            if board[i][j].rstrip()=='0':
                moves.append([i,j])
            else:
                obstacle=board[i][j]
                if obstacle[0]=='b':
                    if obstacle[1::].rstrip()!='king':
                        moves.append([i,j])
                    else:
                        checks+=1
        i,j=x+1,y+1
        if i<8 and j<8:
            if board[i][j].rstrip()=='0':
                moves.append([i,j])
            else:
                obstacle=board[i][j]
                if obstacle[0]=='b':
                    if obstacle[1::].rstrip()!='king':
                        moves.append([i,j])
                    else:
                        checks+=1
        i,j=x-1,y+1
        if i>=0 and j<8:
            if board[i][j].rstrip()=='0':
                moves.append([i,j])
            else:
                obstacle=board[i][j]
                if obstacle[0]=='b':
                    if obstacle[1::].rstrip()!='king':
                        moves.append([i,j])
                    else:
                        checks+=1
        i,j=x-1,y
        if i>=0:
            if board[i][j].rstrip()=='0':
                moves.append([i,j])
            else:
                obstacle=board[i][j]
                if obstacle[0]=='b':
                    if obstacle[1::].rstrip()!='king':
                        moves.append([i,j])
                    else:
                        checks+=1
        i,j=x+1,y
        if i<8:
            if board[i][j].rstrip()=='0':
                moves.append([i,j])
            else:
                obstacle=board[i][j]
                if obstacle[0]=='b':
                    if obstacle[1::].rstrip()!='king':
                        moves.append([i,j])
                    else:
                        checks+=1
        i,j=x,y-1
        if j>=0:
            if board[i][j].rstrip()=='0':
                moves.append([i,j])
            else:
                obstacle=board[i][j]
                if obstacle[0]=='b':
                    if obstacle[1::].rstrip()!='king':
                        moves.append([i,j])
                    else:
                        checks+=1
        i,j=x-1,y-1
        if i>=0 and j>=0:
            if board[i][j].rstrip()=='0':
                moves.append([i,j])
            else:
                obstacle=board[i][j]
                if obstacle[0]=='b':
                    if obstacle[1::].rstrip()!='king':
                        moves.append([i,j])
                    else:
                        checks+=1
        i,j=x+1,y-1
        if i<8 and j>=0:
            if board[i][j].rstrip()=='0':
                moves.append([i,j])
            else:
                obstacle=board[i][j]
                if obstacle[0]=='b':
                    if obstacle[1::].rstrip()!='king':
                        moves.append([i,j])
                    else:
                        checks+=1
    return moves,checks
def move_generator_pawn(loc):
    piece=board[loc[0]][loc[1]]
    x=loc[0]
    y=loc[1]
    moves=[]
    checks=0
    if piece[0]=='b':
        i,j=x+1,y
        if i<8:
            if board[i][j].rstrip()=='0':
                moves.append([i,j])
        i,j=x+2,y
        if i<8:
            if board[i-1][j].rstrip()=='0' and board[i][j].rstrip()=='0':
                moves.append([i,j])
        i,j=x+1,y+1
        if i<8 and j<8:
            if board[i][j].rstrip()!='0':
                obstacle=board[i][j]
                if obstacle[0]=='w':
                    if obstacle[1::].rstrip()!='king':
                        moves.append([i,j])
                    else:
                        checks+=1
        i,j=x+1,y-1
        if i<8 and j>=0:
            if board[i][j].rstrip()!='0':
                obstacle=board[i][j]
                if obstacle[0]=='w':
                    if obstacle[1::].rstrip()!='king':
                        moves.append([i,j])
                    else:
                        checks+=1
    if piece[0]=='w':
        i,j=x-1,y
        if i>=0:
            if board[i][j].rstrip()=='0':
                moves.append([i,j])
        i,j=x-2,y
        if i>=0:
            if board[i][j].rstrip()=='0' and board[i+1][j].rstrip()=='0':
                moves.append([i,j])
        i,j=x-1,y+1
        if i>=0 and j<8:
            if board[i][j].rstrip()!='0':
                obstacle=board[i][j]
                if obstacle[0]=='b':
                    if obstacle[1::].rstrip()!='king':
                        moves.append([i,j])
                    else:
                        checks+=1
        i,j=x-1,y-1
        if i>=0 and j>=0:
            if board[i][j].rstrip()!='0':
                obstacle=board[i][j]
                if obstacle[0]=='b':
                    if obstacle[1::].rstrip()!='king':
                        moves.append([i,j])
                    else:
                        checks+=1
    return moves,checks
def move_generator(loc):
    x=loc[0]
    y=loc[1]
    piece=board[x][y]
    if piece.rstrip()=='0':
        return 0,0
    if piece[1::].rstrip()=='rook':
        return move_generator_rook(loc)
    if piece[1::].rstrip()=='knight':
        return move_generator_knight(loc)
    if piece[1::].rstrip()=='bishop':
        return move_generator_bishop(loc)
    if piece[1::].rstrip()=='queen':
        return move_generator_queen(loc)
    if piece[1::].rstrip()=='king':
        return move_generator_king(loc)
    if piece[1::].rstrip()=='pawn':
        return move_generator_pawn(loc)

def evaluate_board():
    piece_values={'pawn':1,'bishop':3,'knight':3,'rook':5,'queen':9,'king':100}
    white_score=0
    black_score=0
    for row in board:
        for piece in row:
            if piece[0]=='b':
                black_score+=piece_values[piece[1::].rstrip()]
            elif piece[0]=='w':
                white_score+=piece_values[piece[1::].rstrip()]
    black_mobility=0
    white_mobility=0
    no_black_checks=0
    no_white_checks=0
    for i in range(8):
        for j in range(8):
            piece=board[i][j]
            moves,checks=move_generator([i,j])
            if piece[0]=='b':
                black_mobility+=len(moves)
                no_black_checks+=checks
            elif piece[0]=='w':
                white_mobility+=len(moves)
                no_white_checks+=checks
    white_score+=white_mobility+no_white_checks
    black_score+=black_mobility+no_black_checks
    return white_score-black_score


if __name__=='__main__':
    moves,checks=move_generator([5,7])
    print("The possible moves for the white knight located at [5,7]. 'X' represent the possible moves --->\n")
    for move in moves:
        x=move[0]
        y=move[1]
        if board2[x][y].rstrip()!='0':
            board2[x][y]+='X'
        else:
            board2[x][y]='X       '
    for row in board2:
        for piece in row:
            print(piece,end='  ')
        print()
    print('\n')
    value=evaluate_board()
    print("The initial configuration of the board is --->","\n")
    for row in board:
        for piece in row:
            print(piece,end='  ')
        print()
    print()
    print("Using the evaluation function, the evaluated value of this initial state is:",value)