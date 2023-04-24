from fractions import Fraction
from dataclasses import dataclass,field
from typing import Optional, NewType, Mapping, List

currentID = 0

"""
    Creating data types for the language
"""
def fresh():
    global currentID
    currentID = currentID + 1
    return currentID

@dataclass
class NumType:
    pass

@dataclass
class BoolType:
    pass

@dataclass
class StringType:
    pass

@dataclass
class ListType:
    pass

@dataclass
class IntType:
    pass

class VarType:
    pass

@dataclass 
class FracType:
    pass


SimType = NumType | BoolType | StringType | ListType | IntType | FracType | VarType

"""
    Defining the structure of data types, conditionals, unary and 
    binary operators and loops.
"""

@dataclass
class NumLiteral:
    value: Fraction
    type: SimType = NumType
    # def __init__(self, *args):
    #     self.value = Fraction(*args)

@dataclass 
class IntLiteral:
    value: int
    type: SimType=IntType
    def __init__(self, *args):
        self.value = int(*args)

@dataclass 
class FracLiteral:
    value: Fraction
    type: SimType=FracType
    def __init__(self, *args):
        self.value = Fraction(*args)

@dataclass
class BoolLiteral:
    value: bool
    type: SimType =BoolType

@dataclass
class StringLiteral:
    value: str
    type: SimType=StringType
    

@dataclass
class BinOp:
    operator: str
    left: 'AST'
    right: 'AST'
    type: Optional[SimType] = None

@dataclass(frozen=True)
class Variable:
    name: str
    # id: int
    # localID:int
    type: SimType = VarType


    # def make(name):
    #     return Variable(name, fresh(), VarType)

    

@dataclass
class UnOp:
    operator: str
    vari : int

@dataclass
class LogOp:
    operator: str
    left: 'AST'
    right: Optional['AST']= None
    type: Optional[SimType] = None 

@dataclass
class PrintOp:
    inp: 'AST'


@dataclass
class StringOp:
    operator:str
    left:'AST'
    right:Optional['AST']=None
    type:Optional[SimType]=StringType
    
@dataclass
class StringSlice(StringOp):
    start: Optional[int] = None
    stop: Optional[int] = None
    step: Optional[int] = None
    type: Optional[SimType] = StringType
@dataclass
class Let:
    var: 'AST'
    e1: 'AST'
    e2: 'AST'
    type:SimType=None
class LetGlobal:
    var:'AST'
    e1:'AST'
    e2:Optional['AST']
@dataclass
class IfElse:
    condition: 'AST'
    iftrue: 'AST'
    iffalse: 'AST'
    type: Optional[SimType] = None

@dataclass
class ListLiteral:
    list_val:list
    type:SimType=ListType

@dataclass
class ListOp:
    operator:str
    left:'AST'
    right:Optional['AST']=None
    assign:Optional['AST']=None
    type:SimType=ListType

@dataclass
class Get:
    var: 'AST'

@dataclass
class Put:
    var: 'AST'
    e1: 'AST'

@dataclass
class LetConst:
    var: 'AST'
    e1: 'AST'
    e2: 'AST'

@dataclass
class Seq:
    things: List['AST']

@dataclass
class Un_boolify:
    left:'AST'
    type:SimType=NumType|StringType

@dataclass
class Whilethen:
    condition: 'AST'
    then_body: 'AST'
    

@dataclass
class For:
    condition:'AST'
    update:'AST'
    body:'AST'

@dataclass
class LetFun:
    name: 'AST'
    params: List['AST']
    body: 'AST'
    expr: 'AST'

@dataclass
class FunCall:
    fn: 'AST'
    args: List['AST']

@dataclass
class FnObject:
    params: List['AST']
    body: 'AST'
@dataclass
class If:
    cond: 'AST'
    body: 'AST'
    type: Optional[SimType] = None

"""
    Creating environment as a list of dictionaries which ensures
    scoping is done correctly.
"""
class Environment:
    envs: List

    def __init__(self):
        self.envs = [{}]

    def enter_scope(self):
        self.envs.append({})

    def exit_scope(self):
        assert self.envs
        self.envs.pop()

    def add(self, name, value):
        assert name not in self.envs[-1]
        self.envs[-1][name] = value

    def get(self, name):
        for env in reversed(self.envs):
            if name in env:
                return env[name]
        raise KeyError()

    def update(self, name, value):
        for env in reversed(self.envs):
            if name in env:
                env[name] = value
                return
        raise KeyError()
    
"""
    AST here has the different types of node
    value it can have.

    Value defined here is return value from
    the eval function below.
"""

