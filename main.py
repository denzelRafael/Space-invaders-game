import pygame
pygame.init() # It initialises pygames's modules, so they are ready to use
WIDTH , HEIGHT = 800, 600
Dispaly= pygame.display.set_mode((WIDTH, HEIGHT))

running = True
while running:
   Dispaly.fill((0,0,50))
   pygame.display.update()
   for event in pygame.event.get():
    if event.type == pygame.QUIT:
        running = False
pygame.quit()
        



