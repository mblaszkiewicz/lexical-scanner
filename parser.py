#!/usr/bin/python

import scanner
import ply.yacc as yacc


names_dictionary = {}
tokens = scanner.tokens

precedence = (
    # to fill ...
    # ("left", '+', '-'),
    # ("left", '*', '/')
    # to fill ...
)


def p_error(p):
    if p: # scanner.find_column(p)
        print("Syntax error at line {0}, column {1}: LexToken({2}, '{3}')".format(p.lineno, "1",
                                                                                  p.type, p.value))
    else:
        print("Unexpected end of input")


def p_program(p):
    """program : instructions_opt"""
    print("PROGRAM")


def p_instructions_opt_1(p):
    """instructions_opt : instructions """
    print("INSTRUCTIONS OPT 1")


def p_instructions_opt_2(p):
    """instructions_opt : """
    print("INSTRUCTIONS OPT 2")


def p_instructions_1(p):
    """instructions : instructions instruction """
    print("INSTRUCTIONS 1")


def p_instructions_2(p):
    """instructions : instruction """
    print("INSTRUCTIONS 2")


def p_instruction_assign(p):
    'instruction : ID "=" expression'
    names_dictionary[p[1]] = p[3]
    print("INSTRUCTION ASSIGN")


def p_expression_paren(p):
    '''expression : "(" expression ")"
                  | "[" expression "]"
                  | "{" expression "}"'''
    p[0] = p[2]
    print("EXPRESSION PAREN")



def p_exp_name(p):
    'expression : ID'
    try:
        p[0] = names_dictionary[p[1]]
    except LookupError:
        print("Name not defined")
        p[0] = 0
    print("EXPRESSION NAME")


def p_exp_num(p):
    'expression : INTNUM'
    p[0] = p[1]
    print("EXPRESSION INTNUM")


def p_exp_fnum(p):
    'expression : FLOATNUM'
    p[0] = p[1]
    print("EXPRESSION FLOATNUM")


# to finish the grammar
# ....

def p_while_for(p):
    '''instruction : WHILE "(" expression ")" "{" instructions "}"
                   | FOR ID "=" INTNUM ":" INTNUM "{" instructions "}"
                   | WHILE "(" expression ")" instruction
                   | FOR ID "=" INTNUM ":" INTNUM instruction '''
    print("WHILE/FOR")

def p_break_cont_ret(p):
    '''instruction : BREAK ";"
                   | CONTINUE ";"
                   | RETURN ";"'''
    print("BREAK/CONT/RETURN")


def p_print(p):
    'instruction : PRINT ID ";"'
    print("PRINT")


def p_array_range(p):
    'arrayrange : ID range'


def p_range(p):
    'range : "[" INTNUM "," INTNUM "]" '


parser = yacc.yacc()
