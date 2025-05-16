import heapq
from collections import defaultdict,deque

def ancient_ordering(wrd):
    gph = defaultdict(set)
    in_dgr = {chr(i):0 for i in range(ord('a'),ord('z')+1)}
    l_in_wrd = set()
    
    for word in wrd :
        for ch in word:
            l_in_wrd.add(ch)

    for i in range(len(wrd)-1) :
        w1,w2 = wrd[i], wrd[i+1]
        minn_l = min(len(w1), len(w2))
        fnd_diff = False

        for j in range(minn_l) :
            if w1[j] != w2[j]:

                if w2[j] not in gph[w1[j]]:
                    gph[w1[j]].add(w2[j])
                    in_dgr[w2[j]] += 1
                fnd_diff = True

                break

        if not fnd_diff and len(w1) > len(w2) :     
            return -1
        
    

    heap = []
    for ch in l_in_wrd :
        if in_dgr[ch]==0:
            heapq.heappush(heap,ch)
    
    result=[]
    while heap :
        ch=heapq.heappop(heap)
        result.append(ch)
        for nei in sorted(gph[ch]) :

            in_dgr[nei]-=1
            if in_dgr[nei]==0 :
                heapq.heappush(heap,nei)

    
    if len(result)!=len(l_in_wrd) :
    
        return -1  
    
    return ''.join(result)

n = int(input())
wrd = [input().strip() for i in range(n)]


print(ancient_ordering(wrd))
