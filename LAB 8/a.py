def find(prt, x):
    if prt[x] != x:
        prt[x] = find(prt,prt[x])
    return prt[x]

def union(prt,sz,a,b):
    rt_a= find(prt,a)
    rt_b= find(prt,b)
    if rt_a != rt_b :
        if sz[rt_a] < sz[rt_b] :
            rt_a,rt_b = rt_b,rt_a
        prt[rt_b]= rt_a
        sz[rt_a]+=sz[rt_b]



def solve_friendship():
    N,K = map(int,input().split())
    prt= list(range(N+1))
    sz = [1]*(N+1)
    for _ in range(K):
        a,b = map(int,input().split())
        union(prt,sz,a,b)
        circle_sz=sz[find(prt,a)]
        print(circle_sz)

solve_friendship()