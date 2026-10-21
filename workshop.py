import sys
from collections import Counter
filename = sys.argv[1]
pos = int(sys.argv[2])
keyword = sys.argv[3]
k_count = 0
with open(filename,"r") as f:
    lines = f.readlines()
print("Total lines:",len(lines))
counts = Counter()
for line in lines:
    fields = line.split()
    if len(fields) > pos:
        key = fields[pos]
        counts[key] += 1
    for i in fields:
        if i == keyword:
            k_count+=1
print("Top 5:")
for item, n in counts.most_common(5):
    print(item, n)
print(keyword,"Count :",k_count)