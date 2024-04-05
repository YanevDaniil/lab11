from flask import Flask, render_template
import re, math


app = Flask(__name__)

@app.route('/')
def mainpage():
    return render_template('main_page.html')

@app.route('/arithmetic/')
def arithmetic_empty():
    return "Нет выражения"


@app.route('/arithmetic/<action>/')
def arithmetic(action):

    array = re.split('(\*\*|sqrt|\*|-|\+|!|::|:)', action)

    if len(array) != 3:
        return f"Некорректное  выражение {array}"

    try:
        a_num = float(array[0])
        b_num = float(array[2])
        oper = array[1]

        if oper == "+":
            result = a_num + b_num
            return f"{a_num} {oper} {b_num} = {result}"

        if oper == "-":
            result = a_num - b_num
            return f"{a_num} {oper} {b_num} = {result}"

        if oper == "*":
            result = a_num * b_num
            return f"{a_num} {oper} {b_num} = {result}"

        if oper == ":":
            if b_num == 0.0:
                return "Деление на 0 невозможно"
            result = a_num / b_num
            return f"{a_num} {oper} {b_num} = {result}"

        if oper == "**":
            result = a_num ** b_num
            return f"{a_num} {oper} {b_num} = {result}"

        if oper == "sqrt":
            result = a_num ** (1.0 / b_num)
            return f"{a_num} {oper} {b_num} = {result}"

        if oper == "!":
            result = a_num % b_num
            return f"{a_num} {oper} {b_num} = {result}"

        if oper == "::":
            result = float(int(a_num / b_num))
            return f"{a_num} {oper} {b_num} = {result}"

    except:
        return "Операция не поддерживается"



@app.route('/trigonometric/')
def trigonometric_rad_empty():
    return "Нет выражения (радианы)"

@app.route('/trigonometric/deg')
def trigonometric_deg_empty():
    return "Нет выражения (градусы)"

@app.route('/trigonometric/<action>/')
def trigonometric_rad(action):
    array = re.split('(sin|cos|tg|asin|acos|atg)', action)

    if len(array) != 3 or array[0] != "":
        return "Некорректное  выражение"

    try:
        float(array[2])
    except:
        return "Некорректное  выражение"


    num = float(array[2])
    oper = array[1]


    if oper == "sin":
        result = math.sin(num)
        return f"sin({num}) = {result}"

    if oper == "cos":
        result = math.cos(num)
        return f"cos({num}) = {result}"

    if oper == "tg":
        result = math.tan(num)
        return f"tg({num}) = {result}"

    if oper == "asin":
        try:
            result = math.asin(num)
            return f"asin({num}) = {result}"
        except:
            return f"asin({num}) = Undefined"

    if oper == "acos":
        try:
            result = math.acos(num)
            return f"acos({num}) = {result}"
        except:
            return f"acos({num}) = Undefined"

    if oper == "atg":
        result = math.atan(num)
        return f"atg({num}) = {result}"


@app.route('/trigonometric/deg/<action>/')
def trigonometric_deg(action):
    array = re.split('(sin|cos|tg|asin|acos|atg)', action)

    if len(array) != 3 or array[0] != "":
        return "Некорректное  выражение"

    try:
        float(array[2])
    except:
        return "Некорректное  выражение"

    num = float(array[2])
    degrees = num * math.pi / 180.0

    oper = array[1]

    if oper == "sin":
        result = math.sin(degrees)
        return f"sin({num}°) = {result}"

    if oper == "cos":
        result = math.cos(degrees)
        return f"cos({num}°) = {result}"

    if oper == "tg":
        result = math.tan(degrees)
        return f"tg({num}°) = {result}"

    if oper == "asin":
        try:
            result = math.asin(degrees)
            return f"asin({num}°) = {result}"
        except:
            return f"asin({num}°) = Undefined"

    if oper == "acos":
        try:
            result = math.acos(degrees)
            return f"acos({num}°) = {result}"
        except:
            return f"acos({num}°) = Undefined"

    if oper == "atg":
        result = math.atan(degrees)
        return f"atg({num}°) = {result}"


if __name__ == "__main__":
    app.run()