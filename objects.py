class Interpreter:

    def __init__(self):

        self.stack = []
        self.env   = {}

    def LOAD_VALUE(self, number):
        self.stack.append(number)

    def STORE_NAME(self, name):
        val = self.stack.pop()
        self.env[name] = val

    def LOAD_NAME(self, name):
        val = self.env[name]
        self.stack.append(val)

    def PRINT_ANSWER(self):
        ans = self.stack.pop()
        print(ans)

    def ADD_TWO_VALUES(self):
        b = self.stack.pop()
        a = self.stack.pop()

        added = a + b
        self.stack.append(added)

    def parse_arg(self, instr, arg, code_payload):
        """ Determine what the argument for a given instruction resolves to """

        vals  = ['LOAD_VALUE']
        names = ['LOAD_NAME', 'STORE_NAME']

        if   instr in vals:
            eval_arg = code_payload['vals'][arg]
        elif instr in names:
            eval_arg = code_payload['names'][arg]

        return eval_arg

    def run(self, code_payload):

        """
        code_payload as:
            {
                'instructions': [('INSTRUCTION', val_index), ...],
                'values':       [v1, v2, v3, ...]
            }
        """

        instructions = code_payload['instructions']

        for step in instructions:

            instr, arg = step

            eval_arg      = self.parse_arg(instr, arg, code_payload)
            bytecode_call = getattr(self, instr)

            if not arg:
                bytecode_call()
            else:
                bytecode_call(arg)