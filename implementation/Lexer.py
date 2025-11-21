from Errors import err, detailed_err
import json

KEYWORDS = [
	"if", "else", "try", "except", "match",
	"while", "for",
	"break", "continue", "return",
	"var", "const", "func", "class",
	"true", "false", "none",
	"do", "end"
	]

class Token:
	def __init__(self, type_, value, start: dict, end: dict) -> None:
		self.type = type_
		self.value = value
		self.start = start
		self.end = end
	
	def __repr__(self) -> str:
		return repr({self.type:self.value})

class Lexer:
	def __init__(self, source):
		self.source = source
		self.pos = 0
		self.line = 0
		self.char = 0
		self.current_char = source[0] if source else None
		self.tokens = []
	
	def peek(self):
		peek_pos = self.pos + 1
		if peek_pos >= len(self.source):
			return None
		return self.source[peek_pos]

	def advance(self) -> None|str:
		self.pos += 1

		if self.pos >= len(self.source):
			self.current_char = None
			return None
		
		self.current_char = self.source[self.pos]


		if self.current_char == "\n":
			self.line += 1
			self.char = 0
		else:
			self.char += 1

		return self.current_char

	def skip_whitespace(self):
		while self.current_char is not None and self.current_char.isspace():
			self.advance()

	def get_current_token(self) -> Token | detailed_err | None:
		if not self.current_char:
			return None

		if self.current_char in ['\n', '\r\n', ';']:
			char = self.current_char
			self.advance()
			return Token('TERMENATOR', char, start={"line": self.line, "character":self.char}, end={"line":self.line, "character":self.char})
		
		if self.current_char.isspace():
			start_line = self.line
			start_char = self.char
			self.skip_whitespace()
			return Token('WHITESPACE', ' ', start={"line":start_line, "character":start_char}, end={"line":self.line, "character":self.char})
		
		if self.current_char.isalpha():
			start_pos = self.pos
			start_line = self.line
			start_char = self.char

			while self.current_char is not None and self.current_char.isalnum():
				self.advance()
			value = self.source[start_pos:self.pos]

			if value in KEYWORDS:
				return Token('KEYWORD', value, start={"line":start_line,"character":start_char},end={})

			return Token('IDENTIFIER', value, start={"line":start_line, "character":start_char}, end={"line":self.line, "character":self.char})
		
		if self.current_char.isdigit():
			start_pos = self.pos
			start_line = self.line
			start_char = self.char
			while self.current_char is not None and self.current_char.isdigit():
				self.advance()
			value = self.source[start_pos:self.pos]

			if self.current_char == '.':
				self.advance()
				decimal_start = self.pos
				while self.current_char is not None and self.current_char.isdigit():
					self.advance()
				decimal_value = self.source[decimal_start:self.pos]
				if not decimal_value.isdigit():
					return detailed_err(err.SYNTAX_ERROR, comment=f"Invalid numeric literal at line {self.line}", start={"line":start_line, "character":start_char}, end={"line":self.line, "character":self.char})
				
				value += '.' + decimal_value
			
			return Token('NUMBER', value, start={"line":start_line, "character":start_char}, end={"line":self.line, "character":self.char})
		
		if self.current_char == '+':
			start_line = self.line
			start_char = self.char
			self.advance()
			return Token('ADD', '+', start={"line":start_char, "character":start_char}, end={"line":start_line, "character":start_char})
		
		if self.current_char == '-':
			start_line = self.line
			start_char = self.char
			self.advance()
			return Token('SUBTRACT', '-', start={"line":start_char, "character":start_char}, end={"line":start_line, "character":start_char})
		
		if self.current_char == '*':
			start_line = self.line
			start_char = self.char
			self.advance()
			return Token('MULTIPLY', '*', start={"line":start_char, "character":start_char}, end={"line":start_line, "character":start_char})
		
		if self.current_char == '/':
			start_line = self.line
			start_char = self.char
			self.advance()
			return Token('DIVIDE', '/', start={"line":start_char, "character":start_char}, end={"line":start_line, "character":start_char})
		
		if self.current_char == '=': # check if there is atleast one "="
			start_line = self.line
			start_char = self.char
			if self.advance() != '=': # check if its an assignment and also advancing
				return Token('ASSIGN', '=', start={"line":start_char, "character":start_char}, end={"line":start_line, "character":start_char})
			second_line = self.line
			second_char = self.char

			if self.advance() != '=': # check if its percise or weak comparison and advancing
				return Token('COMPARISON', '==', start={"line":start_char, "character":start_char}, end={"line":second_line, "character":second_char})
			third_line = self.line
			third_char = self.char
			
			self.advance() 
			return Token('STRONG_COMP', '===', start={"line":start_char, "character":start_char}, end={"line":third_line, "character":third_char}) # else we know its a strong comparison
		
		if self.current_char == '(':
			start_line = self.line
			start_char = self.char
			self.advance()
			return Token('LPARENT', '(', start={"line":start_char, "character":start_char}, end={"line":start_line, "character":start_char})
		
		if self.current_char == ')':
			start_line = self.line
			start_char = self.char
			self.advance()
			return Token('RPARENT', ')', start={"line":start_char, "character":start_char}, end={"line":start_line, "character":start_char})

		start_line = self.line
		start_char = self.char
		unkown_char = self.current_char
		self.advance()
		return Token('UNKNOWN', unkown_char, start={"line":start_char, "character":start_char}, end={"line":start_line, "character":start_char})


	def lex(self) -> list[detailed_err]:
		self.tokens = []
		Errors = []
		while self.current_char is not None:
			result = self.get_current_token()

			if type(result) == Token:
				self.tokens.append(result)
			elif type(result) == detailed_err:
				print(f"appending '{result.err.name}:{result.comment}' to errors")
				Errors.append(result)

		if Errors:
			return Errors
		
		self.tokens.append(Token('EOF', '', start={"line":-1, "character":-1}, end={"line":-1, "character":-1}))
		
		return [detailed_err(err.OK, "Successfully lexed", start={"line":-1, "character":-1}, end={"line":-1, "character":-1})]


if __name__ == "__main__":
	source = """x = 1
y = 5

if x >= y print("wow")
else print("no :(")"""

	print(f"source:\n{source}\n")

	lexer = Lexer(source)
	error = lexer.lex()

	print(f"error: {error}\n")

	if error != err.OK:
		if type(error) == list:
			print(f"Errors happened:")
			print([f"{single_err}\n" for single_err in error])
		
		else:
			print(f"Error happened: {err.name}")
	
	else:
		token_dict = [{token.type:token.value} for token in lexer.tokens if token.type != 'WHITESPACE']
		print(f"all tokens:\n{json.dumps(token_dict, indent=2)}")
		for token in lexer.tokens:
			print(f"{' '*(10-len(token.type))}{token.type}:{repr(token.value)}")
