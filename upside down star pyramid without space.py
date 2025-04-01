num=4
total=2*num
for i in range(1,num+1):
    for j in range(1,i):
        print(" ",end="")
    for k in range(1,total):
        print("*",end="")
    total-=2
    
    print("")