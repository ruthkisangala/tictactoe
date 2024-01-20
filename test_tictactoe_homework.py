import pytest

from tictactoe_new import evaluate, move

#Tests for evaluate

def test_evaluate_player_win():
    assert evaluate("x"*3 + "-"*17, "x") == "x"

def test_evaluate_draw():
    assert evaluate("xo"*10, "o") == "!"

def test_evaluate_continue():
    assert evaluate("xo"*9 + "x" + "-", "x") == "-"

def test_few_arguments():
    with pytest.raises(TypeError):
       evaluate("-"*20)

def test_invalid_arguments():
    with pytest.raises(TypeError):
       evaluate("-"*20, True)

def test_right_mark():
    assert evaluate("x"*3 + "-"*17, "x") != "o"

#Tests for move

def test_normal_move():
    board = move(20*"-","x", 2)
    assert board.count("-") == 19
    assert board == "-" + "x" + "-"*18

def test_negative_number():
    assert move(20*"-", "x", -5) == ("-"*14 + "x" + "-"*5)
    
def test_higher_twenty():
    assert move(20*"-", "x", 21) == False

def test_position_no_integer():
    with pytest.raises(TypeError):
        move(20*"-", "x", "b")

'''
a) A module is a self-contained piece of code that can be utilized directly in other code. 
It aids in avoiding the need to repeatedly program or write the same code and functions. 
An example is the Math module, which includes functions for calculating the sine or cosine, for instance.

A package consists of multiple submodules. 
It is not necessary to call the entire package, you can also use individual submodules.

b) Side effects are anything that creats an output, for example, print(). They should be avoided. 
They are only executed the first time when a module is imported. 
Another side effect would be modifying global variables. 

c) Exceptions are raised errors. 
We can see in the message what kind of error it is, can solve it. 
Or we can use try and except, so the code won't be interrrupted.

d)
Create: define an exception as a class
Throw: defines when an exception is raised ("raise")
Catch: with "try" and "except" it can be tried out and catched if it is an exception

e) 
- to find bugs. 
- for example if some parameters are changed, we don't have to write a complete new code to test it. 
- for larger projects to see where the bug is

'''