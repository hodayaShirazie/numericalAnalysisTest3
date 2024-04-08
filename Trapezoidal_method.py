import math
import sympy as sp
from sympy.utilities.lambdify import lambdify
from colors import bcolors

def error_t(f_e, a, b, error,n):
    h = (b - a) / n
    x = sp.symbols('x')
    #print("my_func: ", f_e) # my_func: x**3 + 2*x + 5
    df = sp.diff(f_e, x) # Derivation of my_f by x
    #print("f' : ", df) # print my_f1
    ddf = sp.diff(df, x)
    #print("f'' : ", ddf) # print my_f1
    f_tag_tag = lambdify(x, ddf)
    er=f_tag_tag(error)
    y = (1/12)*(b-a)*h**2
    finallError= y*er
    print("-----------------------------------------------------")
    print(bcolors.OKBLUE,"The Error: ", finallError,bcolors.ENDC)
    print("-----------------------------------------------------")


def trapezoidal_rule(f, a, b, n):

    h = (b - a) / n
    T = f(a) + f(b)
    integral = 0.5 * T

    for i in range(1, n):
        x_i = a + i * h
        integral += f(x_i)

    integral *= h

    return integral


def calc_trapez():
    xa = -1
    xb = 0.7
    g = lambda x: (3 * x ** 2 + math.sin(x ** 4 + 5 * x - 6)) / (2 * math.e ** (-2 * x + 5))
    n1 = 500
    n2 = 501


    result1 = trapezoidal_rule(g, xa, xb, n1)
    print(bcolors.OKBLUE, "n=",str(n1) )
    print(bcolors.OKBLUE, "Approximate integral:", result1, bcolors.ENDC)

    print("--------------------------------------------------------------")
    result2 = trapezoidal_rule(g, xa, xb, n2)
    print(bcolors.OKBLUE, "n=",str(n2) )
    print(bcolors.OKBLUE, "Approximate integral:", result2, bcolors.ENDC)



if __name__ == '__main__':
    calc_trapez()
