grammar Expr;

// Reglas léxicas
NUMBER  : [0-9]+ ;
ID      : [a-zA-Z]+ ;
WS      : [ \t\r\n]+ -> skip ;

// Operadores
MUL  : '*' ;
DIV  : '/' ;
ADD  : '+' ;
SUB  : '-' ;
ASSIGN : '=' ;
SEMI   : ';' ;

// Reglas sintácticas
exprList : expr (SEMI expr)* SEMI? ;
expr    : ID ASSIGN expr          # AssignExpr
        | expr (MUL | DIV) expr   # MulDivExpr
        | expr (ADD | SUB) expr   # AddSubExpr
        | '(' expr ')'            # ParensExpr
        | NUMBER                  # NumberExpr
        | ID                      # IdExpr
        ;

// Punto de entrada
prog : exprList ;

