import Lexer
from FileReader import open_file
import sys 

if len(sys.argv) == 2:
    code = open_file(sys.argv[1])
    lexer = Lexer.Lexer(code)
    print(lexer.generate_tokens())