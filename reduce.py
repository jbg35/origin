from ast import *

def is_value(e):
  return type(e) in (BoolExpr, AbsExpr, LambdaExpr)

def is_reducible(e):
  return not is_value(e)

def step(e):
  assert isinstance(e, Expr)
  assert is_reducible(e)

  if type(e) is AndExpr:
    return e.step_and()

  if type(e) is OrExpr:
    return e.step_or()

  if type(e) is NotExpr:
    return e.step_not()

  if type(e) is IfExpr:
    return e.step_if()

  if type(e) is AppExpr:
    return e.step_app()

  if type(e) is CallExpr:
    return e.step_call()

  assert False
  
def reduce(e):
  while not is_value(e):
    e = step(e)
    print(e)
  return e

def evaluate(e, store = {}):
  # Evaluate an expression. The store is a stack of mappings from
  # variables to values.

  if type(e) is BoolExpr:
    return e.eval_bool(store)

  if type(e) is AndExpr:
    return e.eval_and(store)

  if type(e) is OrExpr:
    return e.eval_or(store)

  if type(e) is NotExpr:
    return e.eval_not(store)

  if type(e) is IdExpr:
    return e.eval_id(store)

  if type(e) is AbsExpr:
    return e.eval_abs(store)

  if type(e) is AppExpr:
    return e.eval_app(store)

  if type(e) is LambdaExpr:
    return e.eval_lambda(store)

  if type(e) is CallExpr:
    return e.eval_call(store)
