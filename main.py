import pygame
from enemy import Enemy
from player import Player
pygame.init() # It initialises pygames's modules, so they are ready to use
score_font = pygame.font.Font(None, 36)
lives_font = pygame.font.Font(None, 36) 
game_over_font = pygame.font.Font(None, 72)     
WIDTH , HEIGHT = 800, 600
Display= pygame.display.set_mode((WIDTH, HEIGHT))
player = Player(375, 500, 500) # values are x, y, speed
enemy_x_position= [100, 200, 300, 400, 500]
enemy_y_position= [50, 50, 50, 50, 50]
enemy_speed= 150
enemies = []
for i in range(5):
    enemy = Enemy(enemy_x_position[i], enemy_y_position[i], enemy_speed)
    enemies.append(enemy)
lives = 3
bullet_x= player.x + 25 - 2.5
bullet_y= player.y - 10
bullet_speed= 500
score= 0
bullet_active= False #this line makes sure that the player can only shoot one bullet at a time
running = True
game_over = False
clock = pygame.time.Clock() # this line creates a clock object that we can use to control the frame rate of the game
while running:
   dt = clock.tick(60) / 1000
   for event in pygame.event.get():
    if event.type == pygame.QUIT:
        running = False
    if event.type == pygame.KEYDOWN:
     if event.key == pygame.K_r and game_over is True:
        # Restart the game
        game_over = False
        player.x = 375
        player.y = 500
        for i in range(5):
            enemies[i].x = 100 + i * 100
            enemies[i].y = 50
            enemies[i].speed = 150
        lives = 3
        bullet_x= player.x + 25 - 2.5
        bullet_y= player.y - 10
        score= 0
        bullet_active= False #this line makes sure that the player can only shoot one bullet at a time
        for enemy in enemies:
            enemy.alive = True

   if not game_over:
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]: #we use if here instead of elif because we want to check both keys at the same time
      player.move(dt, "right", WIDTH)
    if keys[pygame.K_LEFT]: #we use if here instead of elif because we want to check both keys at the same time
      player.move(dt, "left", WIDTH)

   if keys[pygame.K_SPACE] and bullet_active == False and not game_over: #this line makes sure that the player can only shoot one bullet at a time
      bullet_active = True
      bullet_x = player.x + 25 - 2.5
      bullet_y = player.y - 10

   if bullet_active and not game_over:
      bullet_y -= bullet_speed * dt

   if bullet_y < 0: #this line makes sure that the bullet disappears when it goes out of the screen and the player can shoot again
      bullet_active = False
      bullet_y = player.y - 10
   Display.fill((0,0,50))
   pygame.draw.rect(Display, (0,255,0),(player.x, player.y,50,30))
   if bullet_active:
      pygame.draw.rect(Display, (255,255,0), (bullet_x, bullet_y, 5, 10))

   for enemy in enemies:
      if enemy.alive and not game_over:
       pygame.draw.rect(Display, (255,0,0), (enemy.x, enemy.y, 40, 30))

   for enemy in enemies:
    if enemy.alive and not game_over:
     enemy.move(dt) # this line makes the enemy move 

  # if enemy_active and not game_over and (enemy.x > WIDTH - 40 or enemy.x < 0):
    #  enemy_speed *= -1 #this line makes the enemy move in the opposite direction when it reaches the edge of the screen
     # for i in range(len(enemy.x)): 
       #  enemy.y[i] += 20 #this line makes the enemy move down when the right enemy reach 

   boundary_hit = False

   for enemy in enemies:
      if enemy.alive and (enemy.x <= 0 or enemy.x >= WIDTH - 40):
       boundary_hit = True

   if boundary_hit and not game_over:
          for enemy in enemies:
            enemy.speed *= -1
            enemy.y += 20

   for enemy in enemies:
    if not game_over and enemy.alive and enemy.y >= HEIGHT - 30: #this line makes sure that the enemy doesn't go out of the screen
      lives -= 1 #this line makes sure that the player loses a life when the enemy reaches the bottom of the screen
      for i in range(5):
       enemies[i].y = 50
       enemies[i].x = 100 + i * 100 #this resets the enemy's position to the top of the screen when it reaches the bottom
       enemies[i].alive = True #this line makes sure that the enemy is alive again when it reaches the bottom of the screen
       enemies[i].speed = enemy_speed #this line makes sure that the enemy's speed is reset to the original speed when it reaches the bottom of the screen
      break #stop the loop when the enemy reaches the bottom of the screen so that the player doesn't lose multiple lives at once

   if lives <= 0:
      game_over = True 
       
   # enemy_x_position[i] = max(min(enemy_x_position[i], WIDTH - 40), 0) #this line makes sure that the enemy doesn't go out of the screen
   bullet_rect = pygame.Rect(bullet_x, bullet_y, 5, 10) #this line creates a rectangle for the bullet so we can check for collision with the enemy
   for enemy in enemies:
      if enemy.alive and not game_over:
       enemy_rect = pygame.Rect(enemy.x, enemy.y, 40, 30)
       if bullet_active and enemy.alive and not game_over and bullet_rect.colliderect(enemy_rect):
            bullet_active =False 
            enemy.alive = False
            score += 10
            bullet_y = player.y - 10
   if not game_over and not any(enemy.alive for enemy in enemies): #this line makes sure that the player wins when all the enemies are dead
          score += 100 #this line makes sure that the player gets 100 points when all the enemies are dead
          for i in range(5):
           enemies[i].y = 50
           enemies[i].x = i * 100 + 100 #this resets the enemy's position to the top of the screen when all the enemies are dead
           enemies[i].alive = True
           enemies[i].speed = enemy_speed #this line makes sure that the enemy's speed is reset to the original speed when all the enemies are dead

   #if not enemy_active:
    #  enemy_y_position = [50, 50, 50, 50, 50]
     # enemy_x_position = [100, 200, 300, 400, 500]
      #enemy_active = True
      
   score_text = score_font.render("Score: " + str(score), True, (255,255,255))
   lives_text = lives_font.render("Lives: " + str(lives), True, (255,255,255))
   game_over_text = game_over_font.render("GAME OVER", True, (255,0,0))
   Display.blit(score_text, (10,10))
   Display.blit(lives_text, (10,40))
   if game_over== True:
    Display.blit(game_over_text, (300, 250)) 
   pygame.display.update() 
pygame.quit()


        
