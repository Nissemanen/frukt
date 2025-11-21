from enum import Enum

class err(Enum):
	OK = 0
	UNKNOWN_TOKEN = 1
	SYNTAX_ERROR = 2

# TODO - make use of this funny guy, try find a way to get the line/char of where the error ocured
class detailed_err:
	def __init__(self, err: err, comment: str, start: dict, end: dict) -> None:
		self.err = err
		self.comment = comment
		self.start = start
		self.end = end
	
	def __repr__(self) -> str:
		return repr({self.err:self.comment})