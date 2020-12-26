from Parser import Parser


A=Parser('''read,READ
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
+,PLUS
1,NUMBER
+,PLUS
1,NUMBER
end,END''')
if A.check_error()==1:
    print ('ERROR')
elif A.check_error()==0:
    A.start_parsing()
    A.show_tree()
