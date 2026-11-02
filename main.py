import pygame
pygame.init() # It initialises pygames's modules, so they are ready to use
WIDTH , HEIGHT = 800, 600
Dispaly= pygame.display.set_mode((WIDTH, HEIGHT))
player_x= 375
player_y= 500
running = True
while running:
   for event in pygame.event.get():
    if event.type == pygame.QUIT:
        running = False
      
   Dispaly.fill((0,0,50))
   pygame.draw.rect(Dispaly, (0,255,0),(player_x, player_y,50,30))
   pygame.display.update()
   keys = pygame.key.get_pressed()
   if keys[pygame.K_RIGHT]:
      player_x += 1
   if keys[pygame.K_LEFT]: #we use if here instead of elif because we want to check both keys at the same time 
      player_x -= 1
pygame.quit()
        



