exponet = "^"
multiplication = "*"
division = "/"
addition = "+"
subtraction = "-"
def evaluate(equation):

    filter = -1
    operator = []
    if exponet in equation:
        first_find = 0
        for letter in equation:
            operator.append (equation.find("^", first_find, first_find + 1))
            first_find += 1
        for number in operator:
            operator.remove(filter)
        operator.remove(filter)
        #replace with number
    print(operator)
    operator.clear()
    if multiplication in equation:
        first_find = 0
        for letter in equation:
            operator.append (equation.find("*", first_find, first_find + 1))
            first_find += 1
        for number in operator:
            operator.remove(filter)
        operator.remove(filter)
    if division in equation:
        first_find = 0
        for letter in equation:
            operator.append (equation.find("/", first_find, first_find + 1))
            first_find += 1
        for number in operator:
            operator.remove(filter)
        operator.remove(filter)
        #replace with number
    print(operator)
    operator.clear()
    if addition in equation:
        first_find = 0
        for letter in equation:
            operator.append (equation.find("+", first_find, first_find + 1))
            first_find += 1
        for number in operator:
            operator.remove(filter)
        operator.remove(filter)
    if subtraction in equation:
        first_find = 0
        for letter in equation:
            operator.append (equation.find("-", first_find, first_find + 1))
            first_find += 1
        for number in operator:
            operator.remove(filter)
        operator.remove(filter)
    print(operator)
    operator.clear()
example = "3*3-3"
evaluate(example)
