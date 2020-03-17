exponet = "^"
multiplication = "*"
division = "/"
addition = "+"
subtraction = "-"
def evaluate(equation):

    filter = -1
    operators = []
    if exponet in equation:
        first_find = 0
        for letter in equation:
            operators.append (equation.find("^", first_find, first_find + 1))
            first_find += 1
        for number in operators:
            try:
                operators.remove(filter)
            except:
                pass
        try:
            operators.remove(filter)
        except:
            pass
        #replace with number
        for  operator in operators:
            fnum = equation[operator-1]
            snum = equation[operator+1]
            answer = float(fnum)**float(snum)
    operators.clear()
    if multiplication in equation:
        first_find = 0
        for letter in equation:
            operators.append (equation.find("*", first_find, first_find + 1))
            first_find += 1
        try:
            operators.remove(filter)
        except:
            pass
        try:
            operators.remove(filter)
        except:
            pass
        for  operator in operators:
            fnum = equation[operator-1]
            snum = equation[operator+1]
            answer = float(fnum)*float(snum)
    if division in equation:
        first_find = 0
        for letter in equation:
            operators.append (equation.find("/", first_find, first_find + 1))
            first_find += 1
        for number in operators:
            try:
                operators.remove(filter)
            except:
                pass
        try:
            operators.remove(filter)
        except:
            pass
        for operator in operators:
            fnum = equation[operator-1]
            snum = equation[operator+1]
            answer = float(fnum)/float(snum)
        #replace with number
    print(operators)
    operators.clear()
    if addition in equation:
        first_find = 0
        for letter in equation:
            operators.append (equation.find("+", first_find, first_find + 1))
            first_find += 1
        try:
            operators.remove(filter)
        except:
            pass
    try:
        operators.remove(filter)
    except:
        pass
    for  operator in operators:
        fnum = equation[operator-1]
        snum = equation[operator+1]
        answer = float(fnum)+float(snum)
    if subtraction in equation:
        first_find = 0
        for letter in equation:
            operators.append (equation.find("-", first_find, first_find + 1))
            first_find += 1
        for number in example:
            try:
                operators.remove(filter)
            except:
                pass
        try:
            operators.remove(filter)
        except:
            pass
        for  operator in operators:
            fnum = equation[operator-1]
            snum = equation[operator+1]
            answer = float(fnum)-float(snum)
        operators.clear()
    print (answer)
example = "3-9"
evaluate(example)
