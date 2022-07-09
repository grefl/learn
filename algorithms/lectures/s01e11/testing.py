from diff import diff
from pathlib import Path

a = Path('./a').read_text().split('\n')
b = Path('./b').read_text().split('\n')
print(a,b)
for i in range(len(a)):
    print(diff(a[i] + ' ', b[i] + ' ' ))
