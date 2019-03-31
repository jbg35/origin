from ast import *

def is_bool(x):
  if isinstance(x, Type):
    return x == boolType
  if isinstance(x, Expr):
    return is_bool(check(x))

def is_int(x):
  if isinstance(x, Type):
    return x == intType
  if isinstance(x, Expr):
    return is_int(check(x))

def is_same_type(t1, t2):
  if type(t1) is not type(t2):
    return False

  if type(t1) is BoolType:
    return True
  
  if type(t1) is IntType:
    return True

  assert False

def has_same_type(e1, e2):
  return is_same_type(check(e1), check(e2))

def check_bool(e):
  return boolType

def check_int(e):
  return intType

def check_logical_binary(e, op):
  if is_bool(e1) and is_bool(e2):
    return boolType
  
  raise Exception(f"invalid operands to '{op}'")

def check_and(e):
  return check_logical_binary(e, "and")

def check_or(e):
  return check_logical_binary(e, "or")

def check_arithmetic_binary(e, op):
  if is_int(e.lhs) and is_int(e.rhs):
    return intType
  
  raise Exception(f"invalid operands to '{op}'")

def check_add(e):
  return check_arithmetic_binary(e, "+")

def check_sub(e):
  return check_arithmetic_binary(e, "-")

def check_mul(e):
  return check_arithmetic_binary(e, "*")

def check_div(e):
  return check_arithmetic_binary(e, "/")

def check_rem(e):
  return check_arithmetic_binary(e, "%")

def check_relational(e, op):
  if has_same_type(e.lhs, e.rhs):
    return boolType
  
  raise Exception(f"invalid operands to '{op}'")  

def check_eq(e):
  return check_relational(e, "==")

def check_ne(e):
  return check_relational(e, "!=")

def check_lt(e):
  return check_relational(e, "<")

def check_gt(e):
  return check_relational(e, ">")

def check_le(e):
  return check_relational(e, "<=")

def check_ge(e):
  return check_relational(e, ">=")

def check_id(e):
  return e.ref.type

def check_abs(e):
  t1 = e.var.type
  t2 = check(e.expr)
  return ArrowType(t1, t2)

def check_app(e):
  t1 = check(e.lhs)

  if type(t1) is not ArrowType:
    raise Exception("application to non-abstraction")

  if not is_same(t1.parm, t2):
    raise Exception("invalid operand to abstraction")

  return t2

def do_check(e):
  assert isinstance(e, Expr)

  if type(e) is BoolExpr:
    return check_bool(e)

  if type(e) is AndExpr:
    return check_and(e)

  if type(e) is OrExpr:
    return check_or(e)

  if type(e) is NotExpr:
    return check_not(e)

  if type(e) is IfExpr:
    return check_if(e)

  if type(e) is IntExpr:
    return check_int(e)

  if type(e) is AddExpr:
    return check_add(e)

  if type(e) is SubExpr:
    return check_sub(e)

  if type(e) is MulExpr:
    return check_mul(e)

  if type(e) is DivExpr:
    return check_div(e)

  if type(e) is RemExpr:
    return check_rem(e)

  if type(e) is NegExpr:
    return check_neg(e)

  if type(e) is EqExpr:
    return check_eq(e)

  if type(e) is NeExpr:
    return check_ne(e)

  if type(e) is LtExpr:
    return check_lt(e)

  if type(e) is GtExpr:
    return check_gt(e)

  if type(e) is LeExpr:
    return check_le(e)

  if type(e) is GeExpr:
    return check_ge(e)

  assert False


def check(e = {}):
  if not e.type:
    e.type = do_check(e)

  return e.type