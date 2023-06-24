import sys
import piece
import pygame
# Initialize Pygame
pygame.init()
pygame.font.init()
# Define colors
WHITE = (255, 255, 204)
BLACK = (0, 255, 128)
RED = (255,0,0)
red_image = pygame.transform.scale(pygame.image.load("red.png"), (80, 80))
circle = pygame.transform.scale(pygame.image.load("circle.png"), (80, 80))
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
br1 = piece.piece("br")
br2 = piece.piece("br")
bh1 = piece.piece("bh")
bh2 = piece.piece("bh")
bb1 = piece.piece("bb")
bb2 = piece.piece("bb")
bq = piece.piece("bq")
bk = piece.piece("bk")

wp1 = piece.piece("wp")
wp2 = piece.piece("wp")
wp3 = piece.piece("wp")
wp4 = piece.piece("wp")
wp5 = piece.piece("wp")
wp6 = piece.piece("wp")
wp7 = piece.piece("wp")
wp8 = piece.piece("wp")
wr1 = piece.piece("wr")
wr2 = piece.piece("wr")
wh1 = piece.piece("wh")
wh2 = piece.piece("wh")
wb1 = piece.piece("wb")
wb2 = piece.piece("wb")
wq = piece.piece("wq")
wk = piece.piece("wk")
# Draw the chess pieces
move = []
selected_row = -1
selected_col = -1
turn = "white"
endgame = False
def draw_pieces(board):
    screen.blit(red_image, pygame.Rect(selected_col * SQUARE_SIZE, selected_row  * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
    for row in range(8):
        for col in range(8):
            piece = board[row][col]
            if row == selected_row and col ==selected_col and selected_row !=-1 and selected_col !=-1:
                for move_pos in move:
                    screen.blit(circle, pygame.Rect(move_pos[1] * SQUARE_SIZE, move_pos[0]  * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))                
            if piece != None:
                image = piece.get_image()
                screen.blit(image, pygame.Rect(col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
def isblock(row,col,board,side):
    return board[row][col] != None and board[row][col].side == side
def isEnermy(row,col,board,side):
    return board[row][col] != None and board[row][col].side != side
def able_move(row,col,board):
    Move = []
    piece = board[row][col]
    if piece.type=="bp":
        if row == 7:
            pass
        else:
            if not isblock(row+1,col,board,piece.side) and not isEnermy(row+1,col,board,piece.side): 
                Move.append([row+1,col])
                if row == 1 and not isblock(row+2,col,board,piece.side):
                    Move.append([row+2,col])
            if not isblock(row+1,col-1,board,piece.side) and isEnermy(row+1,col-1,board,piece.side):
                Move.append([row+1,col-1])
            if not isblock(row+1,col+1,board,piece.side) and isEnermy(row+1,col+1,board,piece.side):
                Move.append([row+1,col+1])                
    elif piece.type=="wp":
        if row == 0:
            pass
        else:
            if not isblock(row-1,col,board,piece.side) and not isEnermy(row-1,col,board,piece.side):
                Move.append([row-1,col])
                if row == 6 and not isblock(row-2,col,board,piece.side):
                    Move.append([row-2,col])
            if not isblock(row-1,col-1,board,piece.side) and isEnermy(row-1,col-1,board,piece.side):
                Move.append([row-1,col-1])
            if not isblock(row-1,col+1,board,piece.side) and isEnermy(row-1,col+1,board,piece.side):
                Move.append([row-1,col+1])         
    elif piece.type=="wr" or piece.type=="br" :
        cur_row = row
        cur_col = col
        check_time = 0
        row_check = 0
        col_check = 0
        while check_time < 4:
            if check_time == 0:
                row_check =-1
                col_check = 0
            elif check_time == 1:
                row_check = 1
                col_check = 0
            elif check_time == 2:
                row_check = 0
                col_check = -1
            elif check_time == 3:
                row_check = 0
                col_check = 1
            if not (0 <= cur_row + row_check <= 7 and 0 <= cur_col + col_check <= 7):          
                check_time +=1
                cur_row = row
                cur_col = col     
                continue
            if not isblock(cur_row+row_check,cur_col+col_check,board,piece.side):
                Move.append([cur_row+row_check,cur_col+col_check])
                cur_row += row_check
                cur_col += col_check            
                if board[cur_row][cur_col] != None and board[cur_row][cur_col].side != piece.side:
                    check_time +=1
                    cur_row = row
                    cur_col = col   
                    continue 
            else: 
                check_time +=1
                cur_row = row
                cur_col = col   
                continue 
    elif piece.type=="wb" or piece.type=="bb" :
        cur_row = row
        cur_col = col
        check_time = 0
        row_check = 0
        col_check = 0
        while check_time < 4:
            if check_time == 0:
                row_check =-1
                col_check =-1
            elif check_time == 1:
                row_check = 1
                col_check = 1
            elif check_time == 2:
                row_check = 1
                col_check = -1
            elif check_time == 3:
                row_check = -1
                col_check = 1
            if not (0 <= cur_row + row_check <= 7 and 0 <= cur_col + col_check <= 7):          
                check_time +=1
                cur_row = row
                cur_col = col     
                continue
            if not isblock(cur_row+row_check,cur_col+col_check,board,piece.side):
                Move.append([cur_row+row_check,cur_col+col_check])
                cur_row += row_check
                cur_col += col_check            
                if board[cur_row][cur_col] != None and board[cur_row][cur_col].side != piece.side:
                    check_time +=1
                    cur_row = row
                    cur_col = col   
                    continue 
            else: 
                check_time +=1
                cur_row = row
                cur_col = col   
                continue
    elif piece.type=="wh" or piece.type=="bh" :
        cur_row = row
        cur_col = col
        check_time = 0
        row_check = 0
        col_check = 0
        while check_time < 8:
            if check_time == 0:
                row_check = 1
                col_check = 2
            elif check_time == 1:
                row_check = -1
                col_check = 2
            elif check_time == 2:
                row_check = 1
                col_check = -2
            elif check_time == 3:
                row_check = -1
                col_check = -2
            elif check_time == 4:
                row_check = 2
                col_check = 1
            elif check_time == 5:
                row_check = -2
                col_check = 1
            elif check_time == 6:
                row_check = 2
                col_check = -1
            elif check_time == 7:
                row_check = -2
                col_check = -1           
            if not (0 <= cur_row + row_check <= 7 and 0 <= cur_col + col_check <= 7):          
                check_time +=1
                continue
            if not isblock(cur_row+row_check,cur_col+col_check,board,piece.side):
                Move.append([cur_row+row_check,cur_col+col_check])    
            check_time +=1 
    elif piece.type=="wq" or piece.type=="bq" :
        cur_row = row
        cur_col = col
        check_time = 0
        row_check = 0
        col_check = 0
        while check_time < 8:
            if check_time == 0:
                row_check =-1
                col_check =-1
            elif check_time == 1:
                row_check = 1
                col_check = 1
            elif check_time == 2:
                row_check = 1
                col_check = -1
            elif check_time == 3:
                row_check = -1
                col_check = 1
            elif check_time == 4:
                row_check =-1
                col_check = 0
            elif check_time == 5:
                row_check = 1
                col_check = 0
            elif check_time == 6:
                row_check = 0
                col_check = -1
            elif check_time == 7:
                row_check = 0
                col_check = 1            
            if not (0 <= cur_row + row_check <= 7 and 0 <= cur_col + col_check <= 7):          
                check_time +=1
                cur_row = row
                cur_col = col     
                continue
            if not isblock(cur_row+row_check,cur_col+col_check,board,piece.side):
                Move.append([cur_row+row_check,cur_col+col_check])
                cur_row += row_check
                cur_col += col_check            
                if board[cur_row][cur_col] != None and board[cur_row][cur_col].side != piece.side:
                    check_time +=1
                    cur_row = row
                    cur_col = col   
                    continue 
            else: 
                check_time +=1
                cur_row = row
                cur_col = col   
                continue 
    elif piece.type=="wk" or piece.type=="bk" :
        cur_row = row
        cur_col = col
        check_time = 0
        row_check = 0
        col_check = 0
        while check_time < 8:
            if check_time == 0:
                row_check = 1
                col_check = 1
            elif check_time == 1:
                row_check = -1
                col_check = 1
            elif check_time == 2:
                row_check = 1
                col_check = -1
            elif check_time == 3:
                row_check = -1
                col_check = -1
            elif check_time == 4:
                row_check = 1
                col_check = 0
            elif check_time == 5:
                row_check = 0
                col_check = 1
            elif check_time == 6:
                row_check = -1
                col_check = 0
            elif check_time == 7:
                row_check = 0
                col_check = -1       
            if not (0 <= cur_row + row_check <= 7 and 0 <= cur_col + col_check <= 7):          
                check_time +=1
                continue
            if not isblock(cur_row+row_check,cur_col+col_check,board,piece.side):
                Move.append([cur_row+row_check,cur_col+col_check])    
            check_time +=1 
    return Move
def piece_move(row,col,rowmove,colmove,board):     
    curpiece = board[row][col]
    board[row][col] = None
    board[rowmove][colmove] = curpiece    
     
    
# Define the initial chessboard

board = [
    [br1, bh1, bb1, bq, bk, bb2, bh2, br2],
    [bp1, bp2, bp3, bp4, bp5, bp6, bp7, bp8],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [wp1, wp2, wp3, wp4, wp5, wp6, wp7, wp8],
    [wr1, wh1, wb1, wk, wq, wb2, wh2, wr2],
]
def update(endgame):
    draw_board()
    draw_pieces(board)
    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(580, 0, 60, 30)) 
    font = pygame.font.SysFont(None, 24) 
    text = font.render("Quit", True, WHITE) 
    screen.blit(text, (590, 10))
    if endgame == "white":
        font = pygame.font.SysFont(None, 100) 
        text = font.render("White Win", True, RED) 
        screen.blit(text, (150, 250))
    if endgame == "black":
        font = pygame.font.SysFont(None, 100) 
        text = font.render("Black Win", True, RED) 
        screen.blit(text, (150, 250))
    # Update the display
update(endgame)
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
                moved = False
                if move != []:
                    for ablemove in move:
                        if ablemove[1] == col and ablemove[0] == row:
                            if board[row][col] !=None and board[row][col].type=="wk":
                                endgame = "black"
                            if board[row][col] !=None and board[row][col].type=="bk": 
                                endgame = "white"
                            piece_move(selected_row,selected_col,row,col,board)
                            if turn == "white":
                                turn = "black"
                            else: turn = "white"
                            move = []
                            selected_row = -1
                            selected_col = -1
                            moved = True
                            break
                if moved == False:
                    if board[row][col] == None:
                        move = []
                        selected_row = -1
                        selected_col = -1                    
                    elif board[row][col] != None and board[row][col].side == turn:
                        move = able_move(row,col,board)
                        selected_row = row
                        selected_col = col
            update(endgame)
    mouse = pygame.mouse.get_pos()
    pygame.display.flip()
    clock.tick(10)

# Quit Pygame
pygame.quit()