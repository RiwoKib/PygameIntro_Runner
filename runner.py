import pygame
from sys import exit
from random import randint


def display_score():
    current_time = int(pygame.time.get_ticks()/1000) - start_time
    SCORE_TEXT = test_font.render(f'Score: {current_time}', False, (64,64,64))
    SCORE_SURF = SCORE_TEXT.get_rect(center = (400,50))
    screen.blit(SCORE_TEXT, SCORE_SURF)

    return current_time

def obstacle_movement(obstacles):
    if obstacles:
        for obstacle in obstacles:
            obstacle.x -= 5

            if obstacle.bottom == 300: screen.blit(SNAIL, obstacle)
            else: screen.blit(FLY, obstacle)

        obstacles = [obstacle for obstacle in obstacles if obstacle.x > -50]
    
        return obstacles
    else: return []

def collisions(player, obstacles):
    if obstacles:
        for obstacle in obstacles:
            if player.colliderect(obstacle): return False

    return True


pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Runner")
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)
game_active = False
start_time = 0
score = 0


#INTRO 
HEADER = test_font.render('PIXEL RUNNER', False, (64,64,64))
HEADER_SURF = HEADER.get_rect(center = (400,50))
PLAYER = pygame.image.load('graphics/Player/player_stand.png').convert_alpha()
SCALE_PLAYER = pygame.transform.rotozoom(PLAYER,0,2)
SCALE_PLAYER_RECT = SCALE_PLAYER.get_rect(center = (400, 180))


START_TEXT = test_font.render('PRESS  [space] TO PLAY', False, (111, 196, 169))
START_MESSAGE_RECT = START_TEXT.get_rect(center = (400,300))


#fWORLD 
BG_SKY = pygame.image.load('graphics/Sky.png').convert()
GROUND = pygame.image.load('graphics/ground.png').convert()

#PLAYER 
PLAYER_walk1 = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
PLAYER_walk2 = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
player = [PLAYER_walk1, PLAYER_walk2]
player_index = 0
gravity = 0
PLAYER_RECT = PLAYER.get_rect(midbottom = (80, 300))


#SNAIL
SNAIL = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
SNAIL_RECT = SNAIL.get_rect(midbottom = (500, 300))
snail_x = 600

#FLY
FLY = pygame.image.load('graphics/Fly/Fly1.png').convert_alpha()
FLY_RECT = FLY.get_rect(midbottom = (100, 210))

obstacle_list = []

#TIMER 
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1500)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()         

        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAYER_RECT.collidepoint(event.pos):
                    gravity = -20

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and PLAYER_RECT.bottom >= 300:
                    gravity = -20
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                start_time = int(pygame.time.get_ticks()/1000)
        
        if event.type == obstacle_timer:
            if randint(0,1):
                obstacle_list.append(SNAIL.get_rect(midbottom = (randint(800,1100), 300)))
            else:
                obstacle_list.append(FLY.get_rect(midbottom = (randint(900,1100), 210)))
    

    if game_active:
        screen.blit(BG_SKY, (0,0))
        screen.blit(GROUND,(0,300))
        
        score = display_score()        

        #player
        gravity += 1
        PLAYER_RECT.y += gravity
        if PLAYER_RECT.bottom >= 300 : PLAYER_RECT.bottom = 300
        screen.blit(PLAYER, PLAYER_RECT)

        #snail & fly movement
        obstacle_list = obstacle_movement(obstacle_list)

        #collisions 
        game_active = collisions(PLAYER_RECT, obstacle_list)

    else:
        screen.fill((94,129,162))
        screen.blit(HEADER, HEADER_SURF)
        screen.blit(SCALE_PLAYER, SCALE_PLAYER_RECT)
        obstacle_list.clear()
        PLAYER_RECT.midbottom = (80, 300)
        gravity= 0

        score_message = test_font.render(f'Your Score: {score}', False, (111,196,169))
        score_message_rect = score_message.get_rect(center = (400,300))

        if score == 0: screen.blit(START_TEXT, START_MESSAGE_RECT)
        else: 
            screen.blit(score_message, score_message_rect)
            START_MESSAGE_RECT.y = 330
            screen.blit(START_TEXT, START_MESSAGE_RECT)

    pygame.display.update()
    clock.tick(60)

