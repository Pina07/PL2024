import ply.lex as lex


#Lista dos tokens
tokens = (
    'SELECT',
    'VARIABLE',
    'FROM',
    'WHERE',
    'COMMA',
    'EQUALS',
    'NUMBER',
    'GREATER_THAN',
    'LESS_THAN',
    'GREATER_THAN_EQUALS',
    'LESS_THAN_EQUALS',    
)



#Regular expressions for tokens

t_SELECT = r'SELECT'
t_FROM = r'FROM'
t_VARIABLE = r'id|nome|salario|empregados|salario'
t_COMMA = r','
t_WHERE = r'WHERE'
t_NUMBER = r'\d+'
t_EQUALS = r'\='
t_GREATER_THAN = r'\>'
t_LESS_THAN = r'\<'
t_GREATER_THAN_EQUALS = r'\>\='
t_LESS_THAN_EQUALS = r'\<\='



t_ignore = " \t"



def t_newLine(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    
    

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
    
    
lexer = lex.lex()



data = '''
SELECT id, nome, salario FROM empregados WHERE salario >= 820
'''


lexer.input(data)

while(True):
    tok = lexer.token()
    if not tok:
        break
    print(tok)      





