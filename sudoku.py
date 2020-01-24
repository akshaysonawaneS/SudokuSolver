board = [[3,4,0,0,0,7,0,2,6],
        [0,2,0,0,0,4,8,0,1],
        [0,0,1,2,0,5,0,0,0],
        [2,5,0,6,0,0,0,0,0],
        [6,8,0,9,0,0,3,4,0],
        [0,1,0,4,0,2,0,0,8],
        [1,6,0,0,8,9,0,3,0],
        [4,0,9,0,2,0,6,0,0],
        [0,0,8,7,4,6,2,0,0]]

def solvesudoku(board):

    find =  find_empty(board)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if valid(board,(row,col),i):
            board[row][col]=i

            if solvesudoku(board):
                return True

            board[row][col]=0

    return False

        
def print_board(board):
    for i in range(0,9):
        if (i%3 ==0 and i != 0):
            print("- - - - - - - - - - -")
       
        for j in range(0,9):
            if(j%3 == 0 and j !=0):
                print("|" ,end=" ")
            
            print(board[i][j], end=" ")
        
        print()

def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 0:
                return (i,j) # row and col

    return 0

# print_board(board)
def valid(board,pos,num):

    #check row
    for i in range(len(board)):
        if board[pos[0]][i] == num:
            return False
    #column
    for j in range(len(board)):
        if board[j][pos[1]] == num:
            return False

    x = pos[0]//3
    y = pos[1]//3
    for i in range(x*3,x*3+3):
        for  j in range(y*3,y*3+3):
            if board[i][j] == num:
                return False

    return  True

print_board(board)
solvesudoku(board)
print("*************************")
print_board(board)