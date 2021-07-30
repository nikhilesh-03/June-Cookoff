#Quesion3(JUNE LUNCHTIME)
for t in range(int(input())):
    a=list(input())
    li=["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    if a[0]=="<" and a[1]=="/" and a[len(a)-1]==">":
        a.pop(0)
        a.pop(0)
        a.pop(len(a)-1)
        bool=True
        if len(a)==0:
            bool=False
            print("Error")
        else:
            for i in range(len(a)):
                if a[i] in li:
                    continue
                else:
                    bool=False
                    print("Error")
                    break
        if bool:
            print("Success")
    else:
        print("Error")


