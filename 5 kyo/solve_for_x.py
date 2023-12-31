"""
You will be given an equation as a string and you will need to solve for X and return x's value. 

Examples:

solve_for_x('x - 5 = 20') # should return 25
solve_for_x('20 = 5 * x - 5') # should return 5
solve_for_x('5 * x = x + 8') # should return 2
solve_for_x('(5 - 3) * x = x + 2') # should return 2

"""

def solve_for_x(equation):
    x = -200
    splitEquation = equation.split("=")  
    while ( eval(splitEquation[0]) != eval(splitEquation[1])):
        x += 1
    return(x)