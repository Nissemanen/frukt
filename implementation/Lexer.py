from Errors import err

class Token:
	def __init__(self, type_, value) -> None:
		self.type = type_
		self.value = value

class Lexer:
	def __init__(self, source):
		self.source = source
		self.pos = 0
		self.current_char = self.source[self.pos] if self.source else None
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
		return self.current_char

	def skip_whitespace(self):
		while self.current_char is not None and self.current_char.isspace():
			self.advance()

	def get_current_token(self) -> Token | err | None:
		if not self.current_char:
			return None

		if self.current_char in ['\n', '\r\n', ';']:
			char = self.current_char
			self.advance()
			return Token('TERMENATOR', char)
		
		if self.current_char.isspace():
			self.skip_whitespace()
			return Token('WHITESPACE', ' ')
		
		if self.current_char.isalpha():
			start_pos = self.pos
			while self.current_char is not None and self.current_char.isalnum():
				self.advance()
			value = self.source[start_pos:self.pos]
			return Token('IDENTIFIER', value)
		
		if self.current_char.isdigit():
			start_pos = self.pos
			while self.current_char is not None and self.current_char.isdigit():
				self.advance()
			value = self.source[start_pos:self.pos]

			if self.current_char == '.':
				self.advance()
				decimal_start = self.pos
				while self.current_char is not None and self.current_char.isdigit():
					self.advance()
				decimal_value = self.source[decimal_start:self.pos]
				value += '.' + decimal_value
			else:
				return err.SYNTAX_ERROR
			
			return Token('NUMBER', value)
		
		if self.current_char == '+':
			self.advance()
			return Token('ADD', '+')
		
		if self.current_char == '-':
			self.advance()
			return Token('SUBTRACT', '-')
		
		if self.current_char == '*':
			self.advance()
			return Token('MULTIPLY', '*')
		
		if self.current_char == '/':
			self.advance()
			return Token('DIVIDE', '/')
		
		if self.current_char == '=': # check if there is atleast one "="
			if self.advance() != '=': # check if its an assignment and also advancing
				return Token('ASSIGN', '=')

			if self.advance() != '=': # check if its percise or weak comparison and advancing
				return Token('COMPARISON', '==')
			
			self.advance() 
			return Token('STRONG_COMP', '===') # else we know its a strong comparison
		
		return err.UNKNOWN_TOKEN


	def lex(self) -> err|list[err]:
		self.tokens = []
		Errors = []
		while self.current_char is not None:
			result = self.get_current_token()

			if type(result) == Token:
				self.tokens.append(result)
			else:
				Errors.append(result)

		if Errors:
			return Errors
		
		return err.OK