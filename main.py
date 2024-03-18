import pygame
from sys import exit
import random

# sound from pixabay

pygame.init()
screen = pygame.display.set_mode((650, 500))
pygame.display.set_caption("Snakes and ladder")
clock = pygame.time.Clock()

redsq = 1
bluesq = 1
end = 100
dieres = 0
#Hyy dhruv
turn = True
gameactive = False

sq_pos = {1: (25, 475), 2: (75, 475), 3: (125, 475), 4: (175, 475), 5: (225, 475), 6: (275, 475), 7: (325, 475),
          8: (375, 475), 9: (425, 475), 10: (475, 475), 11: (475, 425), 12: (425, 425), 13: (375, 425), 14: (325, 425),
          15: (275, 425), 16: (225, 425), 17: (175, 425), 18: (125, 425), 19: (75, 425), 20: (25, 425), 21: (25, 375),
          22: (75, 375), 23: (125, 375), 24: (175, 375), 25: (225, 375), 26: (275, 375), 27: (325, 375), 28: (375, 375),
          29: (425, 375), 30: (475, 375), 31: (475, 325), 32: (425, 325), 33: (375, 325), 34: (325, 325),
          35: (275, 325), 36: (225, 325), 37: (175, 325), 38: (125, 325), 39: (75, 325), 40: (25, 325), 41: (25, 275),
          42: (75, 275), 43: (125, 275), 44: (175, 275), 45: (225, 275), 46: (275, 275), 47: (325, 275), 48: (375, 275),
          49: (425, 275), 50: (475, 275), 51: (475, 225), 52: (425, 225), 53: (375, 225), 54: (325, 225),
          55: (275, 225), 56: (225, 225), 57: (175, 225), 58: (125, 225), 59: (75, 225), 60: (25, 225), 61: (25, 175),
          62: (75, 175), 63: (125, 175), 64: (175, 175), 65: (225, 175), 66: (275, 175), 67: (325, 175), 68: (375, 175),
          69: (425, 175), 70: (475, 175), 71: (475, 125), 72: (425, 125), 73: (375, 125), 74: (325, 125),
          75: (275, 125), 76: (225, 125), 77: (175, 125), 78: (125, 125), 79: (75, 125), 80: (25, 125), 81: (25, 75),
          82: (75, 75), 83: (125, 75), 84: (175, 75), 85: (225, 75), 86: (275, 75), 87: (325, 75), 88: (375, 75),
          89: (425, 75), 90: (475, 75), 91: (475, 25), 92: (425, 25), 93: (375, 25), 94: (325, 25), 95: (275, 25),
          96: (225, 25), 97: (175, 25), 98: (125, 25), 99: (75, 25), 100: (25, 25)}

ladderpos = {2: 38, 7: 14, 8: 31, 15: 26, 21: 42, 28: 84, 36: 44, 51: 67, 78: 98, 71: 91, 87: 94}
snakepos = {16: 6, 49: 11, 46: 25, 62: 19, 64: 60, 74: 53, 89: 68, 92: 88, 95: 75, 99: 80}

dieface = {0: "snakes and ladder assets\generaldice.png",
           1: "snakes and ladder assets\d1.png",
           2: "snakes and ladder assets\d2.png",
           3: "snakes and ladder assets\d3.png",
           4: "snakes and ladder assets\d4.png",
           5: "snakes and ladder assets\d5.png",
           6: "snakes and ladder assets\d6.png"}

snake_sound = pygame.mixer.Sound("snakes and ladder assets\snakehiss2.mp3")
ladder_sound = pygame.mixer.Sound("snakes and ladder assets\ladderclimb.mp3")
# win_sound = pygame.mixer.Sound("snakes and ladder assets\win_sound.mp3")

game_font = pygame.font.Font("snakes and ladder assets\LaoutBeautyPersonalUse-X3MjG.ttf", 10)

bg = pygame.image.load("snakes and ladder assets\snakes and ladder board.png").convert()
screen.blit(bg, (0, 0))

die_surf = pygame.image.load(dieface[dieres])
die_rect = die_surf.get_rect(center=(575, 400))
screen.blit(die_surf, die_rect)

exb = pygame.image.load("snakes and ladder assets\exitbutton.png").convert_alpha()
exb_rect = exb.get_rect(center=(575, 75))
screen.blit(exb, exb_rect)

redpiece_surf = pygame.image.load("snakes and ladder assets\Red piece.png").convert_alpha()
redpiece_rect = redpiece_surf.get_rect(center=sq_pos[redsq])
screen.blit(redpiece_surf, redpiece_rect)

bluepiece_surf = pygame.image.load("snakes and ladder assets\Blue_piece.png").convert_alpha()
bluepiece_rect = bluepiece_surf.get_rect(center=sq_pos[bluesq])
screen.blit(bluepiece_surf,bluepiece_rect)


def check_red():
    global redsq, ladderpos, snakepos, ladder_sound, snake_sound
    if redsq in ladderpos.keys():
        print("Ladder encountered by Red player")
        redsq = ladderpos[redsq]
        print(f"Red goes directly to square no. {redsq}")
        ladder_sound.play()
    if redsq in snakepos.keys():
        print("Snake encountered by Red player")
        redsq = snakepos[redsq]
        print(f"Red goes directly to square no. {redsq}")
        snake_sound.play()


def check_blue():
    global bluesq, ladder_sound, ladderpos, snakepos, snake_sound
    if bluesq in snakepos.keys():
        print("Snake encountered by Blue player")
        bluesq = snakepos[bluesq]
        print(f"Red goes directly to square no. {bluesq}")
        snake_sound.play()
    if bluesq in ladderpos.keys():
        print("Ladder encountered by Blue player")
        bluesq = ladderpos[bluesq]
        print(f"Red goes directly to square no. {bluesq}")
        ladder_sound.play()


def check_win():
    global redsq, bluesq
    if redsq == 100:
        print("Red wins")
        # win_sound.play()
        exit()
    if bluesq == 100:
        print("Blue wins")
        # win_sound.play()
        exit()
    else:
        pass

def rollred():
    global redsq, redpiece_rect, redpiece_surf, dieres, die_surf
    res = random.randint(1, 6)
    print(f"Red Rolled a {res}")
    dieres = res
    if (redsq + res <= 100):
        redsq += res
    else:
        pass
    redpiece_rect.center = sq_pos[redsq]
    die_surf = pygame.image.load(dieface[dieres])


def rollblue():
    global bluesq, bluepiece_surf, bluepiece_rect, dieres, die_surf
    res = random.randint(1, 6)
    dieres = res
    print(f"Blue Rolled a {res}")
    if (bluesq + res <= 100):
        bluesq += res
    else:
        pass
    bluepiece_rect.center = sq_pos[bluesq]
    die_surf = pygame.image.load(dieface[dieres])


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if die_rect.collidepoint(event.pos):
                if turn:
                    rollred()
                    turn = False
                elif not turn:
                    rollblue()
                    turn = True
                screen.blit(die_surf, die_rect)

        if event.type == pygame.MOUSEBUTTONDOWN:
            if exb_rect.collidepoint(event.pos):
                exit()

        check_blue()
        check_red()

    check_win()
    screen.blit(bg, (0, 0))
    screen.blit(redpiece_surf, redpiece_rect)
    screen.blit(bluepiece_surf, bluepiece_rect)
    screen.blit(die_surf, die_rect)

    pygame.display.update()
    clock.tick(24)
