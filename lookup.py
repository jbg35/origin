from ast import *

def lookup(id, stk):
  for scope in reversed(stk):
    if id in scope:
      return scope[id]
  return None

def typeRes(ts, stk):
  for s in ts:
    resolve(s, stk)

def type_resolve(t : Type, stk : list = []):
  if type(t) is BoolType:
    return t
  if type(t) is IntType:
    return t

def resolve(e, stk = []):
  # Resolve references to declared variables. This requires a scope
  # stack. A scope is a mappings from names to their declarations.
  #
  # Returns the modified tree.

  if type(e) is BoolExpr:
    # No ids here.
    return e

  if type(e) is AndExpr:
    # Recursively resolve in subexpressions.
    resolve(e.lhs, stk)
    resolve(e.rhs, stk)
    return e 

  if type(e) is OrExpr:
    # Recursively resolve in subexpressions.
    resolve(e.lhs, stk)
    resolve(e.rhs, stk)
    return e 

  if type(e) is NotExpr:
    # Recursively resolve in subexpressions.
    resolve(e.expr, stk)
    return e

  if type(e) is IfExpr:
    # Recursively resolve in subexpressions.
    resolve(e.cond, stk)
    resolve(e.true, stk)
    resolve(e.false, stk)
    return e

  if type(e) is IdExpr:
    # Perform name lookup.
    decl = lookup(e.id, stk)
    if not decl:
      raise Exception("name lookup error")

    # Bind the expression to its declaration.
    e.ref = decl
    return e

  if type(e) is AbsExpr:
    # Declare the variable by defining a new scope.
    # We could alternatively push the scope here and
    # then pop the scope after the recursive call (i.e.,
    # bracket the call with push/pop).
    resolve(e.expr, stk + [{e.var.id : e.var}])
    return e

  if type(e) is AppExpr:
    # Recursively resolve in subexpressions.
    resolve(e.lhs, stk)
    resolve(e.rhs, stk)
    return e

  if type(e) is LambdaExpr:
    # Do the same as with abstractions, but declare
    # all variables simultaneously.
    resolve(e.expr, stk + [{var.id : var for var in e.vars}])
    return e

  if type(e) is CallExpr:
    # Recursively resolve in each subexpression.
    resolve(e.fn, stk)
    for a in e.args:
      resolve(e.fn, stk)
    return e

  if type(e) is BoolType:
    return e

  if type(e) is IntType:
    return e

  if type(e) is FuncType:
    typeRes(e.parms, stk)
    type_resolve(e.rets, stk)

  if type(e) is TupleType:
    type_resolve(e.vals, stk)
    return e

  if type(e) is StructType:
    resolve(e.name)
    resolve(e.contents)
    return e
  assert False