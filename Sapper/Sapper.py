import pygame
from time import sleep
import sapper_back
import zero_pool

mine_map=sapper_back.mine_map


field = sapper_back.field

# clicks = sapper_back.clicks
# print(clicks)
clicks = []
flag_map = []
pygame.init()
wh = 499
display = pygame.display.set_mode((wh, wh))
pygame.display.set_caption('sapper')
white = (255, 255, 255)
grey = (83, 87, 83)
black = (0, 0, 0)
red = (255, 0, 17)
green = (26, 232, 84)
saddle_brown=(139, 69, 19)
# font = pygame.font.SysFont("None", 50)
# first_over_message = font.render("У сапера одно право", True, red)
# second_over_message = font.render("на ошибку", True, red)



# def game_over():
#
#     #display.blit(pygame.font.SysFont("None", 50).render(str(field[coordinate[1]][coordinate[0]]), True, green),[18 + 50 * coordinate[0], 18 + 50 * coordinate[1]])
#     for i in mine_map:
#         display.blit(pygame.font.SysFont("None", 50).render(str(field[i[1]][i[0]]), True, red),[18 + 50 * i[0], 18 + 50 * i[1]])
#     for i in range(48, 450, 50):
#         pygame.draw.rect(display, black, [i, 0, 2, wh])
#         pygame.draw.rect(display, black, [0, i, wh, 2])
#     for i in range(0, 498, 496):
#         pygame.draw.rect(display, black, [i, 0, 3, wh])
#         pygame.draw.rect(display, black, [0, i, wh, 3])
#     display.blit(pygame.font.SysFont("None", 50).render("У сапера одно право", True, red), [60, (wh // 2 )-35])
#     display.blit(pygame.font.SysFont("None", 50).render("на ошибку", True, red), [160, (wh // 2) ])
#
#
#     pygame.display.flip()
#     sleep(5)
#     exit()
def player_step(field,clicks, flag_map):
    display.fill(green)
    clicks.sort()
    for flag in flag_map:
        pygame.draw.polygon(display, red, [[flag[0]*50+35, flag[1]*50+35],
                                           [flag[0]*50+35, flag[1]*50+5],
                                           [flag[0]*50+10, flag[1]*50+20]])
        pygame.draw.line(display, saddle_brown, [flag[0]*50+35, flag[1]*50+35], [flag[0]*50+35, flag[1]*50+45])
    for coordinate in clicks:
        pygame.draw.rect(display, saddle_brown, [50 * coordinate[0], 50 * coordinate[1], 48, 48])
        if field[coordinate[1]][coordinate[0]] != '*':
            display.blit(pygame.font.SysFont("None", 50).render(str(field[coordinate[1]][coordinate[0]]), True, green),[16 + 50 * coordinate[0], 10 + 50 * coordinate[1]])
        else:
            for i in flag_map:
                try:
                    mine_map.remove(i)
                except:
                    pass
            for i in mine_map:
                display.blit(pygame.font.SysFont("None", 50).render(str(field[i[1]][i[0]]), True, red),[18 + 50 * i[0], 18 + 50 * i[1]])
            print_sc()
            display.blit(pygame.font.SysFont("None", 50).render("У сапера одно право", True, red), [60, (wh // 2) - 35])
            display.blit(pygame.font.SysFont("None", 50).render("на ошибку", True, red), [160, (wh // 2)])
            pygame.display.flip()
            sleep(3)
            quit()

    if (len(clicks) + 10)//10 == 10:
        for i in flag_map:
            mine_map.remove(i)
        for i in mine_map:
            display.blit(pygame.font.SysFont("None", 50).render(str(field[i[1]][i[0]]), True, red),
                         [18 + 50 * i[0], 18 + 50 * i[1]])
        print_sc()
        display.blit(pygame.font.SysFont("None", 50).render("Победа!", True, red), [(wh // 2) - 70, (wh // 2) - 35])
        pygame.display.flip()
        sleep(3)
        quit()

    print_sc()
    pygame.display.flip()
# def flag_point(flag_map):
#     for flag in flag_map:
#         pygame.draw.polygon(display, red, [[flag[0]*50+35, flag[1]*50+35],
#                                            [flag[0]*50+35, flag[1]*50+5],
#                                            [flag[0]*50+10, flag[1]*50+20]])
#         pygame.draw.line(display, red,[[flag[0]*50+35, flag[1]*50+45], [flag[0]*50+35, flag[1]*50+35]])
def print_sc():
    for i in range(48, 450, 50):
        pygame.draw.rect(display, black, [i, 0, 2, wh])
        pygame.draw.rect(display, black, [0, i, wh, 2])
    for i in range(0, 498, 496):
        pygame.draw.rect(display, black, [i, 0, 3, wh])
        pygame.draw.rect(display, black, [0, i, wh, 3])
def flag_pool(flag_map, click, clicks):
    for i in clicks:
        try:
            flag_map.remove(i)
        except:
            pass
    key = True
    for i in flag_map:
        if i == ([click[0] // 50, click[1] // 50]):
            flag_map.remove([click[0] // 50, click[1] // 50])
            key = False
            break
    if len(flag_map) < 10 and key:
        flag_map.append([click[0] // 50, click[1] // 50])
    return(flag_map)




player_step(field,clicks, flag_map)

while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                click=pygame.mouse.get_pos()
                key = True
                for i in flag_map:
                    if i == ([click[0]//50, click[1]//50]):
                        key = False
                if key:
                    click_x=click[0]//50
                    click_y=click[1]//50
                    clicks.append([click_x, click_y])
                    if field[click_y][click_x] == 0:
                        field, clicks = zero_pool.zero_pool(field, clicks, click_x, click_y)
                    for i in clicks:
                        while True:
                            try:
                                clicks.remove(i)
                            except:
                                clicks.append(i)
                                break
                    player_step(field, clicks, flag_map)
            elif event.button == 3:
                click = pygame.mouse.get_pos()
                flag_pool(flag_map, click, clicks)
                player_step(field, clicks, flag_map)







