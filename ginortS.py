n=input()
l=list(n)
l1=[]
l2=[]
l3=[]
l4=[]
sum1=" "
for i in l:
    if i.isalpha():
        if i.islower():
            l1.append(i)
        else:
            l2.append(i)
    else:
        if int(i)%2==1:
            l3.append(i)
        else:
            l4.append(i)
        
l1.sort()
l2.sort()
l3.sort()
l4.sort()

print("".join(l1+l2+l3+l4))


