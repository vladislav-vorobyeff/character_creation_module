from math import sqrt

message = 'Добро пожаловать в самую лучшую программу для вычисления'
'квадратного корня из заданного числа'


def calculate_square_root(Number):
    """Вычисляет квадратный корень."""
    return sqrt(Number)


def calc(your_number):
    """Проверяет, чтобы число не было меньше 0, и выводит результат."""
    if your_number <= 0:
        return 'Ваше число меньше 0'
    result = calculate_square_root(your_number)
    print(f'Мы вычислили квадратный корень из введённого '
          f'вами числа. Это будет: {result}')


print(message)
calc(25.5)
