from collections import deque, defaultdict

def max_robo_or_humans():
    n,m= map(int,input().split())
    gph= defaultdict(list)

    for i in range(m):
        u,v= map(int,input().split())
        gph[u].append(v)
        gph[v].append(u)
    clr=[-1]*(n+1)
    max_cnt=0
    def bfs(start) :
        queue = deque([start])
        clr[start]= 0
        count = [1,0]
        while queue:
            nd=queue.popleft()
            for nbr in gph[nd] :
                if clr[nbr]==-1 :
                    clr[nbr]=1-clr[nd]
                    count[clr[nbr]]+= 1
                    queue.append(nbr)
                elif clr[nbr]== clr[nd] :
                    pass                 
        return max(count)


    for i in range(1,n+1) :
        if clr[i]==-1 :
            max_cnt+= bfs(i)


    print(max_cnt)



max_robo_or_humans()
