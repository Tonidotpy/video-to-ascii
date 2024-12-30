from matplotlib import pyplot as plt
import os
import sys
import time

dir = sys.argv[1]

ascii_chars = { "@" : 0, "%" : 1, "#" : 2, "*" : 3, "+" : 4, "=" : 5, "-" : 6, ":" : 7, "." : 8, " " : 9 }

idx = []
for file in os.listdir(dir):
    with open(os.path.join(dir, file), "r") as f:
        for c in f.read():
            if c in ascii_chars:
                idx.append(ascii_chars[c])

plt.hist(idx)
plt.show()
    
