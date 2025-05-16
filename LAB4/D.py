a,m = map(int,input().split())

x=list(map(int, input().split()))
y=list(map(int,input().split()))

deg =[0]*(a+1)

for i in range(m) :
    deg[x[i]]+=1
    deg[y[i]]+= 1

odd_c =0
for d in deg:
    if d%2 == 1 :
        odd_c+=1
if odd_c==0 or odd_c==2 :
    print("YES")

else:
    print ("NO")

