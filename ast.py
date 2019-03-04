class Expr(object):
    pass

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

class orOp(Expr):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __repr__(self):
        return "orOp({},{})".format(self.left, self.right)

    def orEval(self):
        if isValue(self.left) and isValue(self.right):
            return Bool(self.left.value and self.right.value)

        if isReducible(self.left):
            return orOp(step(self.left), self.right)

        if isReducible(self.right):
            return orOp(self.left, step(self.right))

class notOp(Expr):
    def __init__(self, e):
        self.expr = e

    def __repr__(self):
        return "notOp({})".format(self.expr)

    def notEval(self):
        if isValue(self.expr):
            return Bool(not self.expr)

        return notOp(step(self.expr))

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
    return type(e) is Bool

def isReducible(e):
    return not isValue(e)

def step(e):
    assert isReducible(e)

    if type(e) is notOp:
        return notOp.notEval(e)

    if type(e) is andOp:
        return andOp.step_and(e)

    if type(e) is orOp:
        return orOp.step_and(e)

def reduce(e):
    while isReducible(e):
        e = step(e)
    return e