from enum import Enum

class err(Enum):
	OK = 0
	UNKNOWN_TOKEN = 1
	SYNTAX_ERROR = 2

# TODO - make use of this funny class, try find a way to get the line/char of where the error ocured
class detailed_err:
	def __init__(self, err: err, line: int, char: int) -> None:
		self.err = err
		self.line = line
		self.char = char