# Generated from Expr.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ExprParser import ExprParser
else:
    from ExprParser import ExprParser

# This class defines a complete generic visitor for a parse tree produced by ExprParser.

class ExprVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ExprParser#exprList.
    def visitExprList(self, ctx:ExprParser.ExprListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#MulDivExpr.
    def visitMulDivExpr(self, ctx:ExprParser.MulDivExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#IdExpr.
    def visitIdExpr(self, ctx:ExprParser.IdExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#NumberExpr.
    def visitNumberExpr(self, ctx:ExprParser.NumberExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#ParensExpr.
    def visitParensExpr(self, ctx:ExprParser.ParensExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#AddSubExpr.
    def visitAddSubExpr(self, ctx:ExprParser.AddSubExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#AssignExpr.
    def visitAssignExpr(self, ctx:ExprParser.AssignExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#prog.
    def visitProg(self, ctx:ExprParser.ProgContext):
        return self.visitChildren(ctx)



del ExprParser