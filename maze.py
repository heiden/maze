import numpy as np
from collections import deque

maze = np.zeros((50, 50), dtype=np.int)
moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]
start = np.random.randint(0, 50 * 50 - 1)
xo, yo = start // 50, start % 50
walls = deque()
walls.append((xo, yo))
while len(walls) > 0:
  if len(walls) > 1:
    cur = np.random.randint(0, len(walls) - 1)
    walls[cur], walls[-1] = walls[-1], walls[cur]
  wall = walls.pop()
  if maze[wall[0]][wall[1]] != 0: continue
  count = 0
  for move in moves:
    x, y = wall[0] + move[0], wall[1] + move[1]
    if x >= 0 and x < 50 and y >= 0 and y < 50 and maze[x][y] != 0:
      count += 1
  if count > 1: continue
  for move in moves:
    x, y = wall[0] + move[0], wall[1] + move[1]
    if x >= 0 and x < 50 and y >= 0 and y < 50 and maze[x][y] == 0:
      walls.append((x, y))
  maze[wall[0]][wall[1]] = 1
h = []
for i in range(50):
  for j in range(50):
    if maze[i][j] == 0:
      count = 0
      for move in moves:
        x, y = wall[0] + move[0], wall[1] + move[1]
        if x >= 0 and x < 50 and y >= 0 and y < 50 and maze[x][y] != 0:
          count += 1
      if count > 1:
        h.append((i, j))
np.random.shuffle(h)
for i in range(len(h) // 20):
  maze[h[i][0]][h[i][1]] = 1
for row in maze:
  print(row[0], end='')
  for pos in row[1:]:
    print(" ", pos, end='', sep='')
  print()