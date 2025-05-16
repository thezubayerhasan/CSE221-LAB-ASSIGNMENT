def find(prn, x) :

    if prn[x] != x :
        prn[x] = find(prn,prn[x])
        
    return prn[x]


def union(prn,rnk,a,b):
    rt_a= find(prn,a)
    rt_b= find(prn,b)

    if rt_a!=rt_b:
        if rnk[rt_a] < rnk[rt_b] :
            rt_a, rt_b = rt_b, rt_a
        prn[rt_b] = rt_a

        if rnk[rt_a] == rnk[rt_b]:
            rnk[rt_a] += 1



def solve_mst():
    N,M = map(int,input().split())
    edg = []

    for _ in range(M) :
        u,v,w = map(int,input().split())
        edg.append((w, u, v))
    

    edg.sort()

    
    prn = list(range(N + 1))
    rnk = [0] * (N + 1)
    

    full_cst = 0
    edg_used = 0
    

    for w, u, v in edg:
        if find(prn, u) != find(prn, v):
            union(prn, rnk, u, v)
            full_cst += w
            edg_used += 1
            if edg_used == N - 1:
                break
    



    print(full_cst)




solve_mst()