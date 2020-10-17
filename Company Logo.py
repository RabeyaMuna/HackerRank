import math
import os
import random
import re
import sys
from collections import Counter, OrderedDict



if __name__ == '__main__':
    s = input()
    [print (*v) for v in Counter(sorted(s)).most_common(3)]
