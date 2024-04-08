from colors import bcolors
from polinomial_interpolation_guess_elimination import calc_polinomial_guessian
from Trapezoidal_method import calc_trapez





def printInput():
    print(bcolors.HEADER + "INPUT: " + bcolors.ENDC)
    print("part 1:\ntable_points = [(1.2, -3.5), (1.3, -3.69), (1.4,0.9043), (1.5,1.1293), (1.6,2.3756)]")
    print("xa=1.35, xb=1.55 ")
    print("part 2:\n g = lambda x: (3*x**2 + math.sin(x**4 + 5*x -6))/(2*math.e**(-2*x + 5)) ")

def printDetails():
    print(bcolors.HEADER + "date: " + bcolors.ENDC +"8/4/24\n" + bcolors.HEADER + "group members:\n" + "(1)" + bcolors.ENDC + " name: Shulamit-mor-yossef. id: 206576977.\n" +
          bcolors.HEADER + "(2)" + bcolors.ENDC + " name: Zohar-monsonego. id: 214067662.\n" +
          bcolors.HEADER + "(3)" + bcolors.ENDC + " name: hodaya-shirazie. id: 213907785.\n" +
          bcolors.HEADER + "submitted by: " + bcolors.ENDC + "name: Hodaya-shirazie. id: 213907785.")
    printInput()





if __name__ == '__main__':

    printDetails()
    print(bcolors.HEADER + "OUTPUT: " + bcolors.ENDC)
    print("--------------------------------------------------------")

    calc_polinomial_guessian()
    print("--------------------------------------------------------")

    xa = -1.0779
    xb = 0.71974
    calc_trapez()


