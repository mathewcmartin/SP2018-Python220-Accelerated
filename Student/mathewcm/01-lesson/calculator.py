### Simple calculator

def f_get_number():
    return int(input('Enter an interger:'))


def f_get_operator():
    return int(input('Enter an operator +, -, *, /):'))


def f_calculate(number1, number2, operator):
    return number1+number2 if operator =='+'\
        else number1+number2 if operator =='*'\
        else number1+number2 if operator =='-'\
        else number1/number2
        else None


def f_main():
    return f_calculate(
    f_get_number(),
    f_get_operator(),
    f_get_number()
    )

print('The result is: %s' % f_main())
