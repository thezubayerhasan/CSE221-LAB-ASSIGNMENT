from collections import deque

def bfs(gph,st,end) :
    QUEUE= deque([(st,[st])])
    vsd =set([st])

    while QUEUE :
        nd,pth = QUEUE.popleft()
        if nd == end:
            return pth
        
        for nhbr in gph[nd]:
            if nhbr not in vsd :
                vsd.add(nhbr)

                QUEUE.append((nhbr,pth+[nhbr]))
                
    return None

def final_path():
    N,M,S,D,K = map(int,input().split())
    
    gph =[[] for i in range(N+1)]
    for i in range(M) :
        u,v = map(int,input().split())
        gph[u].append(v)
    

    p_1 = bfs(gph,S,K)
    if not p_1:
        print(-1)
        return
    
    p_2 = bfs(gph,K,D)
    if not p_2 :
        print(-1)
        return
    
    fin_path=p_1+p_2[1:]
    length=len(fin_path)-1
    
    print(length)
    print(*fin_path)

final_path()