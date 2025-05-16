import sys
import heapq

n,m,s,t = map(int,input().split())
gph=[[] for _ in range(n + 1)]

for _ in range(m) :
    u,v,w=map(int,input().split())
    gph[u].append((v,w))


def dijkstra(start) :
    dist=[float('inf')]*(n+1)
    dist[start]=0
    heap=[(0,start)]

    while heap :
        cst,nd = heapq.heappop(heap)

        if cst>dist[nd]:
            continue

        for nei, weight in gph[nd]:
            if dist[nei] > cst + weight:
                dist[nei] = cst + weight
            
                heapq.heappush(heap, (dist[nei], nei))
    return dist

dist_s= dijkstra(s)
dist_t =dijkstra(t)

min_t =float('inf')
meeting_nd= -1

for i in range(1,n+1):
    mx_tt = max(dist_s[i], dist_t[i])

    if dist_s[i] != float('inf') and dist_t[i] != float('inf'):
        if mx_tt < min_t or (mx_tt == min_t and i < meeting_nd):
            min_t=mx_tt
            meeting_nd= i

if meeting_nd == -1:
    print(-1)
else:
    print(min_t,meeting_nd)
