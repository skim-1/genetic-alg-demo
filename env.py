import pygame
import random
import genes

pygame.init()

win = pygame.display.set_mode((400, 400))
pygame.display.set_caption("First Game")

x = 0
y = 0
width = 40
height = 40
vel = 40

psize = 96

endX = 360
endY = 360

run = True

children = []

for i in range(psize):
    children.append({'moves': [], 'fitness': 0})
    for j in range(30):
        children[i]['moves'].append(random.randint(1,4))

gen_one = genes.test(children)

for x in range(100):
    gen_one = genes.cross(gen_one)
    # print(gen_one[-1]['fitness'])
    # print(gen_one[-1]['moves'])

# print(gen_one)

# print(gen_one[-1])
#
# gen_one[-1]['fitness'] = 0
#
# for j in range(len(gen_one[-1]['moves'])):
#     if gen_one[-1]['moves'][j] == 1:
#         y -= 40
#     if gen_one[-1]['moves'][j] == 2:
#         x += 40
#     if gen_one[-1]['moves'][j] == 3:
#         y += 40
#     if gen_one[-1]['moves'][j] == 4:
#         x -= 40
#
#     if x < 0 or x > 360 or y <= 0 or y >= 360:
#         gen_one[-1]['fitness'] -= 50
#     elif x == 360 and y == 360:
#         gen_one[-1]['fitness'] += 100
#     else:
#         gen_one[-1]['fitness'] += 10
#
#     print(str(x) + " " + str(gen_one[-1]['fitness']))
#
# print(gen_one[-1]['fitness'])
#
# x = 0
# y = 0


for i in gen_one[-1]['moves']:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    win.fill((0, 0, 0))
    pygame.draw.rect(win, (0, 0, 255), (0, 0, width, height))
    pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
    pygame.draw.rect(win, (0, 255, 0), (360, 360, width, height))
    pygame.display.update()

    print("y: " + str(y) + "\n")

    if i == 1:
        y -= 40
    elif i == 2:
        x += 40
    elif i == 3:
        y += 40
    elif i == 4:
        x -= 40

pygame.quit()
