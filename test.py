
from ast import *
import copy

clone = copy.deepcopy


# test = TupleType(VarDecl("p", boolType) ,'test')
# print(test)
# print_tup(test, 1)
# len_tup(test)
# print(TupleType)
k = ['Dog', 1]
test = StructType('Animal', k)
print(test)

# impl = \
#   LambdaExpr([VarDecl("p", boolType), VarDecl("q", boolType)], OrExpr(NotExpr("p"), "q"))
#
#
#
# table = [
#   resolve(CallExpr(clone(impl), [True, True])),
#   resolve(CallExpr(clone(impl), [True, False])),
#   resolve(CallExpr(clone(impl), [False, True])),
#   resolve(CallExpr(clone(impl), [False, False]))
# ]
#
# for e in table:
#   print(e)
#   print(evaluate(e))
#   reduce(e)
