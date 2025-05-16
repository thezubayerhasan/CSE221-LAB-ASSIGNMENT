import sys
import heapq

n,m = map(int,input().split())
gph = [[]for _ in range(n+1)]

for _ in range(m):
    u, v, w= map(int,input().split())
    gph[u].append((v, w))
    gph[v].append((u, w))

dngr = [float('inf')] * (n + 1)
dngr[1]=0
heap=[(0,1)]

while heap:
    d,node = heapq.heappop(heap)
    if d>dngr[node]:
        continue

    for nei,w in gph[node]:
        max_dngr=max(d,w)

        if max_dngr < dngr[nei]:
            dngr[nei] = max_dngr
            heapq.heappush(heap, (max_dngr, nei))

res=[]
for i in range(1,n+1):
    if dngr[i] == float('inf'):
        res.append(-1)
    else:
        res.append(dngr[i])
        
print(*res)
