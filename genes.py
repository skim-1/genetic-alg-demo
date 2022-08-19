def cmp(dict1, dict2):
    return dict1['fitness'] < dict2['fitness']

def test(ch):
    for i in range(len(ch)):
        x = 0
        y = 0
        for j in range(len(ch[i]['moves'])):
            if ch[i]['moves'][j] == 1:
                y += 40
            if ch[i]['moves'][j] == 2:
                x += 40
            if ch[i]['moves'][j] == 3:
                y -= 40
            if ch[i]['moves'][j] == 4:
                x -= 10

            if x < 0 or x > 360 or y < 0 or y > 360:
                ch[i]['fitness'] -= 10
            else:
                ch[i]['fitness'] += 10
    ch.sort()
    return ch



