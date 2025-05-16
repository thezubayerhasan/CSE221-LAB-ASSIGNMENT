import sys
input= sys.stdin.readline
 
n,r = map(int, input().split())
adj = [[] for i in range(n+1)]
for i in range(n-1):
    u,v = map(int,input().split())
    adj[u].append(v)
    adj[v].append(u)
 
sub = [0]*(n+1)
stk = [(r,0)]
ordr = []
 
while stk:
    u,p=stk.pop()
    ordr.append((u, p))
    for v in adj[u] :
        if v != p:
            stk.append((v,u))
 
for u,p in reversed(ordr):
    sub[u]= 1
    for v in adj[u]:
        if v != p:
            sub[u] += sub[v]
 
q = int(input())
out = []

for i in range(q) :
    x = int(input())
    
    out.append(str(sub[x]))
 
print('\n'.join(out))