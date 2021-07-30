#Question 4(JUNE LUNCHTIME)
for _ in range(int(input())):
    n=int(input())
    li=list(map(int,input( ).split( )))
    even=[]
    odd=[]
    for i in range(n):
        if li[i]%2==0:
            even.append(li[i])
        else:
            odd.append(li[i])
    even.sort()
    odd.sort(reverse=True)
    pi=[]
    for t in range(len(even)):
        pi.append(even[t])
    for j in range(len(odd)):
        pi.append(odd[j])
    print(*pi)
