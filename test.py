token_input_string='''read,READ
x,IDENTIFIER
;,SEMICOLON 
if,IF
0,NUMBER
<,LESSTHAN
x,IDENTIFIER
then,THEN 
fact,IDENTIFIER
:=,ASSIGN
1,NUMBER
;,SEMICOLON 
repeat,REPEAT
fact,IDENTIFIER
:=,ASSIGN
fact,IDENTIFIER
*,MULT
x,IDENTIFIER
;,SEMICOLON 
x,IDENTIFIER
:=,ASSIGN
x,IDENTIFIER
-,MINUS
1,NUMBER
until,UNTIL 
x,IDENTIFIER
=,EQUAL
0,NUMBER
;,SEMICOLON 
write,WRITE
fact,IDENTIFIER
end,END'''
temp_array=token_input_string.split('\n')
token_input=[]
for i in temp_array :
    temp_array2=i.split(',')
    token_input.append([temp_array2[0].strip(),temp_array2[1].strip()])

def stmt_seq(token_pointer,current_node) :
    # add to listofattachedchild to the current node 
    token_pointer= statement(token_pointer,current_node)
    while token_pointer<len(token_input) :
        if token_input[token_pointer][1] == 'SEMICOLON' :
            token_pointer= statement(token_pointer+1,current_node)
    return token_pointer

def statement(token_pointer,current_node) :
    if token_input[token_pointer][1] =='IF' : token_pointer= if_statement(token_pointer,current_node)
    elif token_input[token_pointer][1] =='READ' : token_pointer= read_statement(token_pointer,current_node)
    elif token_input[token_pointer][1] == 'WRITE': token_pointer= write_statement(token_pointer,current_node)
    elif token_input[token_pointer][1] == 'IDENTIFIER': token_pointer= assign_statement(token_pointer,current_node)
    elif token_input[token_pointer][1] == 'REPEAT' : token_pointer= repeat_statement(token_pointer,current_node)
    return token_pointer

def if_statement(token_pointer,current_node) : pass
def read_statement(token_pointer,current_node) : pass
def write_statement(token_pointer,current_node) : pass
def assign_statement(token_pointer,current_node) : pass
def repeat_statement(token_pointer,current_node) : pass
