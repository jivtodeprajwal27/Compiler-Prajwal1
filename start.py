from fractions import Fraction
from dataclasses import dataclass
from typing import Optional, NewType, Mapping

# A minimal example to illustrate typechecking.

@dataclass
class NumType:
    pass

@dataclass
class BoolType:
    pass


SimType = NumType | BoolType

@dataclass
class NumLiteral:
    value: Fraction
    type: SimType = NumType
    def __init__(self, *args):
        self.value = Fraction(*args)

@dataclass
class BoolLiteral:
    value: bool
    type: SimType =BoolType

    


@dataclass
class BinOp:
    operator: str
    left: 'AST'
    right: 'AST'
    type: Optional[SimType] = None

@dataclass
class Variable:
    name: str


@dataclass
class Let:
    var: 'AST'
    e1: 'AST'
    e2: 'AST'

@dataclass
class IfElse:
    condition: 'AST'
    iftrue: 'AST'
    iffalse: 'AST'
    type: Optional[SimType] = None

AST = NumLiteral | BoolLiteral | BinOp | IfElse 


TypedAST = NewType('TypedAST', AST)

class TypeError(Exception):
    pass

# Since we don't have variables, environment is not needed.
def typecheck(program: AST, env = None) -> TypedAST:
    match program:
        case NumLiteral() as t: # already typed.
            return t
        case BoolLiteral() as t: # already typed.
            return t
        
        case BinOp(op, left, right) if op in ["+", "*"]:
            tleft = typecheck(left)
            tright = typecheck(right)
            
            if tleft.type != NumType or tright.type != NumType:
                print(f"left: {tleft}.type")
                print(f"right: {tright}.type")
                raise TypeError()
            return BinOp(op, left, right, NumType)
        case BinOp("<", left, right):
            tleft = typecheck(left)
            tright = typecheck(right)
            if tleft.type != NumType or tright.type != NumType:
                raise TypeError()
            return BinOp("<", left, right, BoolType)
        case BinOp("=", left, right):
            tleft = typecheck(left)
            tright = typecheck(right)
            if tleft.type != tright.type:
                raise TypeError()
            return BinOp("=", left, right, BoolType)
        case IfElse(c, t, f): # We have to typecheck both branches.
            tc = typecheck(c)
            if tc.type != BoolType:
                raise TypeError()
            tt = typecheck(t)
            tf = typecheck(f)
            if tt.type != tf.type: # Both branches must have the same type.
                raise TypeError()
            return IfElse(tc, tt, tf, tt.type) # The common type becomes the type of the if-else.
    raise TypeError()
Value = Fraction

class InvalidProgram(Exception):
    pass


    

def eval(program: AST, environment: Mapping[str, Value] = None) -> Value:
    if environment is None:
        environment = {}
    match program:
        case NumLiteral(value):
            return value
        
        case Variable(name):
            if name in environment:
                return environment[name]
            raise InvalidProgram()
        case Let(Variable(name), e1, e2):
            v1 = eval(e1, environment)
            return eval(e2, environment | { name: v1 })
        case BinOp("+", left, right):
            return eval(left, environment) + eval(right, environment)
        case BinOp("-", left, right):
            return eval(left, environment) - eval(right, environment)
        case BinOp("*", left, right):
            return eval(left, environment) * eval(right, environment)
        case BinOp("/", left, right):
            return eval(left, environment) / eval(right, environment)

        
    raise InvalidProgram()


def test_typecheck():
    import pytest
    te = typecheck(BinOp("+", NumLiteral(2), NumLiteral(3)))
    assert te.type == NumType()
    te = typecheck(BinOp("<", NumLiteral(2), NumLiteral(3)))
    assert te.type == BoolType()
    with pytest.raises(TypeError):
        typecheck(BinOp("+", BinOp("*", NumLiteral(2), NumLiteral(3)), BinOp("<", NumLiteral(2), NumLiteral(3))))
