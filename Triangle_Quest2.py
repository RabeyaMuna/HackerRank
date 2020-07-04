#1) 10^i == 1 followed by i zeros

# pow(10,5)
#100000
# 10^i / 9 == i-1 1's followed by .1 repeating
#pow(10,5)/9
#11111.111111111111
#We could also take the floor...
#floor(pow(10,5)/9)
#11111
#Then apply the power 2 trick.
#pow(11111, 2)
#123454321
==================================Solution=============================
for i in range(1,int(input())+1): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print ((10**(i)//9)**2)
