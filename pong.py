import pygame
import time

pygame.init() # initialises pygame modules

# defining colors by their RGB values

WIDTH = 800
LENGTH = 600

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0 ,0)
green = (0, 255, 0)
blue = (0, 0, 255)

def check_boundaries(x, y):
    if x <= 0 or x >= WIDTH or y <= 0 or y >= LENGTH:
        return False
    return True

gameDisplay = pygame.display.set_mode((WIDTH, LENGTH)) # the map the user will see
# 800, 600 refers to the size of the canvas, note that its a tuple, can be a list
pygame.display.set_caption('Pong') # name of the window

pygame.display.update() #updates the displ

clock = pygame.time.Clock()

smallfont = pygame.font.SysFont("comicsansms", 25) # second parameter is font size
medfont = pygame.font.SysFont("comicsansms", 50)
largefont = pygame.font.SysFont("comicsansms", 80)

def score(score1, score2):
    text = smallfont.render(str(score1) + " : " + str(score2), True, black)
    gameDisplay.blit(text, [400, 50])

def text_objects(text, colour):
    textSurface = smallfont.render(text, True, colour)
    return textSurface, textSurface.get_rect()

def message_to_screen(msg, colour):
    textSurf, textRect = text_objects(msg, colour) # textsurf refers to the surface of the message, textrect
    textRect.center = (WIDTH/2), (LENGTH/2)
    gameDisplay.blit(textSurf, textRect)


def gameLoop():

    gameExit = False
    roundOver = False
    gameOver = False

    lead_x = 300 # the first block of the snake
    lead_y = 300 
    lead_x_change = 10 # used for continuous movement
    lead_y_change = 10

    rect_x = 750
    rect_y = 300
    rect_y_change = 0

    rect_2_x = 50
    rect_2_y = 300
    rect_2_y_change = 0

    your_score = 0
    opponent_score = 0

    while gameExit != True: # basic game loop
        
        while gameOver == True:

            gameDisplay.fill(white)
            if your_score == 10:
                message_to_screen("You win", green)
            elif opponent_score == 10:
                message_to_screen("You lose", red)
 
            # time.sleep(3)

            pygame.display.update()

            gameDisplay.fill(white)
            message_to_screen("Game over, press C to play again or Q to quit", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        gameLoop() # calling game loop within game loop
                    if event.type == pygame.QUIT: # has to be referenced by timegame
                        gameExit = True
                        break
        
        if roundOver == True:
            # gameLoop()
            lead_x = 300
            lead_y = 300
            lead_x_change = 10
            lead_y_change = 10
            roundOver = False 

        for event in pygame.event.get(): #note, as you move your mouse/click, it will give you the position or the key
            if event.type == pygame.QUIT: # has to be referenced by timegame
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    rect_y_change = -10
                if event.key == pygame.K_DOWN:
                    rect_y_change = 10
                if event.key == pygame.K_SPACE: # will stop motion
                    rect_y_change = 0
                if event.key == pygame.K_w:
                    rect_2_y_change = -10
                if event.key == pygame.K_s:
                    rect_2_y_change = 10
                if event.key == pygame.K_LSHIFT: # will stop motion
                    rect_2_y_change = 0

        if check_boundaries(lead_x, lead_y) == False:
            if lead_x <= 0:
                roundOver = True
                your_score += 1
            if lead_x >= WIDTH:
                roundOver = True
                opponent_score += 1
            if lead_y <= 0 or lead_y >= LENGTH: 
                lead_y_change = -lead_y_change

        if lead_x == 740 and ((rect_y + 100) >= lead_y and lead_y >= rect_y):
             lead_x_change = -lead_x_change

        if lead_x == 60 and ((rect_2_y + 100) >= lead_y and lead_y >= rect_2_y):
             lead_x_change = -lead_x_change

        lead_x += lead_x_change 
        lead_y += lead_y_change 

        rect_y += rect_y_change
        rect_2_y += rect_2_y_change
        # rect_2_y = lead_y

        if your_score == 10 or opponent_score == 10:
            gameOver = True
    
            #elif event.type != pygame.KEYDOWN:

        gameDisplay.fill(white) # game display will now be white
        pygame.draw.rect(gameDisplay, black, [lead_x, lead_y, 10, 10]) 
        pygame.draw.rect(gameDisplay, black, [rect_x, rect_y, 10, 100])
        pygame.draw.rect(gameDisplay, black, [50, rect_2_y, 10, 100]) 
        score(opponent_score, your_score)
            # first parameter is the display, second is colour, third is [0 and 1]: place in the display, [2 and 3]: the size of the rectangle
        pygame.display.update() # we need this for the updating actions taken

        clock.tick(15) # controls frames per second, variable inside refers to the fps
        
    pygame.quit() # will unitialise pygame
    quit() 
    
gameLoop()
message_to_screen("thank you for playing :)", black) 
pygame.display.update()
time.sleep(3)
