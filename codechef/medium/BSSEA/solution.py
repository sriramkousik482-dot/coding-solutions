# cook your dish here
n=int(input())
median=0
arr=list(map(int,input().split()))
mid=arr[0]+arr[n-1]//2
if mid%2==0:
    print(median)
elif median<mid:
    print(arr[n//2-1])
else:
    print("none")