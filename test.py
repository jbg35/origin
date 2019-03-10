from helpers import *

e = eqOp(subOp(15, 3), addOp(3,5))
print(e)
print(check(e))
e = andOp(True, False)
  
print(e)
print(check(e))

try:
  e2 = \
    eqOp(
      addOp(3, 5),
      subOp(11, True) # nope
    )
  print(e2)
  check(e2)
except Exception as err:
  print(f"error: {err}")