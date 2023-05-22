#Ask for user input 1-9, 0 For list, and 1-9 correspond for differnt things like Surface Area, Volume, Area of 2d shape, Circle stuff (Sectors, Radius, Angles) 


#---- Formula Stuff ----

#Formula List
input_types = "Input 1 - Area | Input 2 - Surface Area | Input 3 - Volume | Input 4 - Relationship Between Ratios " 
formulas = "Formula 1 - Area of a square | Formula 2 - Area of a trapezoid | Formula 3 - Area of a circle " 
SA_formulas = "Formula 1 - Surface Area of a Prism | Formula 2 - Surface Area of a Cylinder | Formula 3 - Surface Area of a Pyramid | Formula 4 - Surface Area of a Cone | Formula 5 - Surface Area of a Sphere"

#Area Formulas
formA1 = "b1*b2 or s^2"   #Area of a square
formA2 = "((b1+b2)*h)/2"  #Area of a trapezoid
formA3 = "πr^2"           #Area of a circle
formA4 = "Formula 4"
formA5 = "Formula 5"
formA6 = "Formula 6"
formA7 = "Formula 7"
formA8 = "Formula 8"
formA9 = "Formula 9"

#Surface Area Formulas
formSA1 = "2B+Ph" #Surface Area of a Prism 
formSA2 = "2(pi)r^2+2(pi)rh" #Surface Area of a Cylinder
formSA3 = "B+((Pl)/2)" #Surface Area of a Pyramid
formSA4 = "(pi)r^2+(pi)rl" #Surface Area of a Cone
formSA5 = "4(pi)r^2" #Surface Area of a Sphere



#-----------------------

#---- Gathers User's Input ----

first_input = input("Enter a number between  1 and 9. Enter 0 for formula types:")

def second_input():
    user_input = input("Enter a number between  1 and 9. Enter 0 for formula:")

#------------------------------


#Prints the variable from user's input
if first_input.isdigit() and 0 <= int(first_input) <= 9:
    num = int(first_input)

    if num == 0:
        print("Formula Types:")
        print(input_types)

    #Area Formulas
    elif num == 1:
        print("Area Formulas")
        second_input()

    #Surface Area
    elif num == 2:
        print("Surface Area Formulas")
        second_input()
        if second_input.isdigit() and 1 <= int(second_input) <= 9:
            num = int(second_input)
            
            if num == 0:
                print(SA_formulas)

            if num == 1:
                print("Surface Area of a Prism")
                print(formSA1)

            elif num ==  2:
                print("Surface Area of a Cylinder")
                print(formSA2)

            elif num ==  3:
                print("Surface Area of a Pyramid")
                print(formSA3)

            elif num ==  4:
                print("Surface Area of a Cone")
                print(formSA4)    
        
            elif num ==  5:
                print("Surface Area of a Sphere")
                print(formSA5)
    #Volume
    elif num == 3:
        print("Volume Formulas")
        second_input()

    elif num == 4:
        print("Relationship Between Ratios")
        second_input()

    elif num == 5:
        second_input()

    elif num == 6:
        second_input()

    elif num == 7:
        second_input()

    elif num == 8:
        second_input()

    elif num == 9:
        second_input()

else:
    print("You did not enter a number between 0 and 9.")
