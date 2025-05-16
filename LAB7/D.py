import heapq
import sys
input = sys.stdin.readline

n,m,s,d= map(int,input().split())
wgts = list(map(int,input().split()))
gphh = [[]for _ in range(n)]

for _ in range(m):
    u,v = map(int,input().split())
    gphh[u - 1].append(v-1)

distt = [float('inf')] * n
distt[s-1] = wgts[s-1]
pq = [(wgts[s-1], s-1)]


while pq:

    cstt,u = heapq.heappop(pq)
    if cstt > distt[u]:
        continue

    for v in gphh[u]:
        new_cstt = cstt+wgts[v]
        if new_cstt < distt[v]:
            distt[v]=new_cstt

            heapq.heappush(pq,(new_cstt,v))

print(distt[d-1] if distt[d-1] != float('inf') else -1)
