import pygame
pygame.init()
#screen = pygame.display.set_mode((640, 480))
#screen = pygame.display.set_mode((640, 480), pygame.NOFRAME)
screen = pygame.display.set_mode((640, 480), pygame.SCALED)
pygame.display.set_caption("Test Window")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((0, 0, 255))  # Fill with blue
    pygame.display.flip()
    
pygame.quit()