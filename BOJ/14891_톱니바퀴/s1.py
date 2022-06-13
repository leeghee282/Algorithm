# 14891_톱니바퀴
# 2022-06-13


def rotate_info(num, ndir):

    rot = num - 1
    l = num - 2

    rot_wheel = []
    while l >= 0:
        if wheel[rot][6] != wheel[l][2]:
            rot_wheel.append(l)
        else:
            break

        rot -= 1
        l -= 1

    rotate(rot_wheel, ndir)

    rot = num - 1
    r = num

    rot_wheel = []
    while r < 4:
        
        if wheel[rot][2] != wheel[r][6]:
            rot_wheel.append(r)
        else:
            break

        rot += 1
        r += 1

    rotate(rot_wheel, ndir)


def rotate(array, ndir):
    for w in array:
        if ndir == 1:
            tmp = wheel[w].pop(0)
            wheel[w].append(tmp)
            ndir = -1
        else:
            tmp = wheel[w].pop()
            wheel[w].insert(0, tmp)
            ndir = 1


wheel = [list(map(int, list(input().strip()))) for _ in range(4) ]

K = int(input())

for _ in range(K):
    n, d = map(int, input().split())
    rotate_info(n, d)

    rot = n - 1
    if d == 1:
        tmp = wheel[rot].pop()
        wheel[rot].insert(0, tmp)
    else:
        tmp = wheel[rot].pop(0)
        wheel[rot].append(tmp)


point = 0
plus = 1

for i in range(4):
    if wheel[i][0] == 1:
        point += plus
    plus *= 2

print(point)