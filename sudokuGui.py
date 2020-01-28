import pygame, sys
from pygame.locals import *
from sudoku import find_empty,valid

FPS = 10

# Sets size of grid
WINDOWMULTIPLIER = 5 # Modify this number to change size of grid
WINDOWSIZE = 90
WINDOWWIDTH = WINDOWSIZE * WINDOWMULTIPLIER
WINDOWHEIGHT = WINDOWSIZE * WINDOWMULTIPLIER
SQUARESIZE = (WINDOWSIZE * WINDOWMULTIPLIER) // 3 # size of a 3x3 square
CELLSIZE = SQUARESIZE // 3 # Size of a cell

board = [[3,4,0,0,0,7,0,2,6],
        [0,2,0,0,0,4,8,0,1],
        [0,0,1,2,0,5,0,0,0],
        [2,5,0,6,0,0,0,0,0],
        [6,8,0,9,0,0,3,4,0],
        [0,1,0,4,0,2,0,0,8],
        [1,6,0,0,8,9,0,3,0],
        [4,0,9,0,2,0,6,0,0],
        [0,0,8,7,4,6,2,0,0]]

pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)

BLACK = (0,  0,  0)
WHITE = (255,255,255)
LIGHTGRAY = (200, 200, 200)
mousex = 18
mousey = 18

def solvesudoku(board):
    pygame.display.update()
    pygame.time.delay(300)
    find =  find_empty(board)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if valid(board,(row,col),i):
            board[row][col]=i
          #  print(str(row)+" "+str(col)+" "+ str(i))
            Disply_text(mousex + (50 * col), mousey + (50 * row), str(board[row][col]),(0,0,0))

            if solvesudoku(board):
                return True

            Disply_text(mousex + (50 * col), mousey + (50 * row), str(board[row][col]),WHITE) #for Erasing
            board[row][col]=0

    return False


def drawGrid():

    ### Draw Minor Lines
    for x in range(0, WINDOWWIDTH, CELLSIZE): # draw vertical lines
        pygame.draw.line(DISPLAYSURF, LIGHTGRAY, (x,0),(x,WINDOWHEIGHT))
    for y in range (0, WINDOWHEIGHT, CELLSIZE): # draw horizontal lines
        pygame.draw.line(DISPLAYSURF, LIGHTGRAY, (0,y), (WINDOWWIDTH, y))
    
    ### Draw Major Lines
    for x in range(0, WINDOWWIDTH, SQUARESIZE): # draw vertical lines
        pygame.draw.line(DISPLAYSURF, BLACK, (x,0),(x,WINDOWHEIGHT))
    for y in range (0, WINDOWHEIGHT, SQUARESIZE): # draw horizontal lines
        pygame.draw.line(DISPLAYSURF, BLACK, (0,y), (WINDOWWIDTH, y))

    return None

def main():
    global FPSCLOCK, DISPLAYSURF
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT))

    pygame.display.set_caption('Sudoku Solver')
    DISPLAYSURF.fill(WHITE)
    drawGrid()
    ak = 0;
    initialize(board)
    while True: #main game loop

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        if ak == 0:
            solver(board)
            ak=1

        pygame.display.update()
        FPSCLOCK.tick(FPS)

def solver(board):
    solvesudoku(board)

def Disply_text(x,y,text1,tup):
    textsurface = myfont.render(text1, True, tup)
    DISPLAYSURF.blit(textsurface, (x, y))

def initialize(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] != 0:
                Disply_text(mousex + (50 * j), mousey + (50 * i), str(board[i][j]),(0,0,255))


if __name__=='__main__':
    main()