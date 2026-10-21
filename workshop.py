import sys
from collections import Counter
filename = sys.argv[1]
pos = int(sys.argv[2])
with open(filename,"r") as f:
    lines = f.readlines()
print("Total lines:",len(lines))
counts = Counter()
for line in lines:
    fields = line.split()
    if len(fields) > pos:
        key = fields[pos]
        counts[key] += 1
print("Top 5:")
for item, n in counts.most_common(5):
    print(item, n)