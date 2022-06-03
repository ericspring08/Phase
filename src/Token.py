class Token:
    def __init__(self, _type, _value):
        self.type = _type
        self.value = _value 
    
    def __repr__(self):
        return f"{self.type}: {self.value}"
