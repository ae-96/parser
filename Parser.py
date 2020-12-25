from tree import Tree
from node import Node


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
        self.output_tree = Tree()

    def stmt_seq(self, token_pointer, current_node):
        token_pointer = self.statement(token_pointer, current_node, 'parent')
        while token_pointer < len(self.token_input):
            if self.token_input[token_pointer][1] == 'SEMICOLON':
                token_pointer = self.statement(token_pointer + 1, current_node, 'sib')
        return token_pointer

    def statement(self, token_pointer, current_node, attachto):
        if self.token_input[token_pointer][1] == 'IF':
            token_pointer = self.if_statement(token_pointer, current_node, attachto)
        elif self.token_input[token_pointer][1] == 'READ':
            token_pointer = self.read_statement(token_pointer, current_node, attachto)
        elif self.token_input[token_pointer][1] == 'WRITE':
            token_pointer = self.write_statement(token_pointer, current_node, attachto)
        elif self.token_input[token_pointer][1] == 'IDENTIFIER':
            token_pointer = self.assign_statement(token_pointer, current_node, attachto)
        elif self.token_input[token_pointer][1] == 'REPEAT':
            token_pointer = self.repeat_statement(token_pointer, current_node, attachto)
        return token_pointer

    def if_statement(self, token_pointer, current_node, attachto):
        if_node = Node()
        if_node.name = 'if'
        if_node.shape = 'rect'
        if_node.attachto = attachto
        token_pointer = self.exp(token_pointer+1, if_node, 'parent')
        # lazm ykon fe then hena
        token_pointer = self.stmt_seq(token_pointer + 1, if_node)
        if self.token_input[token_pointer][1] == 'ELSE':
            token_pointer = self.stmt_seq(token_pointer + 1, if_node)
        # lazm ykon fe end hena
        token_pointer = token_pointer + 1
        current_node.listofchild.append(if_node)
        return token_pointer

    def read_statement(self, token_pointer, current_node, attachto):
        pass

    def write_statement(self, token_pointer, current_node, attachto):
        pass

    def assign_statement(self, token_pointer, current_node, attachto):
        pass

    def repeat_statement(self, token_pointer, current_node, attachto):
        pass

    def exp(self, token_pointer, current_node, attachto):
        pass
