import sys
import heapq
n,m,s, d = map(int,input().split())

u=list(map(int,input().split()))
v=list(map(int,input().split()))
w=list(map(int,input().split()))

gph = [[] for _ in range(n+1)]


for i in range(m):
    gph[u[i]].append((v[i],w[i]))



distt=[float('inf')]*(n+1)
previous=[-1]*(n+1)
distt[s]=0
heap= [(0,s)]


while heap:
    cost,node = heapq.heappop(heap)
    if cost>distt[node] :
        continue

    for nbr,weight in gph[node] :
        if distt[nbr]>cost+weight :
            distt[nbr]= cost+weight
            previous[nbr]= node
            heapq.heappush(heap,(distt[nbr],nbr))

if distt[d]== float('inf'):
    print(-1)

else:
    print(distt[d])
    pth=[]
    curr= d
    while curr!= -1:
        pth.append(curr)
        curr=previous[curr]


    print(' '.join(map(str,pth[::-1])))
