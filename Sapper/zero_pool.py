# import copy
#
#
# def zero_pool(field, clicks, click_x, click_y):
#     def radius(x, y):
#
#         if y - 1 >= 0 and x - 1 >= 0:
#             open_space.append([x - 1, y - 1])
#
#         if y - 1 >= 0:
#             open_space.append([x, y - 1])
#
#         if y - 1 >= 0 and x + 1 <= 9:
#             open_space.append([x + 1, y - 1])
#
#         if x - 1 >= 0:
#             open_space.append([x - 1, y])
#
#         if x + 1 <= 9:
#             open_space.append([x + 1, y])
#
#         if y + 1 <= 9 and x - 1 >= 0:
#             open_space.append([x - 1, y + 1])
#
#         if y + 1 <= 9:
#             open_space.append([x, y + 1])
#
#         if y + 1 <= 9 and x + 1 <= 9:
#             open_space.append([x + 1, y + 1])
#
#     key = True
#     click=[[click_x,click_y]]
#     while key:
#         for xy in click:
#             x, y = xy
#             key = False
#
#             if y - 1 >= 0 and x - 1 >= 0 and field[y - 1][x - 1] == 0:
#                 click.append([x - 1, y - 1])
#                 field[y - 1][x - 1] = ''
#
#                 key = True
#
#             if y - 1 >= 0 and field[y - 1][x] == 0:
#                 click.append([x, y - 1])
#                 field[y - 1][x] = ''
#                 key = True
#
#             if y - 1 >= 0 and x + 1 <= 9 and field[y - 1][x + 1] == 0:
#                 click.append([x + 1, y - 1])
#                 field[y - 1][x + 1] = ''
#                 key = True
#
#             if x - 1 >= 0 and field[y][x - 1] == 0:
#                 click.append([x - 1, y])
#                 field[y][x - 1] = ''
#                 key = True
#
#             if x + 1 <= 9 and field[y][x + 1] == 0:
#                 click.append([x + 1, y])
#                 field[y][x + 1] = ''
#                 key = True
#
#             if x - 1 >= 0 and y + 1 <= 9 and field[y + 1][x - 1] == 0:
#                 click.append([x - 1, y + 1])
#                 field[y + 1][x - 1] = ''
#                 key = True
#
#             if y + 1 <= 9 and field[y + 1][x] == 0:
#                 click.append([x, y + 1])
#                 field[y + 1][x] = ''
#                 key = True
#
#             if y + 1 <= 9 and x + 1 <= 9 and field[y + 1][x + 1] == 0:
#                 click.append([x + 1, y + 1])
#                 field[y + 1][x + 1] = ''
#                 key = True
#
#     open_space=copy.deepcopy(click)
#     for yx in click:
#         x, y = yx
#         radius(x, y)
#
#     free_space = []
#     while open_space != []:
#         free_space.append(open_space[0])
#         while True:
#             try:
#                 open_space.remove(free_space[-1])
#             except:
#                 break
#     clicks+=free_space
#
#     return (field, clicks)
def zero_pool(field, clicks, click_x, click_y):
    key = True
    click = [[click_x, click_y]]
    while key:
        key = False
        for x, y in click:
            # upper string check
            if field[y][x] == 0:
                field[y][x] = ''
                if y - 1 >= 0:
                    if x - 1 >= 0:
                        if x + 1 <= 9:
                            click += [[x - 1, y - 1], [x + 1, y - 1]]
                            key = True
                        else:
                            click += [[x - 1, y - 1]]
                            key = True
                    elif x + 1 <= 9:
                        click += [[x + 1, y - 1]]
                        key = True
                    click += [[x, y - 1]]
                    key = True
                # middle string check
                if x - 1 >= 0:
                    click += [[x - 1, y]]
                    key = True

                if x + 1 <= 9:
                    click += [[x + 1, y]]
                    key = True
                # down string check
                if y + 1 <= 9:
                    if x - 1 >= 0:
                        if x + 1 <= 9:
                            click += [[x - 1, y + 1], [x + 1, y + 1]]
                            key = True
                        else:
                            click += [[x - 1, y + 1]]
                            key = True
                    elif x + 1 <= 9:
                        click += [[x + 1, y + 1]]
                        key = True
                    click += [[x, y + 1]]
                    key = True
    # final sort
    clicks += click
    for i in clicks:
        while True:
            try:
                clicks.remove(i)
            except:
                clicks.append(i)
                break


    return(field, clicks)