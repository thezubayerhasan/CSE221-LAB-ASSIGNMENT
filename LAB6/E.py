import sys
from collections import deque
input = sys.stdin.readline
 
n = int(input())
g= [[] for i in range(n + 1)]


for i in range(n-1):
    u,v = map(int,input().split())
    g[u].append(v)
    g[v].append(u)
 
def bfs(start):
    dst=[-1]*(n+1)
    dst[start]=0
    q= deque([start])
    far= start

    while q:
        u = q.popleft()
        for v in g[u]:
            if dst[v]==-1:
                dst[v]=dst[u]+1
                q.append(v)
                if dst[v] > dst[far]:
                    far=v
    return far,dst[far]

 
a, _ = bfs(1)
b, d = bfs(a)


print(d)
print(a,b)