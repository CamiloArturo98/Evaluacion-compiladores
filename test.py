from antlr4 import *
from ExprLexer import ExprLexer
from ExprParser import ExprParser
from EvalVisitor import EvalVisitor

def main():
    visitor = EvalVisitor()

    while True:
        expr_input = input("Ingresa una expresión (o 'salir' para terminar): ")
        if expr_input.lower() == "salir":
            break

        # Convertimos la entrada a un flujo de entrada para ANTLR
        input_stream = InputStream(expr_input)
        lexer = ExprLexer(input_stream)  # Lexer procesa el flujo de entrada
        token_stream = CommonTokenStream(lexer)  # Genera el flujo de tokens
        parser = ExprParser(token_stream)  # Parser interpreta los tokens
        tree = parser.expr()  # Genera el árbol de expresión

        # Visitamos el árbol generado con el visitante
        result = visitor.visit(tree)
        print("Resultado:", result)
        print("Variables almacenadas:", visitor.memory)

if __name__ == "__main__":
    main()
