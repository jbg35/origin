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

class Type:
    pass

class BoolType(Type):
    def __str__(self):
        return "T: Boolean"

class IntType(Type):
    def __str__(self):
        return "T: Integer"

 ########

class Expr:
    def __init__(self):
        self.type = None

class Bool(Expr):
    def __init__(self, val):
        Expr.__init__(self)
        self.value = val

    def __repr__(self):
        return "Bool ({})".format(self.value)

    def boolEval(self):
        return e.value

class andOp(Expr):

    def __init__(self, left, right):
        Expr.__init__(self)
        self.left = expr(left)
        self.right = expr(right)

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
        Expr.__init__(self)
        self.left = expr(left)
        self.right = expr(right)

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
        Expr.__init__(self)
        self.expr = expr(e)
    def __repr__(self):
        return "notOp({})".format(self.expr)

    def step_not(self):
        return step_unary(e, notOp, lambda x: not x)

    def notEval(self):
        return not evaluate(e.expr)


class ifOp(Expr):
    def __init__(self, e1, e2, e3):
        Expr.__init__(self)
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

class Int(Expr):
    def __init__(self, val):
        Expr.__init__(self)
        self.value = val

    def __str__(self):
        return str(self.value)

    def intEval(self):
        return e.value

class addOp(Expr):
    def __init__ (self, lhs, rhs):
        Expr.__init__(self)
        self.lhs = expr(lhs)
        self.rhs= expr(rhs)

    def __str__(self):
        return "addOp({} + {})".format(self.lhs, self.rhs)

    def step_add(self):
        return step_binary(e, addOp, lambda x, y: x+y)
            # lambda (arguments) : expression
            # Will x + y given an x and y

    def addEval(self):
        return evaluate(lhs) + evaluate(rhs)

class subOp(Expr):
    def __init__ (self, lhs, rhs):
        Expr.__init__(self)
        self.lhs = expr(lhs)
        self.rhs= expr(rhs)

    def __str__(self):
        return "subOp({} - {})".format(self.lhs, self.rhs)

    def step_sub(self):
        return step_binary(e, subOp, lambda x, y: x-y)

    def subEval(self):
        return evaluate(lhs) - evaluate(rhs)

class mulOp(Expr):
    def __init__ (self, lhs, rhs):
        Expr.__init__(self)
        self.lhs = expr(lhs)
        self.rhs= expr(rhs)

    def __str__(self):
        return "mulOp({} * {})".format(self.lhs, self.rhs)

    def step_mul(self):
        return step_binary(e, mulOp, lambda x,y: x*y)

    def mulEval(self):
        return evaluate(lhs) * evaluate(rhs)

class divOp(Expr):
    def __init__ (self, lhs, rhs):
        Expr.__init__(self)
        self.lhs = expr(lhs)
        self.rhs= expr(rhs)

    def __str__(self):
        return "divOp({} / {})".format(self.lhs, self.rhs)

    def step_div(self):
        pass

    def divEval(self):
        return evaluate(lhs) / evaluate(rhs)

class modOp(Expr):
    def __init__ (self, lhs, rhs):
        Expr.__init__(self)
        self.lhs = expr(lhs)
        self.rhs= expr(rhs)

    def __str__(self):
        return "modOp({} % {})".format(self.lhs, self.rhs)

    def step_mod(self):
        pass

    def modEval(self):
        return evaluate(lhs) % evaluate(rhs)

class eqOp(Expr):
    def __init__ (self, lhs, rhs):
        Expr.__init__(self)
        self.lhs = expr(lhs)
        self.rhs= expr(rhs)

    def __str__(self):
        return "eqOp({} == {})".format(self.lhs, self.rhs)

    def step_eq(self):
        pass

    def eqEval(self):
        return evaluate(lhs) == evaluate(rhs)

class gtOp(Expr):
    def __init__ (self, lhs, rhs):
        Expr.__init__(self)
        self.lhs = expr(lhs)
        self.rhs= expr(rhs)

    def __str__(self):
        return "subOp({} > {})".format(self.lhs, self.rhs)

    def step_gt(self):
        pass

    def gtEval(self):
        return evaluate(lhs) > evaluate(rhs)

class ltOp(Expr):
    def __init__ (self, e1, e2):
        Expr.__init__(self)
        self.lhs = e1
        self.rhs = e2

    def __str__(self):
        return "subOp({} < {})".format(self.lhs, self.rhs)

    def step_lt(self):
        pass

    def ltEval(self):
        return evaluate(lhs) < evaluate(rhs)

class gteOp(Expr):
    def __init__ (self, e1, e2):
        Expr.__init__(self)
        self.lhs = e1
        self.rhs = e2

    def __str__(self):
        return "subOp({} >= {})".format(self.lhs, self.rhs)

    def step_gte(self):
        pass

    def gteEval(self):
        return evaluate(lhs) >= evaluate(rhs)

class lteOp(Expr):
    def __init__ (self, e1, e2):
        Expr.__init__(self)
        self.lhs = e1
        self.rhs = e2

    def __str__(self):
        return "subOp({} <= {})".format(self.lhs, self.rhs)

    def step_lte(self):
        pass

    def lteEval(self):
        return evaluate(lhs) <= evaluate(rhs)

def expr(e):
    if type(e) is bool:
        return Bool(e)
    if type(e) is int:
        return Int(e)
    return e

