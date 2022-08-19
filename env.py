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

endX = 360
endY = 360

run = True

children = []

for i in range(10):
    children.append({'moves': [], 'fitness': 0})
    for j in range(30):
        children[i]['moves'].append(random.randint(1,4))

children = genes.test(children)
print(children)

# while run:
#     pygame.time.delay(100)
#
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             run = False
#
#
#
#     win.fill((0, 0, 0))
#     pygame.draw.rect(win, (0, 0, 255), (0, 0, width, height))
#     pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
#     pygame.draw.rect(win, (0, 255, 0), (360, 360, width, height))
#     pygame.display.update()
#
# pygame.quit()