import pygame
pygame.init() # It initialises pygames's modules, so they are ready to use
WIDTH , HEIGHT = 800, 600
Display= pygame.display.set_mode((WIDTH, HEIGHT))
player_x= 375
player_y= 500
bullet_x= player_x + 25 - 2.5
bullet_y= player_y - 10
player_speed= 500
bullet_speed= 500
bullet_active= False #this line makes sure that the player can only shoot one bullet at a time
running = True
clock = pygame.time.Clock()
while running:
   dt = clock.tick(60) / 1000
   for event in pygame.event.get():
    if event.type == pygame.QUIT:
        running = False
   keys = pygame.key.get_pressed()
   if keys[pygame.K_RIGHT]: #we use if here instead of elif because we want to check both keys at the same time
      player_x += player_speed * dt
      player_x = min(player_x, WIDTH-50) #this line makes sure that the player doesn't go out of the screen
   if keys[pygame.K_LEFT]: #we use if here instead of elif because we want to check both keys at the same time 
      player_x -= player_speed * dt
      player_x = max(player_x, 0) #this line makes sure that the player doesn't go out of the screen
   if keys[pygame.K_SPACE] and bullet_active == False: #this line makes sure that the player can only shoot one bullet at a time
      bullet_active = True
      bullet_x = player_x + 25 - 2.5
   if bullet_active:
      bullet_y -= bullet_speed * dt
   if bullet_y < 0: #this line makes sure that the bullet disappears when it goes out of the screen and the player can shoot again
      bullet_active = False
      bullet_y = player_y - 10
   Display.fill((0,0,50))
   pygame.draw.rect(Display, (0,255,0),(player_x, player_y,50,30))
   if bullet_active:
      pygame.draw.circle(Display, (255,255,0), (bullet_x, bullet_y), 5)
   pygame.display.update() 
pygame.quit()

        



