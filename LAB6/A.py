from collections import defaultdict,deque


N,M = map(int,input().split())
gph= defaultdict(list)
in_d = [0]*(N+1)

for i in range(M) :
    A,B= map(int,input().split())
    gph[A].append(B) 
    in_d[B]+=1 
queue= deque()

for i in range(1,N+1):
    if in_d[i]==0:
        queue.append(i)

res= [] 
while queue:
    nd= queue.popleft()
    res.append(nd)
    
    for nbr in gph[nd] :
        in_d[nbr]-= 1
        if in_d[nbr]== 0 :
            queue.append(nbr)

if len(res)== N : 
    print(*res)

else:
    print(-1)