import pygame

pygame.init()
running = True
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Hello World")
while running:
    pygame.time.Clock().tick(120)
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((255, 255, 255))
    pygame.display.flip()
    
pygame.quit()