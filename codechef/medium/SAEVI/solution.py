# cook your dish here
n,k=map(int,input().split())
arr=list(map(int,input().split()))
sum=0
for i in range(0,n,2):
    if arr[i]>2*k:
        sum+=arr[i]
print(sum)