AST = NumLiteral | BoolLiteral | BinOp | IfElse | StringLiteral | StringOp|LogOp|ListLiteral|IntLiteral|FracLiteral|ListOp| Get | Put |Let | LetConst |Seq | Whilethen |For | Variable|LetFun | FunCall
Value = Fraction|FnObject
TypedAST = NewType('TypedAST', AST)

class TypeError(Exception):
    pass
Binary_operators  = "+ - * / % ** // ".split()
Binary_operators_comparision = "== != < > <= >=".split()
# Since we don't have variables, environment is not needed.


"""
    Typechecking the data types, binary operations, unary operations,
    let, conditionals and loops for ensuring operations are 
    performed between correct data types.

"""
def typecheck(program: AST, env = None) -> TypedAST:
    match program:
        case NumLiteral() as t: # already typed.
            return t
        case BoolLiteral() as t: # already typed.
            return t
        case StringLiteral() as t:
            return t
        case IntLiteral() as t:
            return t
        case FracLiteral() as t:
            return t
        case ListLiteral() as t:
            return t
        case Variable() as V:
            return V
        case BinOp(op, left, right) if op in   Binary_operators or Binary_operators_comparision:
            tleft = typecheck(left)
            tright = typecheck(right)
            print(tleft, tright)
            Binop_list_Comp = [NumType, StringType, VarType]
            Binop_list__op = [NumType, VarType]
            if op in Binary_operators:
                if tleft.type in Binop_list__op and tright.type in Binop_list__op:
                    # print(f"left: {tleft}.type")
                    # print(f"right: {tright}.type")
                    return BinOp(op, left, right, NumType)
                raise TypeError()
                
            else:
                if(tleft.type in  Binop_list_Comp  and tright.type in Binop_list_Comp ):
                    return BinOp(op, left, right, BoolType)
                # if(tleft.type == StringType and tright.type == StringType):
                #     return BinOp(op,left,right,BoolType)
                # if(tleft.type == VarType and tright.type == VarType):
                #     return BinOp(op,left,right,BoolType)
                raise TypeError()
        case Let(var, num_val, expr):
            t_var = typecheck(var)
            t_num_val = typecheck(num_val)
            t_expr = typecheck(expr)
            
            type_num_val = [NumType , StringType]
            if(t_num_val.type not in type_num_val ):
                raise TypeError()
            
            return Let(t_var, t_num_val,t_expr,t_num_val.type)
        
        case UnOp('-',vari):
            tvari=typecheck(vari)
            if tvari.type != NumType:
                raise TypeError() 
            return UnOp("++",vari,NumType)
            
        case UnOp('++',vari):
            tvari=typecheck(vari)
            if tvari.type != NumType:
                raise TypeError()
            return UnOp("++",vari,NumType)
            
        case UnOp('--',vari):
            tvari=typecheck(vari)
            if tvari.type != NumType:
                raise TypeError()
            return UnOp("++",vari,NumType)

        case PrintOp(inp):
            if inp==None:
                raise TypeError()
        case IfElse(c, t, f): # We have to typecheck both branches.
            tc = typecheck(c)
            if tc.type != BoolType:
                raise TypeError()
            tt = typecheck(t)
            tf = typecheck(f)
            if tt.type != tf.type: # Both branches must have the same type.
                raise TypeError()
            return IfElse(tc, tt, tf, tt.type) # The common type becomes the type of the if-else.
        case StringSlice("slice",left,start, stop, step):
            tleft = typecheck(left)
            if tleft.type != StringType:
                raise TypeError()
            return StringSlice("slice", left, start, stop, step, StringType)
        
        case StringOp('add',left,right):
            tleft=typecheck(left)
            tright=typecheck(right)
            if tleft.type!=StringType or tright.type!=StringType:
                raise TypeError()
            return StringOp("add",left,right)
        
        case StringOp('compare',left,right):
            tleft=typecheck(left)
            tright=typecheck(right)
            if tleft.type!=StringType or tright.type!=StringType:
                raise TypeError()
            return StringOp("compare",left,right,BoolType)


        case StringOp('length',left):
            tleft=typecheck(left)
            if tleft.type!=StringType:
                raise TypeError()
            return StringOp("length",left,type=NumType)
        
        case Un_boolify(left):
            tleft=typecheck(left)
            if tleft.type!=NumType or StringType:
                raise TypeError()
            return Un_boolify(left)
         
        
    raise TypeError()



"""
    Defining an exception to raise in case of Invalid Program.
"""

class InvalidProgram(Exception):
    pass

"""
    Eval Function evaluates the AST and returns Value. 
"""


