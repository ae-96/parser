def set_tokeninput(token_input_string):
    temp_array = token_input_string.split('\n')
    token_input = []
    for i in temp_array:
        temp_array2 = i.split(',')
        token_input.append([temp_array2[0].strip(), temp_array2[1].strip()])
    return token_input


class Parser:
    def __init__(self, input_string):
        self.token_input = set_tokeninput(input_string)

    def stmt_seq(self, token_pointer, current_node):
        # add to listofattachedchild to the current node
        token_pointer = self.statement(token_pointer, current_node)
        while token_pointer < len(self.token_input):
            if self.token_input[token_pointer][1] == 'SEMICOLON':
                token_pointer = self.statement(token_pointer + 1, current_node)
        return token_pointer

    def statement(self, token_pointer, current_node):
        if self.token_input[token_pointer][1] == 'IF':
            token_pointer = self.if_statement(token_pointer, current_node)
        elif self.token_input[token_pointer][1] == 'READ':
            token_pointer = self.read_statement(token_pointer, current_node)
        elif self.token_input[token_pointer][1] == 'WRITE':
            token_pointer = self.write_statement(token_pointer, current_node)
        elif self.token_input[token_pointer][1] == 'IDENTIFIER':
            token_pointer = self.assign_statement(token_pointer, current_node)
        elif self.token_input[token_pointer][1] == 'REPEAT':
            token_pointer = self.repeat_statement(token_pointer, current_node)
        return token_pointer

    def if_statement(self, token_pointer, current_node):
        pass

    def read_statement(self, token_pointer, current_node):
        pass

    def write_statement(self, token_pointer, current_node):
        pass

    def assign_statement(self, token_pointer, current_node):
        pass

    def repeat_statement(self, token_pointer, current_node):
        pass
