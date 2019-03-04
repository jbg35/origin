from ast import *

# e = not (true and not false)

e0 = \
  notOp(
    andOp(
      Bool(True),
      notOp(Bool(False))))

print(e0)
e = step(e0)
print(e) # one step reduction of e
e = step(e)
print(e) # two step reduction of e
e = step(e)
print(e) # three step reduction


r = reduce(e0)
print(r)