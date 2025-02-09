import pygame

pygame.init()
GREEN = (0, 255, 0)
RED = (255, 0, 0)
clock = pygame.time.Clock() 
running = True
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Bird")

while running:
    clock.tick(120)
    screen.fill(GREEN)
    
    pygame.draw.rect(screen, RED, (100, 100, 100, 100))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    pygame.display.flip()

pygame.quit()