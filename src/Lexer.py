from Token import Token
from Types import *

class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = -1
        self.next_token()
        
    def next_token(self):
        self.pos += 1
        if self.pos < len(self.text):
            self.current_char = self.text[self.pos]
        else:
            self.current_char = None

    def generate_tokens(self):
        tokens = []
        while(self.current_char != None):
            if self.current_char == " ":
                self.next_token()
            elif self.current_char in DIGITS:
                tokens.append(Token(INT_TYPE, self.create_num()))
            elif self.current_char in OPERATORS:
                tokens.append(Token(OPERATOR_TYPE, self.current_char))
                self.next_token()
            elif self.current_char in PARENTHESES:
                tokens.append(Token(PARENTHESIS_TYPE, self.current_char))
                self.next_token()
            elif self.current_char in BRACKETS:
                tokens.append(Token(BRACKET_TYPE, self.current_char))
                self.next_token()
                
        return tokens

    def create_num(self):
        num = ""
        while self.current_char in DIGITS or self.current_char == ".":
            if self.current_char == None: 
                break
            num += self.current_char
            self.next_token()
        
        return num