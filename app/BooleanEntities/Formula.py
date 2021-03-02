class Formula:
    def __init__(self, algebra, text_formula):
        self.text_formula = text_formula
        self.boolean_formula = algebra.parse(text_formula)

    def get_text_formula(self):
        return self.text_formula

    def get_boolean_formula(self):
        return self.boolean_formula
    
    
    