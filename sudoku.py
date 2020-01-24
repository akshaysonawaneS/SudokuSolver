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

    return none

print_board(board)
# def valid(board,pos,num):
#     #check row
#     for i in range(len(board)):
#         if
