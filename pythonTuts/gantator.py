"""
iterable --> __iter__ or __getitem
iterator --> __nexr__()
iteraton -->
"""

def gen(n):
    for i in range(n):
        yield  i

g = gen(4)
print(g)

# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())

s = "sachin"
itr = iter(s)
print(itr.__next__())
print(itr.__next__())
print(itr.__next__())
# for c in s:
#     print(c)
