from collections import deque

N,M,S,D=map(int,input().split())
u_list=list(map(int,input().split()))
v_list=list(map(int,input().split()))

gph=[[] for i in range(N+1)] 

for i in range(M):
    u,v = u_list[i],v_list[i]
    gph[u].append(v)
    gph[v].append(u) 

for i in range(1,N+1) :
    gph[i].sort()


vsd= [False]*(N+1)
prn=[-1]*(N+1)
que =deque([S])

vsd[S]=True



while que:
    u = que.popleft()
    for v in gph[u] :
        if not vsd[v] :
            vsd[v] =True
            prn[v]= u
            que.append(v)



if not vsd[D] : 
    print(-1)

else:
    pth = []
    curr= D
    while curr !=-1 :
        pth.append(curr)
        curr= prn[curr]
    pth.reverse()  

    print(len(pth)-1) 
    print(" ".join(map(str,pth)))