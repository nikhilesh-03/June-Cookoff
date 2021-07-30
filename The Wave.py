# Question 3 THE WAVE
n,q=map(int, input( ).split( ))
li=list(map(int,input().split( )))
li.sort()
pi=[]
for t in range(q):
    x=int(input())
    pi.append(x)

for i in range(len(pi)):
    lo=0
    hi=n-1
    ans=0
    bool=False
    while lo<=hi:
        mid=(lo+hi)//2
        if li[mid]==pi[i]:
            bool=True
            break
        elif li[mid]>pi[i]:
            hi=mid-1
            ans=mid
        else:
            lo=mid+1
            ans=lo
    if bool:
        print(0)
    elif (n-ans)%2==0:
        print("POSITIVE")
    else:
        print("NEGATIVE")
