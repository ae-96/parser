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
        if_node = Node()
        if_node.name = 'if'
        if_node.shape = 'rect'
        token_pointer = self.exp(token_pointer+1, if_node)
        # lazm ykon fe then hena
        token_pointer = self.stmt_seq(token_pointer + 1, if_node)
        if self.token_input[token_pointer][1] == 'ELSE':
            token_pointer = self.stmt_seq(token_pointer + 1, if_node)
        # lazm ykon fe end hena
        token_pointer = token_pointer + 1
        current_node.listofchild.append(if_node)
        return token_pointer

    def read_statement(self, token_pointer, current_node):
        read_node = Node()
        read_node.name = 'read'
        # lazm ykon fe identifier hena ya kalbob
        read_node.value = '(' + str(self.token_input[token_pointer+1][0]) + ')'
        read_node.shape = 'rect'
        current_node.listofchild.append(read_node)
        return token_pointer + 2

    def write_statement(self, token_pointer, current_node):
        write_node = Node()
        write_node.name = 'write'
        write_node.shape = 'rect'
        token_pointer = self.exp(token_pointer + 1, write_node)
        current_node.listofchild.append(write_node)
        return token_pointer


    def assign_statement(self, token_pointer, current_node):
        assign_node = Node()
        assign_node.name = 'assign'
        # lazm ykon fe identifier hena ya kalbob
        assign_node.value = '(' + str(self.token_input[token_pointer][0]) + ')'
        assign_node.shape = 'rect'
        # lazm ykon fe := hena ya kalbob
        token_pointer = self.exp(token_pointer + 2, assign_node)
        current_node.listofchild.append(assign_node)
        return token_pointer


    def repeat_statement(self, token_pointer, current_node):
        repeat_node = Node()
        repeat_node.name = 'repeat'
        repeat_node.shape = 'rect'
        token_pointer = self.stmt_seq(token_pointer + 1, repeat_node)
        # lazm ykon fe until hena ya kalbob
        token_pointer = self.exp(token_pointer + 1, repeat_node)
        current_node.listofchild.append(repeat_node)
        return token_pointer

    def exp(self, token_pointer, current_node):
        pass


    def simple_exp(self, token_pointer, current_node):
        pass



    def term(self, token_pointer, current_node):
        pass
    def exp(self, token_pointer, current_node):
        pass
    def exp(self, token_pointer, current_node):
        pass
    def exp(self, token_pointer, current_node):
        pass
    def exp(self, token_pointer, current_node):
        pass
    def exp(self, token_pointer, current_node):
        pass
    def exp(self, token_pointer, current_node):
        pass
