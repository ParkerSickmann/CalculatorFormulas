# Ask for user input 1-9, 0 For list, and 1-9 correspond to different things like Surface Area, Volume, Area of 2D shape, Circle stuff (Sectors, Radius, Angles)

# ---- Formula Stuff ----

# Formula List
input_types = "Input 1 - Area | Input 2 - Surface Area | Input 3 - Volume | Input 4 - Relationship Between Ratios "
formulas = "Formula 1 - Area of a square | Formula 2 - Area of a trapezoid | Formula 3 - Area of a circle "
SA_formulas = "Formula 1 - Surface Area of a Prism | Formula 2 - Surface Area of a Cylinder | Formula 3 - Surface Area of a Pyramid | Formula 4 - Surface Area of a Cone | Formula 5 - Surface Area of a Sphere"
V_formulas = "Formula 1 - Volume of a Prism | Formula 2 - Volume of a Cylinder | Formula 3 - Volume of a Pyramid | Formula 4 - Volume of a Cone | Formula 5 - Volume of a Sphere"

# Area Formulas
formA1 = "b1*b2 or s^2"  # Area of a square
formA2 = "((b1+b2)*h)/2"  # Area of a trapezoid
formA3 = "πr^2"  # Area of a circle
formA4 = "(A*P)/2"  # Area of a Pentagon & Above
formA5 = "Formula 5"
formA6 = "Formula 6"
formA7 = "Formula 7"
formA8 = "Formula 8"
formA9 = "Formula 9"

# Surface Area Formulas
formSA1 = "2B+Ph"  # Surface Area of a Prism
formSA2 = "2(pi)r^2+2(pi)rh"  # Surface Area of a Cylinder
formSA3 = "B+((Pl)/2)"  # Surface Area of a Pyramid
formSA4 = "(pi)r^2+(pi)rl"  # Surface Area of a Cone
formSA5 = "4(pi)r^2"  # Surface Area of a Sphere

# Volume Formulas
formV1 = "B*h"  # Volume of a Prism
formV2 = "(pi)r^2*h"  # Volume of a Cylinder
formV3 = "(B*h)/3"  # Volume of a Pyramid
formV4 = "((pi)r^2*h)/3"  # Volume of a Cone
formV5 = "(4(pi)r^3)/3"  # Volume of a Sphere

# Relationship Between Ratios
ratio = "SR - A:B --- SAR - A^2:B^2 --- VR - A^3:B^3"

# ---- Gathers User's Input ----

first_input = input("Enter a number between 1 and 9. Enter 0 for formula types:")


def second_input():
    user_input = input("Enter a number between 1 and 9. Enter 0 for formula:")
    return user_input


# Prints the variable from the user's input
if first_input.isdigit() and 0 <= int(first_input) <= 9:
    num = int(first_input)

    if num == 0:
        print("Formula Types:")
        print(input_types)

    # Area Formulas
    elif num == 1:
        print("Area Formulas")
        second_input()
        if second_input().isdigit() and 1 <= int(second_input()) <= 9:
            num = int(second_input())

            if num == 0:
                print(SA_formulas)

            elif num == 1:
                print("Area of a Square")
                print(formA1)

            elif num == 2:
                print("Area of a Trapezoid")
                print(formA2)

            elif num == 3:
                print("Area of a Circle")
                print(formA3)

            elif num == 4:
                print("Area of a Pentagon & Above")
                print(formA4)

            elif num == 5:
                print("Not a valid formula number")

            elif num == 6:
                print("Not a valid formula number")

            elif num == 7:
                print("Not a valid formula number")

            elif num == 8:
                print("Not a valid formula number")

            elif num == 9:
                print("Not a valid formula number")

    # Surface Area
    elif num == 2:
        print("Surface Area Formulas")
        second_input()
        if second_input().isdigit() and 1 <= int(second_input()) <= 9:
            num = int(second_input())

            if num == 0:
                print(SA_formulas)

            elif num == 1:
                print("Surface Area of a Prism")
                print(formSA1)

            elif num == 2:
                print("Surface Area of a Cylinder")
                print(formSA2)

            elif num == 3:
                print("Surface Area of a Pyramid")
                print(formSA3)

            elif num == 4:
                print("Surface Area of a Cone")
                print(formSA4)

            elif num == 5:
                print("Surface Area of a Sphere")
                print(formSA5)

            elif num == 6:
                print("Not a valid formula number")

            elif num == 7:
                print("Not a valid formula number")

            elif num == 8:
                print("Not a valid formula number")

            elif num == 9:
                print("Not a valid formula number")

    # Volume
    elif num == 3:
        print("Volume Formulas")
        second_input()
        if second_input().isdigit() and 1 <= int(second_input()) <= 9:
            num = int(second_input())

            if num == 0:
                print(V_formulas)

            elif num == 1:
                print("Volume of a Prism")
                print(formV1)

            elif num == 2:
                print("Volume of a Cylinder")
                print(formV2)

            elif num == 3:
                print("Area of a Pyramid")
                print(formV3)

            elif num == 4:
                print("Volume of a Cone")
                print(formV4)

            elif num == 5:
                print("Volume of a Sphere")
                print(formV5)

            elif num == 6:
                print("Not a valid formula number")

            elif num == 7:
                print("Not a valid formula number")

            elif num == 8:
                print("Not a valid formula number")

            elif num == 9:
                print("Not a valid formula number")

    # Relationship Between Ratios
    elif num == 4:
        print("Relationship Between Ratios")
        print(ratio)

    elif num == 5:
        print("Not a formula type")

    elif num == 6:
        print("Not a formula type")

    elif num == 7:
        print("Not a formula type")

    elif num == 8:
        print("Not a formula type")

    elif num == 9:
        print("Not a formula type")

else:
    print("You did not enter a number between 0 and 9.")
