from ply import yacc
from lex import tokens,analizador_lexico


def p_programa(p):
  """programa : INICIODEPROGRAMA declaraciones FINPROGRAMA"""
  pass
def p_declaraciones(p):
  """declaraciones : librerias
                   | cuerpo"""
  pass
def p_librerias(p):
  """ librerias : LIBRERIA PARENTESISA ID OPERADORPUNTO EXTENSION PARENTESISC COMA librerias
                | LIBRERIA PARENTESISA ID OPERADORPUNTO EXTENSION PARENTESISC ENDOFLINE cuerpo"""
  pass

def p_cuerpo(p):
  """ cuerpo : variable cuerpo
            | funcion cuerpo
            | asignacion cuerpo
            | procedimiento cuerpo
            | condicional cuerpo
            | bucle cuerpo
            | reservadas cuerpo
            | vpin cuerpo
            | empty"""
  pass
def p_vpin(p):
  """vpin : VPIN PARENTESISA ID VARTYPESEPARATOR TYPE PARENTESISC ENDOFLINE"""
  pass
def p_reservadas(p):
  """ reservadas : ADELANTE PARENTESISA PARENTESISC ENDOFLINE
                | ATRAS PARENTESISA  PARENTESISC ENDOFLINE
                | IZQUIERDA PARENTESISA  PARENTESISC ENDOFLINE
                | DERECHA PARENTESISA PARENTESISC ENDOFLINE
                | ESPERAR PARENTESISA NUMBER PARENTESISC ENDOFLINE
                | ESPERAR PARENTESISA ID PARENTESISC ENDOFLINE
                | FRENAR PARENTESISA PARENTESISC ENDOFLINE"""
  pass
def p_bucle(p):
  """bucle : WHILE PARENTESISA PARENTESISC BEGIN cuerpo END ENDOFLINE"""
  pass
def p_condicional(p):
  """condicional : IF PARENTESISA PARENTESISC BEGIN cuerpo END ENDOFLINE
                 | IF PARENTESISA PARENTESISC BEGIN cuerpo END ELSE BEGIN cuerpo END ENDOFLINE"""
  pass
def p_procedimiento(p):
  """procedimiento : PROCEDIMIENTO ID PARENTESISA argumentos PARENTESISC ENDOFLINE"""
  pass
def p_asignacion(p):
  """asignacion : ID IGUAL ID ENDOFLINE
                  | ID IGUAL NUMBER ENDOFLINE
                  | ID IGUAL DECIMALNUMBER ENDOFLINE
                  """
  pass
def p_funcion(p):
  """funcion : FUNCION ID PARENTESISA argumentos PARENTESISC VARTYPESEPARATOR TYPE ENDOFLINE"""
  pass
def p_variable(p):
  """variable : VARIABLE PARENTESISA ID  VARTYPESEPARATOR TYPE PARENTESISC ENDOFLINE"""
  pass
def p_argumentos(p):
  """ argumentos : ID VARTYPESEPARATOR TYPE COMA argumentos
                 | ID VARTYPESEPARATOR TYPE"""
  pass

def p_empty(p):
  'empty :'
  pass
def p_error(p):
  print("Error sintÃ¡ctico en la li­nea: " + str(p.lineno)
              + ". No se esperaba el token: " + str(p.value))
  raise Exception('syntax', 'error')
analizador_sintactico = yacc.yacc()
analizador_lexico.lineno = 0