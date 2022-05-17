import time
import pathlib
import random 
from heap import DumbHeap, GoodHeap
from merge import sort








h = DumbHeap()

print('----------------------------------------------------------')
print('----------------------------BAD---------------------------')
print('----------------------------------------------------------')
st = time.monotonic()
for i in range(500):
    h.insert(random.randint(0, 700000))
for i in range(500):
    h.remove_min()
et = time.monotonic() - st
print(f"{et* 1000:.2f}: ms {(et/1000)* 1000}: seconds")


gh = GoodHeap()
print('----------------------------------------------------------')
print('----------------------------Good--------------------------')
print('----------------------------------------------------------')
st = time.monotonic()
for i in range(50000):
    gh.insert(random.randint(0, 700000))
for i in range(50000):
    gh.remove_min()
et = time.monotonic() - st
print(f"{et* 1000:.2f}: ms {(et/1000)* 1000}: seconds")

print('----------------------------------------------------------')
print('----------------------------MERGE-------------------------')
print('----------------------------------------------------------')
st = time.monotonic()
merge= []
for i in range(50000):
    merge.append(random.randint(0, 700000))
sort(merge)
et = time.monotonic() - st
print(f"{et* 1000:.2f}: ms {(et/1000)* 1000}: seconds")


print('----------------------------------------------------------')
print('----------------------------INSERT------------------------')
print('----------------------------------------------------------')
st = time.monotonic()
ch2 = []
for i in range(50000):
    ch2.append(random.randint(0, 700000))
sorted(ch2)
et = time.monotonic() - st
print(f"{et* 1000:.2f}: ms {(et/1000)* 1000}: seconds")

