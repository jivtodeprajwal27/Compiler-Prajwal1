from dataclasses import dataclass
from typing import Optional
@dataclass
class ListLiteral:
    list_val:str
 
    

@dataclass
class ListOp:
    operator:str
    left:'AST'
    right:Optional['AST']=None
    

AST =ListLiteral|ListOp

def eval(program:'AST'):
    match program:
        case ListLiteral(val):
            return val
    return 0
l=ListLiteral([1,2,3])
print(eval(l))