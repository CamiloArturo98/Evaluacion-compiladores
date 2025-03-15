from ExprVisitor import ExprVisitor

class EvalVisitor(ExprVisitor):
    def __init__(self):
        self.memory = {}  # Diccionario para almacenar variables

    def visitAssignExpr(self, ctx):
    var_name = ctx.ID().getText()
    value = self.visit(ctx.expr())  # Evaluamos la expresión
    self.variables[var_name] = value  # Guardamos el resultado
    return value


    def visitNumberExpr(self, ctx):
        return int(ctx.NUMBER().getText())

    def visitAddSubExpr(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if ctx.ADD():
            return left + right
        else:
            return left - right

    def visitMulDivExpr(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if ctx.MUL():
            return left * right
        else:
            return left / right  # División flotante

    def visitParensExpr(self, ctx):
        return self.visit(ctx.expr())  # Aquí corregimos el error

    def visitIdExpr(self, ctx):
        var_name = ctx.ID().getText()
        return self.memory.get(var_name, 0)  # Retorna 0 si la variable no existe
