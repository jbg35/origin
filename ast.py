# Bool stuff
# e1 && e2
# e1 || e2
# not e1
# if e1 then e2 else
# e1 == e2

# Int stuff
# e1 + e2
# e1 - e2
# e1 * e2
# e1 / e2
# e1 % e2
# e1 == e2
# e1 != e2
# e1 > e2
# e1 < e2
# e1 >= e2
# e1 <= e2

class type:
    pass

class boolType(type):
    def __str__(self):
        return "Boolean"

class intType(type):
    def __str__(self):
        return "Integer"

 ########

class Expr(object):
    def __init__(self):
        self.type = None

class Bool(Expr):
    def __init__(self, val):
        self.value = val

    def __repr__(self):
        return "Bool ({})".format(self.value)

class andOp(Expr):

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __repr__(self):
        return "andOp({} , {})".format(self.left, self.right)

    def step_and(self):
        if isValue(self.left) and isValue(self.right):
            return Bool(self.left.value and self.right.value)

        if isReducible(self.left):
            return andOp(step(self.left), self.right)

        if isReducible(self.right):
            return andOp(self.left, step(self.right))

    def andEval(self):
        return evaluate(lhs) and evaluate(rhs)


class orOp(Expr):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __repr__(self):
        return "orOp({},{})".format(self.left, self.right)

    def step_or(self):
        if isValue(self.left) and isValue(self.right):
            return Bool(self.left.value and self.right.value)

        if isReducible(self.left):
            return orOp(step(self.left), self.right)

        if isReducible(self.right):
            return orOp(self.left, step(self.right))

    def orEval(self):
        return evaluate(lhs) or evaluate(rhs)

class notOp(Expr):
    def __init__(self, e):
        self.expr = e

    def __repr__(self):
        return "notOp({})".format(self.expr)

    def notEval(self):
        if isValue(self.expr):
            return Bool(not self.expr)

        return notOp(step(self.expr))


class ifOp(Expr):
    def __init__(self, e1, e2, e3):
        self.cond = e1
        self.true = e2
        self.false = e3

    def __str__(self):
        return "ifOp(if {} then {} else {})".format(self.e1,self.e2,self.e3)

    def step_if(self):
        if isReducible(cond):
            return notOp(step(e.cond), true, false)
        if cond.val:
            return true
        else:
            return false

    def ifEval(self):
        if evaluate(e.cond):
            return evaluate(e.true)
        else:
            return evaluate(e.false)

class int(Expr):
    def __init__(self, val):
        self.value = val

    def __str__(self):
        return str(self.value)

class addOp(Expr):
    def __init__ (self, e1, e2):
        self.lhs = e1
        self.rhs = e2

    def __str__(self):
        return "addOp({} + {})".format(self.lhs, self.rhs)

    def step_add(self):
        pass

    def addEval(self):
        return lhs + rhs

class subOp(Expr):
    def __init__ (self, e1, e2):
        self.lhs = e1
        self.rhs = e2

    def __str__(self):
        return "subOp({} - {})".format(self.lhs, self.rhs)

    def step_sub(self):
        pass

    def subEval(self):
        return lhs - rhs

class mulOp(Expr):
    def __init__ (self, e1, e2):
        self.lhs = e1
        self.rhs = e2

    def __str__(self):
        return "mulOp({} * {})".format(self.lhs, self.rhs)

    def step_mul(self):
        pass

    def mulEval(self):
        return lhs * rhs

class divOp(Expr):
    def __init__ (self, e1, e2):
        self.lhs = e1
        self.rhs = e2

    def __str__(self):
        return "divOp({} / {})".format(self.lhs, self.rhs)

    def step_div(self):
        pass

    def divEval(self):
        return lhs / rhs

class modOp(Expr):
    def __init__ (self, e1, e2):
        self.lhs = e1
        self.rhs = e2

    def __str__(self):
        return "modOp({} % {})".format(self.lhs, self.rhs)

    def step_mod(self):
        pass

    def modEval(self):
        return lhs % rhs

class eqOp(Expr):
    def __init__ (self, e1, e2):
        self.lhs = e1
        self.rhs = e2

    def __str__(self):
        return "eqOp({} == {})".format(self.lhs, self.rhs)

    def step_eq(self):
        pass

    def eqEval(self):
        return lhs == rhs

class gtOp(Expr):
    def __init__ (self, e1, e2):
        self.lhs = e1
        self.rhs = e2

    def __str__(self):
        return "subOp({} > {})".format(self.lhs, self.rhs)

    def step_gt(self):
        pass

    def gtEval(self):
        return lhs > rhs

class ltOp(Expr):
    def __init__ (self, e1, e2):
        self.lhs = e1
        self.rhs = e2

    def __str__(self):
        return "subOp({} < {})".format(self.lhs, self.rhs)

    def step_lt(self):
        pass

    def ltEval(self):
        return lhs < rhs

class gteOp(Expr):
    def __init__ (self, e1, e2):
        self.lhs = e1
        self.rhs = e2

    def __str__(self):
        return "subOp({} >= {})".format(self.lhs, self.rhs)

    def step_gte(self):
        pass

    def gteEval(self):
        return lhs >= rhs

class lteOp(Expr):
    def __init__ (self, e1, e2):
        self.lhs = e1
        self.rhs = e2

    def __str__(self):
        return "subOp({} <= {})".format(self.lhs, self.rhs)

    def step_lte(self):
        pass

    def lteEval(self):
        return lhs <= rhs

def expr(e):
    if type(x) is bool:
        return Bool()
    if type(x) is int:
        return Int()

    return x
