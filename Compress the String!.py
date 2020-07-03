=======================explaination==============================
#itertools.groupby is certainly one of the trickiest itertools because it has some possible pitfalls:

#It only groups the items if their key-result is the same for successive items:

#from itertools import groupby

for key, group in groupby([1,1,1,1,5,1,1,1,1,4]):
    print(key, list(group))
# 1 [1, 1, 1, 1]
# 5 [5]
# 1 [1, 1, 1, 1]
# 4 [4]
#groups = []
#uniquekeys = []
#for k, g in groupby(data, keyfunc):
#    groups.append(list(g))      # Store group iterator as a list
  #  uniquekeys.append(k)
#So in your case, data is a list of nodes, keyfunc is where the logic of your criteria function goes and then groupby() groups the data.
#You must be careful to sort the data by the criteria before you call groupby or it won't work. groupby method actually just iterates through a list and whenever the key changes it creates a new group.


============================================Solution=========================================
from itertools import groupby

print(*[(len(list(c)), int(k)) for k, c in groupby(input())])
