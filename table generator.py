from math import *
from numpy import *
x_cord = (
    (1),
    (2),
    (3),
    (4),
    (5)
)
def formula(a):
    transformations = "(-x)**.5"
    varplace = transformations.find("x")
    return transformations.replace("x", str(a))
for number in x_cord:
    expression = formula(number)
    print (expression)
    y = eval(expression)
    print (y.imag)
