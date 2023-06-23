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
            self.Image = pygame.transform.scale(pygame.image.load("black_pawn.png"), (SQUARE_SIZE, SQUARE_SIZE))
        elif Type == "br" :
            self.Image = pygame.transform.scale(pygame.image.load("black_rook.png"), (SQUARE_SIZE, SQUARE_SIZE))
        elif Type == "bh" :
            self.Image = pygame.transform.scale(pygame.image.load("black_horse.png"), (SQUARE_SIZE, SQUARE_SIZE))
        elif Type == "bb" :
            self.Image = pygame.transform.scale(pygame.image.load("black_bishop.png"), (SQUARE_SIZE, SQUARE_SIZE))
        elif Type == "bq" :
            self.Image = pygame.transform.scale(pygame.image.load("black_queen.png"), (SQUARE_SIZE, SQUARE_SIZE))
        elif Type == "bk" :
            self.Image = pygame.transform.scale(pygame.image.load("black_king.png"), (SQUARE_SIZE, SQUARE_SIZE))
        elif Type == "wp" :
            self.Image = pygame.transform.scale(pygame.image.load("white_pawn.png"), (SQUARE_SIZE, SQUARE_SIZE))
        elif Type == "wr" :
            self.Image = pygame.transform.scale(pygame.image.load("white_rook.png"), (SQUARE_SIZE, SQUARE_SIZE))
        elif Type == "wh" :
            self.Image = pygame.transform.scale(pygame.image.load("white_horse.png"), (SQUARE_SIZE, SQUARE_SIZE))
        elif Type == "wb" :
            self.Image = pygame.transform.scale(pygame.image.load("white_bishop.png"), (SQUARE_SIZE, SQUARE_SIZE))
        elif Type == "wq" :
            self.Image = pygame.transform.scale(pygame.image.load("white_queen.png"), (SQUARE_SIZE, SQUARE_SIZE))
        elif Type == "wk" :
            self.Image = pygame.transform.scale(pygame.image.load("white_king.png"), (SQUARE_SIZE, SQUARE_SIZE))
    def get_image(self):
        return self.Image
    
    
    