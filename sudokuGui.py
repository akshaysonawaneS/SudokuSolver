import pygame

def main():
    win = pygame.display.set_mode((500,500))
    pygame.display.set_caption("Sudoku")
    board = Grid(9, 9, 540, 540)

main()git