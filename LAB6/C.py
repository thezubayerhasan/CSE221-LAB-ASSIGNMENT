from collections import deque
 
N= int(input())
x1,y1,x2,y2 = map(int, input().split())

mvs = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
queue= deque([(x1, y1)])

dst = [[-1]*(N+1) for i in range(N+1)]
dst[x1][y1]= 0
 
while queue:
    x,y = queue.popleft()
    for dx, dy in mvs:
        nx,ny = x+dx, y+dy
        if 1 <= nx <= N and 1 <= ny <= N and dst[nx][ny] == -1:
            dst[nx][ny] = dst[x][y]+1
            queue.append((nx,ny))

 
if dst[x2][y2]==-1 :
    print(-1)

else:
    print(dst[x2][y2])