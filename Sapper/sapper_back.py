from random import randint
# from copy import deepcopy
mine_map=[]
def mine_field_generation():
    mine_field=[
    [99,99,99,99,99,99,99,99,99,99,99,99],
    [99,0,0,0,0,0,0,0,0,0,0,99],
    [99,0,0,0,0,0,0,0,0,0,0,99],
    [99,0,0,0,0,0,0,0,0,0,0,99],
    [99,0,0,0,0,0,0,0,0,0,0,99],
    [99,0,0,0,0,0,0,0,0,0,0,99],
    [99,0,0,0,0,0,0,0,0,0,0,99],
    [99,0,0,0,0,0,0,0,0,0,0,99],
    [99,0,0,0,0,0,0,0,0,0,0,99],
    [99,0,0,0,0,0,0,0,0,0,0,99],
    [99,0,0,0,0,0,0,0,0,0,0,99],
    [99,99,99,99,99,99,99,99,99,99,99,99]]
    count_mine=10
    while count_mine!=0:
        for y in range(1,11):
            for x in range(1,11):
                mine=randint(0,100)
                if mine==1 and count_mine>0 and mine_field[y][x]!=9 and mine_field[y][x]!=11:
                    mine_field[y][x]=9
                    mine_map.append([x-1,y-1])
                    count_mine-=1
    field=[]
    for y in range(1,11):
            for x in range(1,11):
                if mine_field[y][x]>=9 and mine_field[y][x]<99:
                   mine_field[y-1][x-1]+=1
                   mine_field[y-1][x]+=1
                   mine_field[y-1][x+1]+=1
                   mine_field[y][x-1]+=1
                   mine_field[y][x+1]+=1
                   mine_field[y+1][x-1]+=1
                   mine_field[y+1][x]+=1
                   mine_field[y+1][x+1]+=1
    for y in range(1,11):
        for x in range(1,11):
            if mine_field[y][x]>=9:
                mine_field[y][x]='*'
    for i in range(1,11):
        field.append(mine_field[i][1:11])
    # for y in range(10):
    #     for x in range(10):
    #         if field[y][x]!='*' and field[y][x]==0:
    #             field[y][x] = ('')
    return(field)

# def hole(field):
#     click_map=[]
#     y=0
#     for x in range(10):
#         if field[y][x] == '':
#             try:
#                 if field[y][x - 1] != '*':
#                     click_map.append([x - 1, y])
#                 if field[y][x + 1] != '*':
#                     click_map.append([x + 1, y])
#                 if field[y + 1][x - 1] != '*':
#                     click_map.append([x - 1, y + 1])
#                 if field[y + 1][x] != '*':
#                     click_map.append([x, y + 1])
#                 if field[y + 1][x + 1] != '*':
#                     click_map.append([x + 1, y + 1])
#             except:
#                 continue
#
#     x=0
#     for y in range(10):
#         if field[y][x] == '':
#             try:
#                 if field[y - 1][x] != '*':
#                     click_map.append([x, y - 1])
#                 if field[y - 1][x + 1] != '*':
#                     click_map.append([x + 1, y - 1])
#                 if field[y][x + 1] != '*':
#                     click_map.append([x + 1, y])
#                 if field[y + 1][x] != '*':
#                     click_map.append([x, y + 1])
#                 if field[y + 1][x + 1] != '*':
#                     click_map.append([x + 1, y + 1])
#             except:
#                 continue
#     for y in range(1,10):
#         for x in range(1,10):
#             if field[y][x]=='':
#                 try:
#                     if field[y - 1][x - 1] != '*':
#                         click_map.append([x - 1, y - 1])
#                     if field[y - 1][x] != '*':
#                         click_map.append([x, y - 1])
#                     if field[y - 1][x + 1] != '*':
#                         click_map.append([x + 1, y - 1])
#                     if field[y][x - 1] != '*':
#                         click_map.append([x - 1, y])
#                     if field[y][x+1] != '*':
#                         click_map.append([x + 1, y])
#                     if field[y + 1][x - 1] != '*':
#                         click_map.append([x - 1, y + 1])
#                     if field[y + 1][x] != '*':
#                         click_map.append([x, y + 1])
#                     if field[y + 1][x + 1] != '*':
#                         click_map.append([x + 1, y + 1])
#                 except:
#                     continue
#
#     return(click_map)

field=mine_field_generation()
# clicks=hole(field)
# click=[]
#
# while clicks!=[]:
#     click.append(clicks[0])
#     while True:
#         try:
#             clicks.remove(click[-1])
#         except:
#             break
# clicks=click

##Режим разработчика
# print(field)
# for i in field:
#     for j in range(10):
#         if i[j] == '*':
#             i[j]=9
#     print(i)




