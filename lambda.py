#lambda express
def make_increments(m):
    return lambda x:x+m

f = make_increments(3)
print(make_increments(3))
print(f)
print(f(10))
