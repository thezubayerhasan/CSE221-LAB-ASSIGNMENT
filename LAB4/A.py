N,M = map(int,input().split())

matrix =[[0]*N for i in range(N)]
for i in range(M) :
    u1,u2,w = map(int,input().split())
    matrix[u1-1][u2-1] = w

for i in range(N):
    print(" ".join(map(str,matrix[i])))

