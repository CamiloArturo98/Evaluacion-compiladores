# Generated from Expr.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ExprParser import ExprParser
else:
    from ExprParser import ExprParser

# This class defines a complete listener for a parse tree produced by ExprParser.
class ExprListener(ParseTreeListener):

    # Enter a parse tree produced by ExprParser#exprList.
    def enterExprList(self, ctx:ExprParser.ExprListContext):
        pass

    # Exit a parse tree produced by ExprParser#exprList.
    def exitExprList(self, ctx:ExprParser.ExprListContext):
        pass


    # Enter a parse tree produced by ExprParser#MulDivExpr.
    def enterMulDivExpr(self, ctx:ExprParser.MulDivExprContext):
        pass

    # Exit a parse tree produced by ExprParser#MulDivExpr.
    def exitMulDivExpr(self, ctx:ExprParser.MulDivExprContext):
        pass


    # Enter a parse tree produced by ExprParser#IdExpr.
    def enterIdExpr(self, ctx:ExprParser.IdExprContext):
        pass

    # Exit a parse tree produced by ExprParser#IdExpr.
    def exitIdExpr(self, ctx:ExprParser.IdExprContext):
        pass


    # Enter a parse tree produced by ExprParser#NumberExpr.
    def enterNumberExpr(self, ctx:ExprParser.NumberExprContext):
        pass

    # Exit a parse tree produced by ExprParser#NumberExpr.
    def exitNumberExpr(self, ctx:ExprParser.NumberExprContext):
        pass


    # Enter a parse tree produced by ExprParser#ParensExpr.
    def enterParensExpr(self, ctx:ExprParser.ParensExprContext):
        pass

    # Exit a parse tree produced by ExprParser#ParensExpr.
    def exitParensExpr(self, ctx:ExprParser.ParensExprContext):
        pass


    # Enter a parse tree produced by ExprParser#AddSubExpr.
    def enterAddSubExpr(self, ctx:ExprParser.AddSubExprContext):
        pass

    # Exit a parse tree produced by ExprParser#AddSubExpr.
    def exitAddSubExpr(self, ctx:ExprParser.AddSubExprContext):
        pass


    # Enter a parse tree produced by ExprParser#AssignExpr.
    def enterAssignExpr(self, ctx:ExprParser.AssignExprContext):
        pass

    # Exit a parse tree produced by ExprParser#AssignExpr.
    def exitAssignExpr(self, ctx:ExprParser.AssignExprContext):
        pass


    # Enter a parse tree produced by ExprParser#prog.
    def enterProg(self, ctx:ExprParser.ProgContext):
        pass

    # Exit a parse tree produced by ExprParser#prog.
    def exitProg(self, ctx:ExprParser.ProgContext):
        pass



del ExprParser