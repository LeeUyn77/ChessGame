import pygame
WIDTH, HEIGHT = 640, 640
SQUARE_SIZE = WIDTH // 8
DEAD = 0
SELECT = 1
ALIVE = 2
class piece:
    def __init__(self,Type):
        self.status = ALIVE
        self.type = Type
        if Type == "bp" :
            self.side = "black"
            self.Image = pygame.transform.scale(pygame.image.load("black_pawn.png"), (SQUARE_SIZE, SQUARE_SIZE))
        elif Type == "br" :
            self.side = "black"
            self.Image = pygame.transform.scale(pygame.image.load("black_rook.png"), (SQUARE_SIZE, SQUARE_SIZE))
        elif Type == "bh" :
            self.side = "black"
            self.Image = pygame.transform.scale(pygame.image.load("black_horse.png"), (SQUARE_SIZE, SQUARE_SIZE))
        elif Type == "bb" :
            self.side = "black"
            self.Image = pygame.transform.scale(pygame.image.load("black_bishop.png"), (SQUARE_SIZE, SQUARE_SIZE))
        elif Type == "bq" :
            self.side = "black"
            self.Image = pygame.transform.scale(pygame.image.load("black_queen.png"), (SQUARE_SIZE, SQUARE_SIZE))
        elif Type == "bk" :
            self.side = "black"
            self.Image = pygame.transform.scale(pygame.image.load("black_king.png"), (SQUARE_SIZE, SQUARE_SIZE))
        elif Type == "wp" :
            self.side = "white" 
            self.Image = pygame.transform.scale(pygame.image.load("white_pawn.png"), (SQUARE_SIZE, SQUARE_SIZE))
        elif Type == "wr" :
            self.side = "white" 
            self.Image = pygame.transform.scale(pygame.image.load("white_rook.png"), (SQUARE_SIZE, SQUARE_SIZE))
        elif Type == "wh" :
            self.side = "white" 
            self.Image = pygame.transform.scale(pygame.image.load("white_horse.png"), (SQUARE_SIZE, SQUARE_SIZE))
        elif Type == "wb" :
            self.side = "white" 
            self.Image = pygame.transform.scale(pygame.image.load("white_bishop.png"), (SQUARE_SIZE, SQUARE_SIZE))
        elif Type == "wq" :
            self.side = "white" 
            self.Image = pygame.transform.scale(pygame.image.load("white_queen.png"), (SQUARE_SIZE, SQUARE_SIZE))
        elif Type == "wk" :
            self.side = "white" 
            self.Image = pygame.transform.scale(pygame.image.load("white_king.png"), (SQUARE_SIZE, SQUARE_SIZE))
    def get_image(self):
        return self.Image
    
    
    