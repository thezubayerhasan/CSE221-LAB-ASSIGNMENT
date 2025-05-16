import sys
import heapq


input = sys.stdin.readline


n, m, s, d = map(int, input().split())
gphh = [[] for _ in range(n)]


for _ in range(m) :
    u, v, w = map(int, input().split())
    gphh[u- 1].append((v-1,w))
    gphh[v-1].append((u-1,w))

distt = [[float('inf'), float('inf')] for _ in range(n)]

distt[s- 1][0]= 0
pq =[(0,s-1)]

while pq:
    cstt,u = heapq.heappop(pq)
    for v, w in gphh[u]:
        new_cstt = cstt+w

        if new_cstt < distt[v][0]   :
            distt[v][1] = distt[v][0]
            distt[v][0] = new_cstt
            heapq.heappush(pq, (new_cstt, v))

        elif distt[v][0]< new_cstt< distt[v][1] :
            distt[v][1] = new_cstt
            heapq.heappush(pq,(new_cstt,v))
            

res = distt[d-1][1]
print(res if res != float('inf') else-1)
