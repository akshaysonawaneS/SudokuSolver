board = [[0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0]]
        
def print_board(board):
    for i in range(len(board)):
        if (i%3 ==0 & i != 1):
            print("- - - - - - - - - - -")
       
        for j in range(len(board)):
            if(j%3 == 0 & j !=1):
                print("|" ,end="")
            
            print(board[i][j], end=" ")
        
        print()

def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 0:
                return (i,j) # row and col

    return none

def valid(board,pos,num):
    #check row
    for i in range(len(board)):
        if 
