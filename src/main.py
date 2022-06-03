import Lexer

lexer = Lexer.Lexer("(10 + 10) / 40521 {{}}")
print(lexer.generate_tokens())