from ast import *

boolType = BoolType()
intType = IntType()

def isBool(x):
    if isinstance(x, Type):
        return x == boolType
    if isinstance(x, Expr):
        return isBool(check(x))

def isInt(x):
    if isinstance(x, Type):
        return x == intType
    if isinstance(x, Expr):
        return isInt(check(x))
    assert False

def is_same_type():
    if type(t1) is not type(t2):
        return False
    if type(t1) is boolType:
        return True
    if type(t2) is intType:
        return True

def sameType(e1,e2):
    return is_same_type(check(e1), check(e2))

def boolCheck(e):
    return boolType

def andCheck(e):
    if isBool(e.left) and isBool(e.right):
        return boolType
    assert False

def orCheck(e):
    if isBool(e1) and isBool(e2):
        return boolType
    assert False

def notCheck(e):
    if isBool(e1):
        return boolType
    assert False

def intCheck(e):
    return intType

def addCheck(e):
    if isInt(e.lhs) and isInt(e.rhs):
        return intType
    assert False

def subCheck(e):
    if isInt(e.lhs) and isInt(e.rhs):
        return intType
    assert False

def binaryCheck(e):
    if isInt(e.lhs) and isInt(e.rhs):
        return intType
    raise Exception("Not Cool")

def checkers(e):
    assert isinstance(e, Expr)

    if type(e) is Bool:
        return boolCheck(e)
    if type(e) is andOp:
        return andCheck(e)
    if type(e) is orOp:
        return orCheck(e)
    if type(e) is notOp:
        return notCheck(e)
    if type(e) is Int:
        return intCheck(e)
    if type(e) is addOp:
        return binaryCheck(e)
    if type(e) is subOp:
        return subCheck(e)
    if type(e) is mulOp:
        return binaryCheck(e)
    if type(e) is divOp:
        return binaryCheck(e)
    if type(e) is modOp:
        return binaryCheck(e)
    if type(e) is eqOp:
        return binaryCheck(e)
    if type(e) is gtOp:
        return binaryCheck(e)
    if type(e) is ltOp:
        return binaryCheck(e)
    if type(e) is gteOp:
        return binaryCheck(e)
    if type(e) is lteOp:
        return binaryCheck(e)

def check(e):
    if not e.type:
        e.type = checkers(e)
    return e.type

def same(e1, e2):
    if type(e1) is not type(e2):
        return False

    if type(e1) is Bool:
        return e1.value == e2.value

    if type(e1) is notOp:
        return same(e1.value, e2.value)

    if type(e1) is andOp:
        return same(e1.left, e2.left) and same(e1.right, e2.right)

    if type(e1) is orOp:
        return same(e1.left, e2.left) and same(e1.right, e2.right)

def isValue(e):
    return type(e) in (Bool, Int)

def isReducible(e):
    return not isValue(e)

def step_unary(e, Node, op):
    if is_reducible(e.expr):
        return Node(step(e.expr))
    return expr(op(e.expr.value))

def step_binary(e, Node, op):
    if is_reducible(e.lhs):
        return Node(e.lhs, step(e.rhs))
    if is_reducible(e.rhs):
        return Node(step(e.lhs), e.rhs)
    return expr(op(e.lhs.value, e.rhs.value))


def step(e):
    assert isReducible(e)

    if type(e) is notOp:
        return notOp.notEval(e)

    if type(e) is andOp:
        return andOp.step_and(e)

    if type(e) is orOp:
        return orOp.step_or(e)

    if type(e) is ifOp:
        return ifOp.step_if(e)

    if type(e) is addOp:
        return addOp.step_add(e)

def reduce(e):
    while isReducible(e):
        e = step(e)
    return e

def evaluate(e):
    assert isinstance(e, Expr)

    if type(e) is Bool:
        return e.boolEval()
    if type(e) is andOp:
        return e.andEval()
    if type(e) is orOp:
        return e.orEval()
    if type(e) is notOp:
        return e.notEval()
    if type(e) is ifOp:
        return e.ifEval()
    if type(e) is Int:
        return e.intEval()
    if type(e) is addOp:
        return e.addEval()
    if type(e) is subOp:
        return e.subEval()
    if type(e) is mulOp:
        return e.mulEval()
    if type(e) is divOp:
        return e.divEval()
    if type(e) is modOp:
        return e.modEval()
    if type(e) is gtOp:
        return e.gtEval()
    if type(e) is ltOp:
        return e.ltOp()
    if type(e) is gteop:
        return e.gteEval()
    if type(e) is lteOp:
        return e.lteOp()


