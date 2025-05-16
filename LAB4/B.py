
N,M = map(int,input().split())
X =list(map(int,input().split()))
Y=list(map(int,input().split()))
Z =list(map(int,input().split()))
    
adj_l=[[] for x in range(N+1)]

for i in range(M):
    x =  X[i]
    y = Y[i]
    z = Z[i]
    adj_l[x].append((y,z))
    
for i in range(1,N+1):
    line= f"{i}:"
    for (v,w) in adj_l[i]:
        line += f"({v},{w})"
    print(line)

