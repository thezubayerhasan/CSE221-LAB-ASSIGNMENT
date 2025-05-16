def got_cycle(gph,nd,visited,recurr_stack) :

    visited.add(nd)
    recurr_stack.add(nd)
    
    for neighbor in gph[nd] :
        if neighbor not in visited:

            if got_cycle(gph,neighbor,visited,recurr_stack) :
                return True
            
        elif neighbor in recurr_stack:
            return True
    
    recurr_stack.remove(nd)
    return False


def cyclee():

    N,M = map(int,input().split())


    gph = [[] for i in range(N+1)]
    for i in range(M) :
        u, v = map(int,input().split())
        gph[u].append(v)


    recurr_stack= set()
    visited =set()


    for nd in range(1, N + 1) :
        if nd not in visited :
            if got_cycle(gph,nd,visited,recurr_stack) :
                print("YES")

                return


    print("NO")


cyclee()