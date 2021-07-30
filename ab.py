#Question2 ICPC Balloons
for i in range(int(input())):
    n=int(input())
    li=list(map(int, input().split( )))
    ci=[]
    count=0
    for j in range(len(li)):
        if 1 in ci and 2 in ci and 3 in ci and 4 in ci and 5 in ci and 6 in ci and 7 in ci:
            break
        else:
            ci.append(li[j])
            count+=1
    print(count)
    