import sys
import piece
import pygame
# Initialize Pygame
pygame.init()

# Define colors
WHITE = (255, 255, 204)
BLACK = (0, 255, 128)
RED = (255,0,0)
red_image = pygame.transform.scale(pygame.image.load("red.png"), (80, 80))
# Set the dimensions of the chessboard
WIDTH, HEIGHT = 640, 640
SQUARE_SIZE = WIDTH // 8

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess Game")

# Draw the chessboard
def draw_board():
    for row in range(8):
        for col in range(8):
            if (row + col) % 2 == 0:
                color = WHITE
            else:
                color = BLACK
            pygame.draw.rect(screen, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

# Define the initial chessboard
bp1 = piece.piece("bp")
bp2 = piece.piece("bp")
bp3 = piece.piece("bp")
bp4 = piece.piece("bp")
bp5 = piece.piece("bp")
bp6 = piece.piece("bp")
bp7 = piece.piece("bp")
bp8 = piece.piece("bp")
wp1 = piece.piece("wp")
wp2 = piece.piece("wp")
wp3 = piece.piece("wp")
wp4 = piece.piece("wp")
wp5 = piece.piece("wp")
wp6 = piece.piece("wp")
wp7 = piece.piece("wp")
wp8 = piece.piece("wp")
# Draw the chess pieces
last_piece = None
def draw_pieces(board):
    for row in range(8):
        for col in range(8):
            piece = board[row][col]
            if piece != None:
                image = piece.get_image()
                if piece.status == 1:
                    image = red_image
                screen.blit(image, pygame.Rect(col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
                image = piece.get_image()
                screen.blit(image, pygame.Rect(col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
def able_move(row,col,board):
    if board[row][col].type=="bp":
        image = pygame.transform.scale(pygame.image.load("red.png"), (80, 80))
        screen.blit(image, pygame.Rect(col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
    elif board[row][col].type=="wp":
        image = pygame.transform.scale(pygame.image.load("red.png"), (80, 80))
        screen.blit(image, pygame.Rect(col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
        
def select_pieces(row,col):
    if last_piece != None:
        last_piece.status = piece.ALIVE
    pos = 8*row+col
    if board[row][col] != None:
        print("You have select piece")
        print(pos)
        board[row][col].status = 1
        #able_move(row,col,board)

    
# Define the initial chessboard
board = [
    [None, None, None, None, None, None, None, None],
    [bp1, bp2, bp3, bp4, bp5, bp6, bp7, bp8],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [wp1, wp2, wp3, wp4, wp5, wp6, wp7, wp8],
    [None, None, None, None, None, None, None, None],
]
def update():
    draw_board()
    draw_pieces(board)
    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(580, 0, 60, 30)) 
    font = pygame.font.SysFont(None, 24) 
    text = font.render("Quit", True, WHITE) 
    screen.blit(text, (590, 10))
    
    # Update the display
update()
# Game loop
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
             running = False 
        elif event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_q: 
                running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            col = int(mouse[0]/SQUARE_SIZE)
            row = int(mouse[1]/SQUARE_SIZE)
            if 580 <= mouse[0] <= 640 and 0 <= mouse[1] <= 30:
                running = False
            else:
                select_pieces(row,col)
                last_piece = board[row][col]
                pos = 8*row+col
                image = pygame.transform.scale(pygame.image.load("red.png"), (80, 80))
                screen.blit(image, pygame.Rect(col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            update()
    mouse = pygame.mouse.get_pos()
    pygame.display.flip()
    clock.tick(10)

# Quit Pygame
pygame.quit()