n,m = map(int,input().split())
x = list(map(int,input().split()))
y = list(map(int,input().split()))

diff = [0]*(n+1)  

for i in range(m):
    diff[x[i]]-=1 
    diff[y[i]]+=1 
print(' '.join(map(str,diff[1:])))









