from Errors import err
from Lexer import Lexer
import Parser

print("Frukt Shell:")
while True:
	try:
		inp = input(">>> ")
		if inp == "exit":
			exit(0)
		
		lexer = Lexer(inp)
		error = lexer.lex()
		if error[0].err != err.OK:
			print(error)
			continue
		
		print(lexer.tokens)

	except Exception as e:
		print(repr(e))