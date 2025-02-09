import pygame
import random


pygame.init()
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
background = BLUE
clock = pygame.time.Clock() 
running = True
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Bird")

while running:
    clock.tick(120)
    screen.fill(background)
    mousePos = pygame.mouse.get_pos()
    pygame.draw.rect(screen, RED, (100, 100, 100, 100))
    
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button != 1:
                break
            if mousePos[0] > 200:
                break
            if mousePos[0] < 100:
                break
            if mousePos[1] > 200:
                break
            if mousePos[1] < 100:
                break
            background = random.randint(0, 225), random.randint(0, 225), random.randint(0, 225)
            
        if event.type == pygame.QUIT:
            running = False
            
    pygame.display.flip()

pygame.quit()