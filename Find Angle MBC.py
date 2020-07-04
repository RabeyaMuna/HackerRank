#math.atan2:Return the arc tangent of y/x in radians

import math
AB = float(input())
BC = float(input())

print(str(int(round(math.degrees(math.atan2(AB, BC)))))+'°')
