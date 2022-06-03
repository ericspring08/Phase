import Lexer

lexer = Lexer.Lexer('true "hello" false kljdsf (10 + 10) / 40521 {{}}"hello"')
print(lexer.generate_tokens())