class Clause:
    def __init__(self, algebra, text_clause):
        self.text_clause = text_clause
        self.boolean_clause = algebra.parse(text_clause)

    def get_text_clause(self):
        return self.text_clause

    def get_boolean_clause(self):
        return self.boolean_clause