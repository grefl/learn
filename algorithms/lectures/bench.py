import time
import pathlib
import random 
from heap import DumbHeap, GoodHeap








h = DumbHeap()

print('----------------------------------------------------------')
print('----------------------------BAD---------------------------')
print('----------------------------------------------------------')
st = time.monotonic()
for i in range(50000):
    h.insert(random.randint(0, 700000))
for i in range(50000):
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


