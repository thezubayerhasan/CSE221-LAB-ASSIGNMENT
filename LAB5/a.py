from collections import deque

N,M=map(int,input().split())


gph=[[] for i in range(N+1)]

for i in range(M) :
    u,v=map(int,input().split())
    gph[u].append(v)
    gph[v].append(u)  

def BFS(G,s) :
    clr =[0]*(N+1)  
    Q= deque()
    
    clr[s]=1 
    Q.append(s)
    v_ord= [s]
    
    while Q :
        u =Q.popleft()
        for v in gph[u]:
            if clr[v] == 0 : 
                clr[v]= 1  
                Q.append(v)
                v_ord.append(v)
    

    return v_ord

res = BFS(gph,1)
print(" ".join(map(str,res)))
