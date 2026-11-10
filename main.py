import pygame
pygame.init() # It initialises pygames's modules, so they are ready to use
score_font = pygame.font.Font(None, 36)
lives_font = pygame.font.Font(None, 36) 
game_over_font = pygame.font.Font(None, 72)     
WIDTH , HEIGHT = 800, 600
Display= pygame.display.set_mode((WIDTH, HEIGHT))
player_x= 375
player_y= 500
enemy_x= 200
enemy_y= 50
enemy_speed= 150
lives = 1
bullet_x= player_x + 25 - 2.5
bullet_y= player_y - 10
player_speed= 500
bullet_speed= 500
score= 0
bullet_active= False #this line makes sure that the player can only shoot one bullet at a time
enemy_active = True
running = True
game_over = False
clock = pygame.time.Clock()
while running:
   dt = clock.tick(60) / 1000
   for event in pygame.event.get():
    if event.type == pygame.QUIT:
        running = False
   if not game_over:
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]: #we use if here instead of elif because we want to check both keys at the same time
      player_x += player_speed * dt
      player_x = min(player_x, WIDTH-50) #this line makes sure that the player doesn't go out of the screen
    if keys[pygame.K_LEFT]: #we use if here instead of elif because we want to check both keys at the same time 
      player_x -= player_speed * dt
      player_x = max(player_x, 0) #this line makes sure that the player doesn't go out of the screen
   if keys[pygame.K_SPACE] and bullet_active == False and not game_over: #this line makes sure that the player can only shoot one bullet at a time
      bullet_active = True
      bullet_x = player_x + 25 - 2.5
   if bullet_active and not game_over:
      bullet_y -= bullet_speed * dt
   if bullet_y < 0: #this line makes sure that the bullet disappears when it goes out of the screen and the player can shoot again
      bullet_active = False
      bullet_y = player_y - 10
   Display.fill((0,0,50))
   pygame.draw.rect(Display, (0,255,0),(player_x, player_y,50,30))
   if bullet_active:
      pygame.draw.rect(Display, (255,255,0), (bullet_x, bullet_y, 5, 10))
   if enemy_active:
      pygame.draw.rect(Display, (255,0,0), (enemy_x, enemy_y, 40, 30))
   if enemy_active and not game_over:
      enemy_x += enemy_speed * dt # this line makes the enemy move
   if enemy_active and not game_over and (enemy_x > WIDTH - 40 or enemy_x < 0):
      enemy_speed *= -1 
      enemy_y += 20
   if not game_over and enemy_y >= HEIGHT - 30: #this line makes sure that the enemy doesn't go out of the screen
      enemy_y = 50
      enemy_x = 200
      lives -= 1 #this line makes sure that the player loses a life when the enemy reaches the bottom of the screen
   if lives <= 0:
      game_over = True 
   enemy_x = max(min(enemy_x, WIDTH - 40), 0) #this line makes sure that the enemy doesn't go out of the screen
   enemy_rect = pygame.Rect(enemy_x, enemy_y, 40, 30)
   bullet_rect = pygame.Rect(bullet_x, bullet_y, 5, 10)
   if bullet_active and enemy_active and not game_over and bullet_rect.colliderect(enemy_rect):
      bullet_active =False 
      enemy_active = False
      score += 10
      bullet_y = player_y - 10

   if not enemy_active:
      enemy_y = 50
      enemy_x = 200
      enemy_active = True
      
   score_text = score_font.render("Score: " + str(score), True, (255,255,255))
   lives_text = lives_font.render("Lives: " + str(lives), True, (255,255,255))
   game_over_text = game_over_font.render("GAME OVER", True, (255,0,0))
   Display.blit(score_text, (10,10))
   Display.blit(lives_text, (10,40))
   if game_over== True:
    Display.blit(game_over_text, (300, 250)) 
   pygame.display.update() 
pygame.quit()


        

