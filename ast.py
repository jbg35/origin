class AST(object):
	pass

class Bool(AST):
	def __init__(self, b):
		assert b == True or b == False
		self.b = b

	def __repr__(self):
		return "Bool ({})".format(self.b)

	def evaluate(self, ctx):
		return self.b

class andOp(AST):
	
	def __init__(self, left, right):
		self.left = left
		self.right = right

	def __repr__(self):
		return "andOp({} , {})".format(self.left, self.right)

	def evaluate(self, ctx):
		lhs = self.left.evaluate(ctx)
		rhs = self.right.evaluate(ctx)
		return lhs and rhs
	
class orOp(AST):
	def __init__(self, left, right):
		self.left = left
		self.right = right

	def __repr__(self):
		return "orOp({},{})".format(self.left, self.right)

	def evaluate(self,ctx):
		return self.left.evaluate(ctx) or self.right.evaluate(ctx)

class notOp(AST):
	def __init__(self, val):
		self.val = val
	def __repr__(self):
		return "notOp({})".format(self.value)
	def evaluate(self,ctx):
		return not self.val.evaluate(ctx)
