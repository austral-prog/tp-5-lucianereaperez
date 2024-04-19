import math
def roots(a, b, c):
    discriminante = (b**2)-(4*a*c)
    if discriminante > 0 :
        r1= (-b + math.sqrt(discriminante))/(2*a)
        r2= (-b - math.sqrt(discriminante))/(2*a)
        return f"({r1}, {r2})"
       
    elif discriminante == 0:
        return f"({-b/(2*a)})"
    else :
        return "( )"
def value_y(a, b, c, x):
    y = a*(x**2)+(b*x)+c
    return y
def to_string(a, b, c):
    return f"f(x) = {a} * X^2 + {b} * X + {c}"
def derivation(a, b, c):
    return f"f'(x) = {2 * a}x + {b}"
roots(1, -3, 2) 
roots(1, -2, 1) 
roots(1, 2, 3)  
value_y(1, -3, 2, 0) 
value_y(1, -3, 2, 1) 
value_y(1, -3, 2, -1) 
to_string(2, -3, 1) 
derivation(2, -3, 1)
