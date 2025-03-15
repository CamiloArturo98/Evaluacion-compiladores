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

        input_stream = InputStream(expr_input)
        lexer = ExprLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = ExprParser(token_stream)
        tree = parser.expr()

        result = visitor.visit(tree)
        print("Resultado:", result)
        print("Variables almacenadas:", visitor.memory)

if __name__ == "__main__":
    main()
