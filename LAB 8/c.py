def find(pnt, x) :

    if pnt[x] != x:
        pnt[x] = find(pnt,pnt[x])
    return pnt[x]

def union(pnt,rnk,a,b):
    root_a = find(pnt, a)
    root_b = find(pnt, b)

    if root_a != root_b:
        if rnk[root_a] < rnk[root_b]:
            root_a, root_b = root_b, root_a

        pnt[root_b] = root_a

        if rnk[root_a]== rnk[root_b] :
            rnk[root_a]+= 1

def kruskal(N,edges,skip_edge=None,force_edge=None) :
    pnt=list(range(N + 1))
    rnk=[0]*(N+1)
    tot_cst=0
    edg_used=0

    if force_edge:

        u, v, w = force_edge
        union(pnt,rnk,u,v)

        tot_cst += w
        edg_used += 1

    for edge in edges:
        u, v, w = edge
        if edge == skip_edge or edge == force_edge:
            continue

        if find(pnt,u)!=find(pnt,v):
            union(pnt,rnk,u,v)
            tot_cst += w
            edg_used += 1

    return tot_cst if edg_used == N-1 else float('inf')



def solve_second_mst():
    N, M = map(int,input().split())
    edges = []
    for _ in range(M):
        u, v, w = map(int,input().split())
        edges.append((u,v,w))
    
    edges.sort(key=lambda x:x[2])
    
    pnt = list(range(N+1))
    rnk = [0] * (N + 1)
    mst_edges = []

    mst_cost = 0
    edg_used = 0

    for u, v, w in edges:

        if find(pnt, u) != find(pnt, v):
            union(pnt, rnk, u, v)
            mst_edges.append((u, v, w))
            mst_cost += w
            edg_used += 1

    if edg_used != N - 1:
        print(-1)
        return
    

    snd_mst = float('inf')

    for skip_edge in mst_edges:

        cost = kruskal(N, edges, skip_edge)

        if cost != float('inf') and cost > mst_cost:
            snd_mst = min(snd_mst, cost)



    for u, v, w in edges:
        if (u, v, w) not in mst_edges and (v, u, w) not in mst_edges:
            cost = kruskal(N, edges, force_edge=(u, v, w))

            if cost != float('inf') and cost > mst_cost:
                snd_mst = min(snd_mst, cost)

    print(snd_mst if snd_mst != float('inf') else-1)


solve_second_mst()