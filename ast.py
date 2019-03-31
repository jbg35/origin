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

import copy

clone = copy.deepcopy

class Closure:
  def __init__(self, abs, env):
    self.abs = abs
    self.env = clone(env)

class Type:
  pass

class BoolType(Type):
  def __str__(self):
    return "Bool"

class IntType(Type):
  def __str__(self):
    return "Int"

class ArrowType(Type):
  def __init__(self, t1, t2):
    self.parm = t1
    self.ret = t2
  
  def __str__(self):
    return f"({self.lhs} -> {self.rhs}"

class FuncType(Type):
  def __init__(self, parms, ret):
    self.parms = parms
    self.ret = ret

boolType = BoolType()
intType = IntType()

class Expr:
  pass

class BoolExpr(Expr):
  def __init__(self, val):
    self.val = val

  def __str__(self):
    return "Bool ({})".format(self.val)

  def eval_bool(self, store):
    return self.val

class AndExpr(Expr):
  def __init__(self, e1, e2):
    self.lhs = expr(e1)
    self.rhs = expr(e2)

  def __str__(self):
    return "andOp({} , {})".format(self.lhs, self.rhs)

  def step_and(self):
    if is_reducible(self.lhs):
      return step(self.lhs), self.rhs

    if is_reducible(self.rhs):
      return self.lhs, step(self.rhs)

    return BoolExpr(self.lhs.val and self.rhs.val)

  def eval_and(self, store):
    return evaluate(self.lhs, store) and evaluate(self.rhs, store)

class OrExpr(Expr):
  def __init__(self, e1, e2):
    self.lhs = expr(e1)
    self.rhs = expr(e2)

  def __str__(self):
    return "orOp({},{})".format(self.lhs, self.rhs)

  def step_or(self):
    if is_reducible(self.lhs):
      return OrExpr(step(self.lhs), self.rhs)

    if is_reducible(self.rhs):
      return OrExpr(self.lhs, step(self.rhs))

    return BoolExpr(self.lhs.val or self.rhs.val)

  def eval_or(self,store):
    return evaluate(self.lhs, store) or evaluate(self.rhs, store)

class NotExpr(Expr):
  def __init__(self, e1):
    self.expr = expr(e1)

  def __str__(self):
    return "notOp({})".format(self.expr)

  def step_not(self):
    if is_reducible(self.expr):
      return NotExpr(step(self.expr))

    return BoolExpr(not self.expr.val)

  def eval_not(self,store):
    return not evaluate(self.expr, store)

class IfExpr(Expr):
  def __init__(self, e1, e2, e3):
    self.cond = expr(e1)
    self.true = expr(e2)
    self.false = expr(e3)

  def step_if(self):
    if is_reducible(self.cond):
      return NotExpr(step(self.cond), self.true, self.false)

    if self.cond.val:
      return self.true
    else:
      return self.false

  def __str__(self):
    return "ifOp(if {} then {} else {})".format(self.cond,self.true,self.false)

class IdExpr(Expr):
  def __init__(self, x):
    if type(x) is str:
      self.id = x
      self.ref = None 
    elif type(x) is VarDecl:
      self.id = x.id
      self.ref = x

  def __str__(self):
    return self.id

  def eval_id(self,store):
    return store[self.ref]

class VarDecl:
  def __init__(self, id, t):
    self.id = id
    self.type = t

  def __str__(self):
    return self.id

class AbsExpr(Expr):
  def __init__(self, var, e1):
    self.var = decl(var)
    self.expr = expr(e1)

  def __str__(self):
    return f"\\{self.var}.{self.expr}"

  def eval_abs(self,store):

    return Closure(e, store)

class AppExpr(Expr):
  def __init__(self, e1, e2):
    self.lhs = expr(e1)
    self.rhs = expr(e2)

  def __str__(self):
    return f"({self.lhs} {self.rhs})"

  def step_app(self):
    if is_reducible(self.lhs): # App-1
      return AppExpr(step(self.lhs), self.rhs)

    if type(self.lhs) is not AbsExpr:
      raise Exception("application of non-lambda")

    if is_reducible(self.rhs): # App-2
      return AppExpr(self.lhs, step(self.rhs))

    s = {
      self.lhs.var: self.rhs
    }

    return subst(e.lhs.expr, s);
  def eval_app(self,store):
    c = evaluate(self.lhs, store)

    if type(c) is not Closure:
      raise Exception("cannot apply a non-closure to an argument")

    v = evaluate(self.rhs, store)

    return evaluate(c.abs.expr, c.env + {c.abs.var: v})

class LambdaExpr(Expr):
  def __init__(self, vars, e1):
    self.vars = list(map(decl, vars))
    self.expr = expr(e1)

  def __str__(self):
    parms = ",".join(str(v) for v in self.vars)
    return f"\\({parms}).{self.expr}"

  def eval_lambda(self, store):
    return Closure(self, store)

class CallExpr(Expr):
  def __init__(self, fn, args):
    self.fn = expr(fn)
    self.args = list(map(expr, args))

  def __str__(self):
    args = ",".join(str(a) for a in self.args)
    return f"{self.fn} ({args})"

  def step_call(self):
    if is_reducible(self.fn):
      return CallExpr(step(self.fn), self.args)

    if len(self.args) < len(self.fn.vars):
      raise Exception("too few arguments")
    if len(self.args) > len(self.fn.vars):
      raise Exception("too many arguments")

    for i in range(len(self.args)):
      if is_reducible(self.args[i]):
        return CallExpr(self.fn, self.args[:i] + [step(self.args[i])] + self.args[i+1:])

    s = {}
    for i in range(len(self.args)):
      s[self.fn.vars[i]] = self.args[i]

    return subst(self.fn.expr, s);

  def eval_call(self,store):
    c = evaluate(self.fn, store)
  
    if type(c) is not Closure:
      raise Exception("cannot apply a non-closure to an argument")

    args = []
    for a in self.args:
      args += [evaluate(a, store)]

    env = clone(c.env)
    for i in range(len(args)):
      env[c.abs.vars[i]] = args[i]

    return evaluate(c.abs.expr, env)

class PlaceholderExpr(Expr):
  def __str__(self):
    return "_"

def expr(x):
  if type(x) is bool:
    return BoolExpr(x)
  if type(x) is str:
    return IdExpr(x)
  return x

def decl(x):
  if type(x) is str:
    return VarDecl(x)
  return x

from lookup import resolve
from subst import subst
from reduce import *
