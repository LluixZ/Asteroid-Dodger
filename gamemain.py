import pygame
import random
import math

pygame.init()

screen = pygame.display.set_mode((1280, 720))

pygame.display.set_caption("Asteroid Dodger game")

playerImg = pygame.image.load("space-shuttle.png")
playerX = 640
playerY = 360
playerX_change = 0
playerY_change = 0

def player(x,y):
    screen.blit(playerImg, (x,y))

asteroids = []
asteroidImg = pygame.image.load("asteroid.png")
spawn_time = 10000
last_spawn = pygame.time.get_ticks()
second = pygame.time.get_ticks()
def asteroid(x,y):
    screen.blit(asteroidImg, (x,y))

def create_asteroids():
    return{
        "asteroidX": random.randint(0,1280),
        "asteroidY": random.randint(0,720),
        "asteroidX_change": random.choice([-0.2,0.2]),
        "asteroidY_change": random.choice([-0.2,0.2])
    }
asteroids.append(create_asteroids())

def isCollision(asteroidX, asteroidY, playerX, playerY):
    distance = math.sqrt((math.pow(asteroidX-playerX,2)) + (math.pow(asteroidY-playerY,2)))
    if distance <50:
        return True
    else:
        return False
    
score = 0
font = pygame.font.Font("freesansbold.ttf", 30)
fontgo = pygame.font.Font("freesansbold.ttf", 60)

textX = 10
textY = 10
game_overX = 400
game_overY = 360
game_over = False

def show_score(x,y):
    text = font.render(f"Score: {score}", True, (255,255,255))
    screen.blit(text, (x,y))

def show_game_over(x,y):
    text = fontgo.render(f"Game Over! Score: {score}", True, (255,255,255))
    screen.blit(text, (x,y))

running = True
while running:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
          
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                playerX_change = -0.2
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                playerX_change = 0.2
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                playerY_change = -0.2
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                playerY_change = 0.2
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_a or event.key == pygame.K_d:
                playerX_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN or event.key == pygame.K_w or event.key == pygame.K_s:
                playerY_change = 0

    if not game_over:
        playerX += playerX_change
        playerY += playerY_change
        if playerX <=0:
            playerX = 0
        if playerX >= 1216:
            playerX = 1216
        if playerY <=0:
            playerY = 0
        if playerY >=656:
            playerY = 656
        player(playerX, playerY)

        current_time = pygame.time.get_ticks()
        if current_time - last_spawn > spawn_time:
            asteroids.append(create_asteroids())
            score += 10
            last_spawn = current_time

        for asteroid_data in asteroids:
            asteroid_data["asteroidX"] += asteroid_data["asteroidX_change"]
            asteroid_data["asteroidY"] += asteroid_data["asteroidY_change"]
            if asteroid_data["asteroidX"] <=0:
                asteroid_data["asteroidX_change"] += 0.2
            if asteroid_data["asteroidX"] >= 1216:
                asteroid_data["asteroidX_change"] += -0.2
            if asteroid_data["asteroidY"] <=0:
                asteroid_data["asteroidY_change"] += 0.2
            if asteroid_data["asteroidY"] >=656:
                asteroid_data["asteroidY_change"] += -0.2
            asteroid(asteroid_data["asteroidX"], asteroid_data["asteroidY"]) 
            collision = isCollision(asteroid_data["asteroidX"], asteroid_data["asteroidY"], playerX, playerY)
            if collision:
                game_over = True
        if current_time - second >=1000:
            score +=1
            second = current_time
        show_score(textX, textY)
    else:
        show_game_over(game_overX, game_overY)

    pygame.display.update()
    pygame.display.flip()

pygame.quit()
