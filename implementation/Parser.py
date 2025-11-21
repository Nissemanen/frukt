from Lexer import Token
from Errors import err, detailed_err

class AST_Node:
	def __init__(self, start:dict, end:dict) -> None:
		self.start = start
		self.end = end

class Literal_AST(AST_Node):
	def __init__(self, val:int|float|str|bool, start, end) -> None:
		super().__init__(start, end)
		self.val = val

class Variable_AST(AST_Node):
	def __init__(self, var:str, start, end) -> None:
		super().__init__(start, end)
		self.var = var

class Unary_AST(AST_Node):
	def __init__(self, operand: AST_Node, op: str, start, end) -> None:
		super().__init__(start, end)
		self.operand = operand
		self.op = op

class Bin_AST(AST_Node):
	def __init__(self, left: AST_Node, right: AST_Node, op: str, start, end) -> None:
		super().__init__(start, end)
		self.left = left
		self.right = right
		self.operator = op

class Conditional_AST(AST_Node):
	def __init__(self, condition: AST_Node, expr: AST_Node, start, end) -> None:
		super().__init__(start, end)
		self.condition = condition
		self.expr = expr

class Parser:
	def __init__(self, tokens: list) -> None:
		self.tokens = tokens
		self.pos = 0
		self.current_token = tokens[0] if tokens else None
		self.program = []

	def peek(self):
		peek_pos = self.pos+1
		if peek_pos >= len(self.tokens):
			return None
		return self.tokens[peek_pos]
	
	def advance(self, steps:int = 1):
		self.pos += 1
		if self.pos >= len(self.tokens):
			self.current_token = None
			return None
		self.current_token = self.tokens[self.pos]


	def parse(self) -> list[detailed_err]:
		program = []

		while self.current_token is not None:
			self.parse_statement()

		return [detailed_err(err.OK, "Successfuly parsed", {"line":-1,"character":-1},{"line":-1,"character":-1})]
	
	def parse_statement(self):
		pass