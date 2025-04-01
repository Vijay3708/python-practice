for i in range(1,6):
    for j in range(1,i):
        print(" ",end=" ")
    x=65
    for k in range(i,6):
        print(chr(x),end=" ")
        x+=1
    
    print(" ")