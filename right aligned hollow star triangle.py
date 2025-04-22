#right aligned hollow star triangle
for i in range(1,6):
    for k in range(i,5):
        print("-",end=" ")

    for j in range(1,i+1):
        if(j==1 or i==5 or i==j):
            print("*",end=" ")
        else:
            print("?",end=" ")

    
    
    print(" ")
