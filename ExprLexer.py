# Generated from Expr.g4 by ANTLR 4.13.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,11,56,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,1,0,1,0,1,1,1,1,1,2,4,2,
        29,8,2,11,2,12,2,30,1,3,4,3,34,8,3,11,3,12,3,35,1,4,4,4,39,8,4,11,
        4,12,4,40,1,4,1,4,1,5,1,5,1,6,1,6,1,7,1,7,1,8,1,8,1,9,1,9,1,10,1,
        10,0,0,11,1,1,3,2,5,3,7,4,9,5,11,6,13,7,15,8,17,9,19,10,21,11,1,
        0,3,1,0,48,57,2,0,65,90,97,122,3,0,9,10,13,13,32,32,58,0,1,1,0,0,
        0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,
        13,1,0,0,0,0,15,1,0,0,0,0,17,1,0,0,0,0,19,1,0,0,0,0,21,1,0,0,0,1,
        23,1,0,0,0,3,25,1,0,0,0,5,28,1,0,0,0,7,33,1,0,0,0,9,38,1,0,0,0,11,
        44,1,0,0,0,13,46,1,0,0,0,15,48,1,0,0,0,17,50,1,0,0,0,19,52,1,0,0,
        0,21,54,1,0,0,0,23,24,5,40,0,0,24,2,1,0,0,0,25,26,5,41,0,0,26,4,
        1,0,0,0,27,29,7,0,0,0,28,27,1,0,0,0,29,30,1,0,0,0,30,28,1,0,0,0,
        30,31,1,0,0,0,31,6,1,0,0,0,32,34,7,1,0,0,33,32,1,0,0,0,34,35,1,0,
        0,0,35,33,1,0,0,0,35,36,1,0,0,0,36,8,1,0,0,0,37,39,7,2,0,0,38,37,
        1,0,0,0,39,40,1,0,0,0,40,38,1,0,0,0,40,41,1,0,0,0,41,42,1,0,0,0,
        42,43,6,4,0,0,43,10,1,0,0,0,44,45,5,42,0,0,45,12,1,0,0,0,46,47,5,
        47,0,0,47,14,1,0,0,0,48,49,5,43,0,0,49,16,1,0,0,0,50,51,5,45,0,0,
        51,18,1,0,0,0,52,53,5,61,0,0,53,20,1,0,0,0,54,55,5,59,0,0,55,22,
        1,0,0,0,4,0,30,35,40,1,6,0,0
    ]

class ExprLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    NUMBER = 3
    ID = 4
    WS = 5
    MUL = 6
    DIV = 7
    ADD = 8
    SUB = 9
    ASSIGN = 10
    SEMI = 11

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'('", "')'", "'*'", "'/'", "'+'", "'-'", "'='", "';'" ]

    symbolicNames = [ "<INVALID>",
            "NUMBER", "ID", "WS", "MUL", "DIV", "ADD", "SUB", "ASSIGN", 
            "SEMI" ]

    ruleNames = [ "T__0", "T__1", "NUMBER", "ID", "WS", "MUL", "DIV", "ADD", 
                  "SUB", "ASSIGN", "SEMI" ]

    grammarFileName = "Expr.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


