import cmath
import math
import sys

"""print_unicode_ans.py

    Takes users input and prints into file the Unicode symbols which contain in description the inputted words.

"""

__author__ = "maydee"

SQUARED = "\N{SUPERSCRIPT TWO}"
ARROW = "\N{RIGHTWARDS ARROW}"
if not sys.platform.startswith("linux"):
    SQUARED = "^2"
    ARROW = "->"


def get_float(msg, allow_zero):
    x = None
    while x is None:
        try:
            x = float(input(msg))
            if not allow_zero and abs(x) < sys.float_info.epsilon:
                print("zero is not allowed")
                x = None
        except ValueError as err:
            print(err)
    return x


print("ax" + SQUARED + " + bx + c = 0")
a = get_float("enter a: ", False)
b = get_float("enter b: ", True)
c = get_float("enter c: ", True)

x1 = None
x2 = None
discriminant = (b ** 2) - (4 * a * c)
if discriminant == 0:
    x1 = -(b / (2 * a))
else:
    if discriminant > 0:
        root = math.sqrt(discriminant)
    else: # discriminant < 0
        root = cmath.sqrt(discriminant)
    x1 = (-b + root) / (2 * a)
    x2 = (-b - root) / (2 * a)

equation = ("{a}x{SQUARED} + {b}x + {c} = 0 {ARROW} x = {x1}"
            .format(**locals()))
if x2 is not None:
    equation += " or x = {0}".format(x2)
print(equation)
