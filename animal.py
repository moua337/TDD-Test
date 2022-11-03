class Animal:
    def __init__(self, ctype):
        self.type = ctype
        self.size = ""
        self.age = 0
        self.name = "" 

        if self.type == 'cat':
            self.name = 'Seymour'
        if self.type == 'dog':
            self.name = 'Spot'
        
   
    def speak(self): 
        if self.type == 'cat':
            if self.size == 'small':
                return 'meow'
            elif self.size != 'small':
                return 'MEOW!'
        if self.type == 'dog':
            if self.size == 'small':
                return 'bow wow'
            elif self.size == 'medium':
                return 'Ruff ruff'
            else:
                return 'arf arf' 

    def describe(self):
        if self.age < 10:
            return f"{self.name} is young"
        else:
            return f"{self.name} is old"
