import pygame
from sys import exit
from random import randint

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Runner")
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)
clock = pygame.time.Clock()
game_active = False


#INTRO 
HEADER = test_font.render('RUNNER', False, (64,64,64))
HEADER_SURF = HEADER.get_rect(center = (400,50))


START_TEXT = test_font.render('PRESS space TO PLAY', False, (64,64,64))
START_SURF = START_TEXT.get_rect(center = (400,300))


#WORLD 
BG_SKY = pygame.image.load('graphics/Sky.png').convert()
GROUND = pygame.image.load('graphics/ground.png').convert()
SCORE_TEXT = test_font.render('Score: ', False, (64,64,64))
SCORE_SURF = SCORE_TEXT.get_rect(center = (400,50))

#PLAYER 
PLAYER = pygame.image.load('graphics/Player/player_stand.png').convert_alpha()
PLAYER_SURF = PLAYER.get_rect(midbottom = (80, 300))


#SNAIL
SNAIL = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
SNAIL_SURF = SNAIL.get_rect(midbottom = (500, 300))


#FLY
FLY = pygame.image.load('graphics/Fly/Fly1.png').convert_alpha()
FLY_SURF = FLY.get_rect(midbottom = (100, 210))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()         

        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                game_active = False
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True


    if game_active:
        screen.blit(BG_SKY, (0,0))
        screen.blit(GROUND,(0,300))
        screen.blit(SCORE_TEXT, SCORE_SURF)

        #player
        screen.blit(PLAYER, PLAYER_SURF)

        #snail
        screen.blit(SNAIL, SNAIL_SURF)

        #fly
        screen.blit(FLY, FLY_SURF)
    else:
        screen.fill((94,129,162))
        screen.blit(HEADER, HEADER_SURF)
        screen.blit(PLAYER, (350,150))
        screen.blit(START_TEXT, START_SURF)



    pygame.display.update()
    clock.tick(60)

