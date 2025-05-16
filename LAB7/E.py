import sys
import heapq

input=sys.stdin.readline

n,m = map(int,input().split())
u= list(map(int,input().split()))
v = list(map(int,input().split()))
w= list(map(int,input().split()))

gph =[[] for _ in range(n)]
for i in range(m):
    gph[u[i]-1].append((v[i]-1,w[i]))

distt = [[float('inf')]*2 for _ in range(n)]
pq= []

for to, wgt in gph[0]:
    parity = wgt % 2
    if distt[to][parity] > wgt:
        distt[to][parity] = wgt
        heapq.heappush(pq, (wgt, to, parity))

while pq:
    cstt,u,parity = heapq.heappop(pq)
    if distt[u][parity] < cstt:
        continue

    for v,wgt in gph[u]:
        new_parity = wgt%2

        if new_parity != parity:
            new_cstt = cstt + wgt

            if distt[v][new_parity]>new_cstt :
                distt[v][new_parity]=new_cstt
                heapq.heappush(pq, (new_cstt,v,new_parity))

res = min(distt[n-1])
print(res if res != float('inf') else-1)
