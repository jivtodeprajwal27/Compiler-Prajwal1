from start import *

def test_div_operator():
    a  = Variable("a")
    n1= NumLiteral(5)
    e2 = BinOp("/", a, a)
    e  = Let(a, n1, e2)
    assert eval(e) == 1

    b = Variable("b")
    n2 = NumLiteral(10)
    e2 = BinOp("/", b, a)
    e  = Let(a, n1, Let(b, n2,e2 ))
    assert eval(e) == 2

    """
    should show error if divided by zero. 
    """
    # c = Variable("c")
    # n0 = NumLiteral(0)
    # e2 = BinOp("/", b, c)
    # e  = Let(c, n0, Let(b, n2,e2 ))
    # assert eval(e) == InvalidProgram


def test_modulus_operator():
    a  = Variable("a")
    n1= NumLiteral(5)
    e2 = BinOp("%", a, a)
    e  = Let(a, n1, e2)
    assert eval(e) == 0

    b = Variable("b")
    n2 = NumLiteral(11)
    e2 = BinOp("%", b, a)
    e  = Let(a, n1, Let(b, n2,e2 ))
    assert eval(e) == 1

def test_floor_div_operator():
    a  = Variable("a")
    n1= NumLiteral(5)
    e2 = BinOp("//", a, a)
    e  = Let(a, n1, e2)
    assert eval(e) == 1

    b = Variable("b")
    n2 = NumLiteral(15)
    e2 = BinOp("//", b, a)
    e  = Let(a, n1, Let(b, n2,e2 ))
    assert eval(e) == 3

def test_power_operator():
    a  = Variable("a")
    n1= NumLiteral(3)
    e2 = BinOp("**", a, a)
    e  = Let(a, n1, e2)
    assert eval(e) == 27

    b = Variable("b")
    n2 = NumLiteral(10)
    e2 = BinOp("**", b, a)
    e  = Let(a, n1, Let(b, n2,e2 ))
    assert eval(e) == 1000

    """ Show an error of Invalid program from line 136"""
    # c = Variable("c")
    # n3 = NumLiteral(0)
    # e2 = BinOp("**", a, c)
    # e  = Let(a, n1, Let(b, n2,e2 ))
    # assert eval(e) == 0

    
def test_equal_operator():
    a  = Variable("a")
    n1= NumLiteral(3)
    e2 = BinOp("==", a, a)
    e  = Let(a, n1, e2)
    assert eval(e) == True

    b = Variable("b")
    n2 = NumLiteral(10)
    e2 = BinOp("==", b, a)
    e  = Let(a, n1, Let(b, n2,e2 ))
    assert eval(e) == False

def test_not_equal_operator():
    a  = Variable("a")
    n1= NumLiteral(3)
    e2 = BinOp("!=", a, a)
    e  = Let(a, n1, e2)
    assert eval(e) == False

    b = Variable("b")
    n2 = NumLiteral(10)
    e2 = BinOp("!=", b, a)
    e  = Let(a, n1, Let(b, n2,e2 ))
    assert eval(e) == True

def test_greter_than_operator():
    a  = Variable("a")
    n1= NumLiteral(3)
    e2 = BinOp(">", a, a)
    e  = Let(a, n1, e2)
    assert eval(e) == False

    b = Variable("b")
    n2 = NumLiteral(10)
    e2 = BinOp(">", b, a)
    e  = Let(a, n1, Let(b, n2,e2 ))
    assert eval(e) == True

def test_greter_than_equal_operator():
    a  = Variable("a")
    n1= NumLiteral(3)
    e2 = BinOp(">=", a, a)
    e  = Let(a, n1, e2)
    assert eval(e) == True

    b = Variable("b")
    n2 = NumLiteral(10)
    e2 = BinOp(">=", b, a)
    e  = Let(a, n1, Let(b, n2,e2 ))
    assert eval(e) == True

    c = Variable("c")
    n3 = NumLiteral(9)
    e2 = BinOp(">=", c, b)
    e  = Let(c, n3, Let(b, n2,e2 ))
    assert eval(e) == False

def test_less_than_operator():
    a  = Variable("a")
    n1= NumLiteral(3)
    e2 = BinOp("<", a, a)
    e  = Let(a, n1, e2)
    assert eval(e) == False

    b = Variable("b")
    n2 = NumLiteral(10)
    e2 = BinOp("<", b, a)
    e  = Let(a, n1, Let(b, n2,e2 ))
    assert eval(e) == False

    c = Variable("c")
    n3 = NumLiteral(9)
    e2 = BinOp("<", c, b)
    e  = Let(c, n3, Let(b, n2,e2 ))
    assert eval(e) == True

def test_less_than_equal_operator():
    a  = Variable("a")
    n1= NumLiteral(3)
    e2 = BinOp("<=", a, a)
    e  = Let(a, n1, e2)
    assert eval(e) == True

    b = Variable("b")
    n2 = NumLiteral(10)
    e2 = BinOp("<=", b, a)
    e  = Let(a, n1, Let(b, n2,e2 ))
    assert eval(e) == False

    c = Variable("c")
    n3 = NumLiteral(9)
    e2 = BinOp("<=", c, b)
    e  = Let(c, n3, Let(b, n2,e2 ))
    assert eval(e) == True


test_div_operator()
test_modulus_operator()
test_power_operator()
test_floor_div_operator()
test_equal_operator()
test_not_equal_operator()
test_greter_than_operator()
test_less_than_operator()
test_less_than_equal_operator()