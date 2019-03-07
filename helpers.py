from ast import *

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

    if type(e) is Bool
    return e.