def eval(program: AST, environment: Environment = None) -> Value:
  
    if environment is None:
        environment =Environment()
    
    # Pass environment to all explicitally
    def eval2(program):
        return eval(program, environment)
    
    # always call eval2 for enviornment passing instead of eval(program, envi)
    match program:

        # Here the value of data types
        # are simply returned if they are encountered.

        case NumLiteral(value):
            return value
        case StringLiteral(value):
            return value
        case IntLiteral(value):
            return value
        case FracLiteral(value):
            return value
        case Variable(_) as v:
            return environment.get(v)
        case ListLiteral(value):
            # print(f'values: {value}')
            return value
        case BoolLiteral(value):
            return value
        

        
        # Let is used to create new bindings
        # after evaluating the first expression
        # it creates a new scope where second
        # expression is evaluated. Same is the
        # case with LetConst with exception that
        # it cannot be redefined.

        case Let(Variable(_) as v, e1, e2):
            v1 = eval2(e1)
            environment.enter_scope()
            environment.add(v, v1)
            v2 = eval2(e2)
            environment.exit_scope()
            return v2
         
        case LetConst(Variable(name),e1,e2):
            v1 = eval2(e1)
            if(environment.check(name) != None):
                print("Variable name exists")
                raise InvalidProgram()
            environment.enter_scope()
            environment.add(name,v1)
            v2 = eval2(e2)
            environment.exit_scope()
            return v2
        
        # Put is used to update value of the variable
        case Put(Variable(_) as v, e):
            environment.update(v, eval2(e))
            return environment.get(v)
        
        # Get is used to retreive the value of the variable
        case Get(Variable(_) as v):
            return environment.get(v)
        case Seq(things):
            v = None
            for thing in things:
                v = eval2(thing)
            return v
        
        # Binary Operators
        case BinOp("+", left, right):
            return eval2(left) + eval2(right)
        case BinOp("-", left, right):
            return eval2(left) - eval2(right)
        case BinOp("*", left, right):
            return eval2(left) * eval2(right )
        case BinOp("/", left, right):
            if(right==0):
                raise InvalidProgram()
            return  eval2(left ) /  eval2(right )
            
        case BinOp("//", left, right):
            if(right==0):
                raise InvalidProgram()
            return  eval2(left ) //  eval2(right )
        case BinOp("%", left, right):
            if(right==0):
                raise InvalidProgram()
            return  eval2(left ) %  eval2(right )
        case BinOp("**", left, right):
            return  eval2(left ) **  eval2(right )
        case BinOp("==",left,right):
            return  eval2(left ) ==  eval2(right )
        case BinOp("<",left,right):
            return  eval2(left ) <  eval2(right )
        case BinOp(">",left,right):
            return  eval2(left ) >  eval2(right )
        case BinOp(">=",left,right):
            return  eval2(left ) >=  eval2(right )
        case BinOp("<=",left,right):
            return  eval2(left ) <=  eval2(right )
        case BinOp("!=",left,right):
            return  eval2(left ) !=  eval2(right )
    
        # Bitwise Operators With type checking
        case BinOp("&",left,right):
            left_type=typecheck(left).type
            right_type=typecheck(right).type
            
            if(left_type!=NumType or right_type!=NumType):
                raise InvalidProgram()
            return int( eval2(left )) & int( eval2(right ))
        case BinOp("|",left,right):
            left_type=typecheck(left).type
            right_type=typecheck(right).type
            
            if(left_type!=NumType or right_type!=NumType):
                print(left_type)
                print(right_type)
                raise InvalidProgram()
            return int( eval2(left )) | int( eval2(right ))
        case BinOp("^",left,right):
            left_type=typecheck(left).type
            right_type=typecheck(right).type
            
            if(left_type!=NumType or right_type!=NumType):
                print(left_type) 
                print(right_type)
                raise InvalidProgram()
            return int( eval2(left )) ^ int( eval2(right ))
        case BinOp(">>",left,right):
            left_type=typecheck(left).type
            right_type=typecheck(right).type
            
            if(left_type!=NumType or right_type!=NumType):
                print(left_type)
                print(right_type)
                raise InvalidProgram()
            return int( eval2(left )) >> int( eval2(right ))
        case BinOp("<<",left,right):
            left_type=typecheck(left).type
            right_type=typecheck(right).type
            
            if(left_type!=NumType or right_type!=NumType):
                print(left_type)
                print(right_type)
                raise InvalidProgram()
            return int( eval2(left )) << int( eval2(right ))
        
        # Addition Assignment Operator
        case BinOp("+=",left,right):
            left_type=typecheck(left).type
            right_type=typecheck(right).type
            rtype=[NumType,VarType]
            if(left_type!=VarType or right_type not in rtype):
                raise InvalidProgram()
            val=eval2(Get(left))
            new_val=val+(eval2(right))
            eval2(Put(left,NumLiteral(new_val)))
            return eval2(NumLiteral(new_val))

        case PrintOp(inp):
            print(eval2(inp))
            return 
  
        # String Operations
        # with string typecheck 

        case StringOp('add',left,right):
            left_type=typecheck(left).type
            right_type=typecheck(right).type
            types=[VarType,StringType]
            if(left_type not in types or right_type not in types):
                raise InvalidProgram()
            return  f"{eval2(left )}{eval2(right )}"
        
        case StringOp('compare',left,right):
            left_type=typecheck(left).type
            right_type=typecheck(right).type
            if(left_type!=StringType or right_type!=StringType):
                raise InvalidProgram()
            return eval2(BoolLiteral(eval2(left)==eval2(right)))

        case StringOp('length',left):
            left_type=typecheck(left).type
            if(left_type!=StringType):
                raise InvalidProgram()
            return len(eval2(left))        

        case StringSlice("slice", left,start, stop,step):
            left_value =  eval2(left )
            return left_value[eval2(start):eval2(stop):eval2(step)]
        

        #unary Operations including unary negation, addition, subtraction
        case UnOp('-',vari):
            un= eval2(vari )
            un=-un
            eval2(Put(vari,NumLiteral(un)))
            return  eval2(NumLiteral(un) )
        case UnOp('++',vari):
            un= eval2(vari )
            un=un+1
            eval2(Put(vari,NumLiteral(un)))
            return  eval2(NumLiteral(un) )
        case UnOp('--',vari):
            un= eval2(vari )
            un=un-1
            eval2(Put(vari,NumLiteral(un)))
            return  eval2(NumLiteral(un) )
        
        case LogOp("and",left,right):
            return eval2(left ) and eval2(right)
        case LogOp("or",left,right):
            return eval2(left ) or eval2(right)
        case LogOp("not",right):
            return not eval2(right)
        

    
        #Only If
        case If(c,b):
            condition_eval= eval2(c)
            if(condition_eval==True):
                return  eval2(b)
            else:
                return 

        # IfElse
        case IfElse(c,l,r):
        
            condition_eval= eval2(c)

            if(condition_eval==True):
                return  eval2(l)
            else:
                return  eval2(r)
        
        # List Operations 

        case ListOp("append",left,right):
            
            
            l= eval2(left)
            r= eval2(right)
            if(type(r)==Fraction):
                l.append(int(r))
            else:
                l.append(r)
            return l
            

        case ListOp('length',left):
            return len( eval2(left))

        case ListOp('assign',array,index,assign):
            # if(typecheck(assign).type!=array.type or typecheck(index).type!=NumType):
            #     raise InvalidProgram
            arr= eval2(array)
            
            arr[int( eval2(index))]=int( eval2(assign))
            return arr
        
        case ListOp('remove',array):
            arr= eval2(array)
            arr.pop()
            return arr


        case ListOp('remove',array,index):
            if(index!=NumType):
                raise InvalidProgram
            arr= eval2(arr)

        case ListOp('pop',array,index):
            if(index!=NumType):
                raise InvalidProgram
            arr= eval2(array)
            arr.remove(index)
            return arr
        case ListOp('get',array,index):

            if(int(eval2(index))>=len(eval2(array))): raise InvalidProgram()

            return eval2(array)[int(eval2(index))]
        

        case Un_boolify(left):
            left_var=eval(left,environment)
            if left_var==0:
                return bool(left_var)
            elif left_var:
                return bool(left_var)
            elif len(left_var)==0:
                return bool(left_var)
            return bool(left_var)
        
        # For Loop and While Loop 
        
        case For(condition, update, body):
            while eval2(condition):
                environment.enter_scope()
                eval2(body)
                eval2(update)
                environment.exit_scope()
            return
        
        case Whilethen(condition,then_body):
            environment.enter_scope()
            condi = eval2(condition)
            while(condi == True):
                eval2(then_body)
                condi = eval2(condition)
                if(condi == False):
                    break
            environment.exit_scope()
            return
        
        # Functions are defined such that there are two 
        # Classes one for defining(LetFun) the functions with all its
        # parameters and body while other(FunCall) is used for calling it.

        case LetFun(Variable(_) as v, params, body, expr):
            environment.enter_scope()
            environment.add(v, FnObject(params, body))
            v = eval2(expr)
            environment.exit_scope()
            return v
        
        case FunCall(Variable(_) as v, args):
            fn = environment.get(v)
            argv = []
            for arg in args:
                argv.append(eval2(arg))
            environment.enter_scope()
            for param, arg in zip(fn.params, argv):
                environment.add(param, arg)
            v = eval2(fn.body)
            environment.exit_scope()
            return v
           
        
        
    raise InvalidProgram()




