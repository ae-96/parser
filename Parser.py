from tree import Tree
from node import Node
from re import *



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
    def check_error(self):
        tokens = compile(r'[a-z]+|\d+|\+|=|;|:=|\(|\)|<|\*|/|-', IGNORECASE)
        for i in self.token_input :
            lexeme = findall(tokens,i[0] )
            if len(lexeme)==0:
                return 1
            if (self.check_syntax(i)==1):
                return 1
        return 0

    def check_syntax(self, token):
        if (token[0]==';' and token[1]=='SEMICOLON'): return 0
        elif (token[0]=='if' and token[1]=='IF'): return 0
        elif (token[0]=='else' and token[1]=='ELSE'): return 0
        elif (token[0]=='then' and token[1]=='THEN'): return 0
        elif (token[0]=='end' and token[1]=='END'): return 0
        elif (token[0]=='repeat' and token[1]=='REPEAT'): return 0
        elif (token[0]=='until' and token[1]=='UNTIL'): return 0
        elif (token[0]==':=' and token[1]=='ASSIGN'): return 0
        elif (token[0]=='read' and token[1]=='READ'): return 0
        elif (token[0]=='write' and token[1]=='WRITE'): return 0
        elif (token[0]=='<' and token[1]=='LESSTHAN'): return 0
        elif (token[0]=='=' and token[1]=='EQUAL'): return 0
        elif (token[0]=='+' and token[1]=='PLUS'): return 0
        elif (token[0]=='-' and token[1]=='MINUS'): return 0
        elif (token[0]=='*' and token[1]=='MULT'): return 0
        elif (token[0]=='/' and token[1]=='DIV'): return 0
        elif (token[0]=='(' and token[1]=='OPENBRACKET'): return 0
        elif (token[0]==')' and token[1]=='CLOSEDBRACKET'): return 0
        elif (token[0].isalpha() and token[1]=='IDENTIFIER'): return 0
        elif (token[0].isalnum() and token[1]=='NUMBER'): return 0
        else : return 1

    def start_parsing(self):
        self.stmt_seq(0, self.output_tree.root)

    def stmt_seq(self, token_pointer, current_node):
        token_pointer = self.statement(token_pointer, current_node)
        while token_pointer < len(self.token_input):
            if self.token_input[token_pointer][1] == 'SEMICOLON':
                token_pointer = self.statement(token_pointer + 1, current_node)

            # bug 3omdaaaaaaaaaaaaaaaaa
            # 2l72ona ya naaaaaaaaaas
            # 2tfrgo 3la el beeeeh
            # de 3'lta y3mlha 3ayel so3'ayar ?
            # 3eeeb walahy
            else:
                break
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
        if_node.shape = 'rectangle'
        token_pointer = self.exp(token_pointer + 1, if_node)
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
        read_node.value = '(' + str(self.token_input[token_pointer + 1][0]) + ')'
        read_node.shape = 'rectangle'
        current_node.listofchild.append(read_node)
        return token_pointer + 2

    def write_statement(self, token_pointer, current_node):
        write_node = Node()
        write_node.name = 'write'
        write_node.shape = 'rectangle'
        token_pointer = self.exp(token_pointer + 1, write_node)
        current_node.listofchild.append(write_node)
        return token_pointer

    def assign_statement(self, token_pointer, current_node):
        assign_node = Node()
        assign_node.name = 'assign'
        # lazm ykon fe identifier hena ya kalbob
        assign_node.value = '(' + str(self.token_input[token_pointer][0]) + ')'
        assign_node.shape = 'rectangle'
        # lazm ykon fe := hena ya kalbob
        token_pointer = self.exp(token_pointer + 2, assign_node)
        current_node.listofchild.append(assign_node)
        return token_pointer

    def repeat_statement(self, token_pointer, current_node):
        repeat_node = Node()
        repeat_node.name = 'repeat'
        repeat_node.shape = 'rectangle'
        token_pointer = self.stmt_seq(token_pointer + 1, repeat_node)
        # lazm ykon fe until hena ya kalbob
        token_pointer = self.exp(token_pointer + 1, repeat_node)
        current_node.listofchild.append(repeat_node)
        return token_pointer

    def exp(self, token_pointer, current_node):
        new_current_node = Node()
        token_pointer = self.simple_exp(token_pointer, new_current_node)
        # temp_token_pointer = token_pointer
        # token_pointer = self.simple_exp(token_pointer, current_node)
        if token_pointer < len(self.token_input):
            if self.token_input[token_pointer][1] == 'LESSTHAN' or self.token_input[token_pointer][1] == 'EQUAL':
                temp_node = Node()
                new_current_node.name = 'op'
                new_current_node.shape = 'oval'
                # lazm ykon fe < or = hena ya kalbob
                new_current_node.value = '(' + str(self.token_input[token_pointer][0]) + ')'
                token_pointer = self.simple_exp(token_pointer + 1, new_current_node)
                temp_node.listofchild.append(new_current_node)
                new_current_node = temp_node

                # comparison_op_node = Node()
                # comparison_op_node.name = 'op'
                # comparison_op_node.shape = 'oval'
                # lazm ykon fe < or = hena ya kalbob
                # comparison_op_node.value = '(' + str(self.token_input[token_pointer][0]) + ')'
                # token_pointer = self.simple_exp(temp_token_pointer, comparison_op_node)
                # token_pointer = self.simple_exp(token_pointer+1, comparison_op_node)
                # del current_node.listofchild[-1]
                # current_node.listofchild.append(comparison_op_node)
        current_node.listofchild.append(new_current_node.listofchild[0])
        return token_pointer

    def simple_exp(self, token_pointer, current_node):
        new_current_node = Node()
        token_pointer = self.term(token_pointer, new_current_node)
        while token_pointer < len(self.token_input):
            if self.token_input[token_pointer][1] == 'PLUS' or self.token_input[token_pointer][1] == 'MINUS':
                temp_node = Node()
                new_current_node.name = 'op'
                new_current_node.shape = 'oval'
                # lazm ykon fe + or - hena ya kalbob
                new_current_node.value = '(' + str(self.token_input[token_pointer][0]) + ')'
                token_pointer = self.term(token_pointer + 1, new_current_node)
                temp_node.listofchild.append(new_current_node)
                new_current_node = temp_node
            else:
                break
        current_node.listofchild.append(new_current_node.listofchild[0])
        return token_pointer

    def term(self, token_pointer, current_node):
        new_current_node = Node()
        token_pointer = self.factor(token_pointer, new_current_node)
        while token_pointer < len(self.token_input):
            if self.token_input[token_pointer][1] == 'MULT' or self.token_input[token_pointer][1] == 'DIV':
                temp_node = Node()
                new_current_node.name = 'op'
                new_current_node.shape = 'oval'
                # lazm ykon fe * or / hena ya kalbob
                new_current_node.value = '(' + str(self.token_input[token_pointer][0]) + ')'
                token_pointer = self.factor(token_pointer + 1, new_current_node)
                temp_node.listofchild.append(new_current_node)
                new_current_node = temp_node
            else:
                break
        current_node.listofchild.append(new_current_node.listofchild[0])

        return token_pointer

    def factor(self, token_pointer, current_node):
        if self.token_input[token_pointer][1] == 'OPENBRACKET':
            bracket_node = Node()
            # lazm ykon fe ( hena ya kalbob
            bracket_node.name = '('
            bracket_node.shape = 'oval'
            current_node.listofchild.append(bracket_node)
            token_pointer = self.exp(token_pointer + 1, current_node)
            # lazm ykon fe ) hena ya kalbob
            bracket_node.name = ')'
            current_node.listofchild.append(bracket_node)

        elif self.token_input[token_pointer][1] == 'NUMBER':
            number_node = Node()
            number_node.name = 'const'
            number_node.value = '(' + str(self.token_input[token_pointer][0]) + ')'
            number_node.shape = 'oval'
            current_node.listofchild.append(number_node)
        elif self.token_input[token_pointer][1] == 'IDENTIFIER':
            identifier_node = Node()
            identifier_node.name = 'id'
            identifier_node.value = '(' + str(self.token_input[token_pointer][0]) + ')'
            identifier_node.shape = 'oval'
            current_node.listofchild.append(identifier_node)
        return token_pointer + 1

    def show_tree(self):
        self.show_subtree(self.output_tree.root)

    def show_subtree(self, start_root):
        print(start_root.name + '\n' + start_root.value + '\n' + start_root.shape + '\n')
        for i in start_root.listofchild:
            self.show_subtree(i)

    def convert_to_string(self):
        definition = []
        relation = []
        levels = []
        nodepointer = 1
        parentnodeindex = 1
        firsttime = 1
        self.convert_tree(self.output_tree.root, definition, relation, levels, nodepointer, parentnodeindex, firsttime)
        definition_str = '\n'.join(definition)
        relation_str = '\n'.join(relation)
        levels_str = '\n'.join(levels)
        final_str = 'graph\ndemo{\n' + definition_str + '\n' + relation_str + '\n' + levels_str + '\n}'
        return final_str

    def convert_tree(self, node, definition, relation, levels, nodepointer, parentnodeindex, firsttime):
        rect_flag = 0
        for i in range(len(node.listofchild)):
            node.listofchild[i].index = nodepointer
            nodepointer = nodepointer + 1
            temp_str = 'node' + str(node.listofchild[i].index) + '[label ="' + str(
                node.listofchild[i].name) + '\\n' + str(node.listofchild[i].value) + '" shape="' + str(
                node.listofchild[i].shape) + '"]'
            definition.append(temp_str)
            if node.listofchild[i].shape == 'oval':
                temp_str = 'node' + str(node.listofchild[i].index) + '--node' + str(parentnodeindex) + ';'
                relation.append(temp_str)
            else:
                if rect_flag == 0:
                    if firsttime == 0:
                        temp_str = 'node' + str(node.listofchild[i].index) + '--node' + str(parentnodeindex) + ';'
                        relation.append(temp_str)
                    rect_flag = 1
                else:
                    temp_str = 'node' + str(node.listofchild[i].index) + '--node' + str(
                        node.listofchild[i - 1].index) + ';'
                    relation.append(temp_str)
                    temp_str = 'subgraph subs' + str(nodepointer) + '{\nrank="same"\nnode' + str(
                        node.listofchild[i].index) + '\nnode' + str(
                        node.listofchild[i - 1].index) + '\n}'
                    levels.append(temp_str)
            nodepointer = self.convert_tree(node.listofchild[i], definition, relation, levels, nodepointer,
                                            node.listofchild[i].index, 0)
        return nodepointer
