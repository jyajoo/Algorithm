'''
< 상하좌우 > - refine

- 계획서에 따라 공간을 넘어가지 않도록 조건을 설정한 후, 이동시킨다.
'''

n = int(input())
plan = list(input().split())

x = y = 1
for i in plan:
    if i == "R":
        if y < n:
            y += 1
    elif i == "U":
        if x > 1:
            x -= 1
    elif i == "D":
        if x < n:
            x += 1
    elif i == "L":
        if y < 1:
            y -= 1
print(x, y)

'''
'''
n = int(input())
x = y = 1
plans = list(input().split())

# L, R, U, D
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

type = ["L", "R", "U", "D"]

for plan in plans:
    for i in range(4):
        if plan == type[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or nx > n or ny < 1 or ny > n:
        continue
    x, y = nx, ny
print(x, y)