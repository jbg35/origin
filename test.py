from ast import *


env = {}

andexpr = andOp(Bool(1), Bool(1))
result = andexpr.evaluate(env)
assert result == 1

orexpr = orOp(Bool(1), Bool(0))
result = orexpr.evaluate(env)
assert result == 1

notexpr = notOp(Bool(1))
result = notexpr.evaluate(env)
assert result == 0

