import pygame 
import numpy as np
#from pygame.locals import *


#Intialization
pygame.init()

#Constants
width = 600
height = width 
board_rows = 3
board_columns = 3
#sq_size = height//board_rows       
line_width = height//40
bg = (255, 255, 110)
line_colour = (255, 225, 100)
cross_colour = (66, 66, 66)
cir_colour = (250,120,120)
cross_width = height//24
space = height//11 
circle_radius = height//10
circle_width = circle_radius//4

#Screen
screen = pygame.display.set_mode( (width, height) )
pygame.display.set_caption(' TIC TAC TOE')
screen.fill(bg)

#Board
board = np.zeros( (board_rows, board_columns ))

def draw_lines():
    # horizontal 1
    pygame.draw.line(screen, line_colour, (0,height//3), (width,height//3), line_width)
    # horizontal 2 
    pygame.draw.line(screen, line_colour, (0,height*2//3), (width,height*2//3), line_width)
    # vertical 1
    pygame.draw.line(screen, line_colour, (width//3,0), (width//3,height), line_width)
    # vertical 2
    pygame.draw.line(screen, line_colour, (width*2//3,0), (width*2//3,height), line_width)
    # border
    pygame.draw.line(screen, line_colour, (0,0), (0,width), 2*line_width)
    pygame.draw.line(screen, line_colour, (0,0), (height,0), 2*line_width)
    pygame.draw.line(screen, line_colour, (height,0), (height,width), 2*line_width)
    pygame.draw.line(screen, line_colour, (0,width), (height,width), 2*line_width)

def draw_fig():
    for row in range(board_rows):
        for col in range(board_columns):
            if board[row][col] == 1:
                pygame.draw.line(screen, cross_colour, (int( col*width/3 + space ), int(row*height/3+height/3 - space)), (int (col*width/3+width/3 - space),int(row*height/3 + space)), cross_width) 
                pygame.draw.line(screen, cross_colour, (int( col*width/3 + space ), int(row*height/3+space)), (int (col*width/3+width/3 - space),int(row*height/3+height/3 - space)), cross_width) 
            elif board[row][col] == 2:
                pygame.draw.circle(screen, cir_colour,(int(col*width//3 +width//3//2), int(row*height//3+height//3//2)), circle_radius, circle_width)

def mark_sq(row, col, player):
    board[row][col] = player  

def avaiable_sq(row, col,):
    return board[row][col] == 0

def board_full():
    for row in range(board_rows):
        for col in range(board_columns):
            if board[row][col] == 0:
                return False
    return True    


def vline(col, player):
    x = col * height//3 + height//2//3

    if player == 1:
        colour = cross_colour
    elif player == 2:
        colour = cir_colour
    
    pygame.draw.line(screen, colour, (x, height//30), (x, height - height//30), height//40)

def hline(row, player):
    y = row * width//3 + width//2//3

    if player == 1:
        colour = cross_colour
    elif player == 2:
        colour = cir_colour
   
    pygame.draw.line(screen, colour, (width//30, y), (width - width//30, y), width//40)

def asc_diagonal(player):
    if player == 1:
        colour = cross_colour
    elif player == 2:
        colour = cir_colour

    pygame.draw.line(screen, colour, (height//20, height - height//20), (width - height//20, height//20), height//40)

def desc_diagonal(player):
    if player == 1:
        colour = cross_colour
    elif player == 2:
        colour = cir_colour

    pygame.draw.line(screen, colour, (height//20, height//20), (width - height//20, height - height//20), height//40)

def win(player):
    #vertical check
    for col in range(board_columns):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            vline(col, player) 
            return True
    #horizontal check
    for row in range(board_rows):
        if  board[row][0] == player and board[row][1] == player and board[row][2] == player:
            hline(row, player) 
            return True
    #asc diagonal check
    if board[2][0] == player and board[1][1] == player and board[0][2] == player:        
        asc_diagonal(player)
        return True
    #desc diagonal check
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:        
        desc_diagonal(player)
        return True

    return False

def restart():
    screen.fill(bg)
    draw_lines()
    player = 1
    for row in range(board_rows):
        for col in range(board_columns):
            board[row][col] = 0


draw_lines()
player = 1
over = False
running = True

#Main loop
while running:

    #Events
    for event in pygame.event.get():
        

        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False


        if event.type == pygame.MOUSEBUTTONDOWN and not over:
            mouseX = event.pos[0] #x-coordinate
            mouseY = event.pos[1] #y-coordinate 

            clicked_row = int(mouseY // (height/3))
            clicked_col = int(mouseX // (width/3))

            if avaiable_sq(clicked_row, clicked_col):
                
                if player == 1:
                    mark_sq(clicked_row, clicked_col, 1)
                    if win(player):
                        over = True
                    player = 2
                elif player == 2:
                    mark_sq(clicked_row,clicked_col, 2)
                    if win(player):
                        over = True
                    player = 1

                draw_fig() 


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart()
                over = False

    #Update Objects
    pygame.display.update()