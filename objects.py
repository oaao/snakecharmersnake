class Interpreter:

    def __init__(self):

        self.stack = []

    def LOAD_VALUE(self, number):
        self.stack.append(number)

    def PRINT_ANSWER(self):
        ans = self.stack.pop()
        print(ans)

    def ADD_TWO_VALUES(self):
        b = self.stack.pop()
        a = self.stack.pop()

        added = a + b
        self.stack.append(added)

    def run(self, code_payload):

        """
        code_payload as:
            {
                'instructions': [('INSTRUCTION', val_index), ...],
                'values':       [v1, v2, v3, ...]
            }
        """

        instructions = code_payload['instructions']
        vals         = code_payload['values']

        for step in instructions:

            instr, arg = step

            if   instr == 'LOAD_VALUE':
                self.LOAD_VALUE(vals[arg])
            elif instr == 'ADD_TWO_VALUES':
                self.ADD_TWO_VALUES()
            elif instr == 'PRINT_ANSWER':
                self.PRINT_ANSWER()
