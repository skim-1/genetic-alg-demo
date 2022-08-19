import random


def test(ch):
    for i in range(len(ch)):
        x = 0
        y = 0

        reward = 10
        for j in range(len(ch[i]['moves'])):
            if ch[i]['moves'][j] == 1:
                y -= 40
            if ch[i]['moves'][j] == 2:
                x += 40
            if ch[i]['moves'][j] == 3:
                y += 40
            if ch[i]['moves'][j] == 4:
                x -= 40

            if x < 0 or x > 360 or y < 0 or y > 360:
                ch[i]['fitness'] -= 50
                reward = 0
            elif x == 360 and y == 360:
                ch[i]['fitness'] += 100
            else:
                ch[i]['fitness'] += reward
                reward -= 0

    ch = sorted(ch, key=lambda i: i['fitness'])
    return ch


# change the values in for loops if pop size is adjusted
def cross(ch):
    c_point = int(random.random() * 30) + 1

    ch_moves = []
    chMove_final = []
    ch_final = []

    for i in ch[-48:]:
        ch_moves.append(i['moves'])
        chMove_final.append(i['moves'])

    for i in range(24):
        in_one = random.randint(0, len(ch_moves) - 1)
        in_two = random.randint(0, len(ch_moves) - 2)

        for j in range(c_point):
            if random.random() < .1:
                if random.random() < .5:
                    ch_moves[in_two][j] = random.randint(1, 4)
                else:
                    ch_moves[in_one][j] = random.randint(1, 4)
            else:
                t = ch_moves[in_two][j]
                ch_moves[in_two][j] = ch_moves[in_one][j]
                ch_moves[in_one][j] = t

        chMove_final.append(ch_moves[in_one])
        chMove_final.append(ch_moves[in_two])
        ch_moves.pop(in_one)
        ch_moves.pop(in_two)

    for i in chMove_final:
        ch_final.append({'moves': i, 'fitness': 0})
    ch_final = test(ch_final)
    return ch_final
