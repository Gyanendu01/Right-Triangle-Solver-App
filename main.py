import time
print("\n\tWelcome to the Right Triangle Solver")

def usr_input():
    usr_name = input("\n\tEnter your username: ")
    frst_leg = float(input("\n\tWhat is the first leg of the triangle: "))
    scnd_leg = float(input("\tWhat is the second leg of the triangle:  "))
    return frst_leg, scnd_leg, usr_name

def traingle_solve(frst_leg,scnd_leg,name):
    print("\n\tHello, {} Here is the desired solution")
    time.sleep(1)
    print("\n\tFor a triangle with legs of {} and {} the hypotenuse is {}.".format(frst_leg,scnd_leg,round(((frst_leg**2)+(scnd_leg**2))**0.5),3))
    print("\tFor a triangle with legs of 20 and 40.5 the area is 405.0.".format(frst_leg,scnd_leg,round(0.5*frst_leg*scnd_leg),3))


# Main function
usr_data = usr_input()
traingle_solve(usr_data[0],usr_data[1],usr_data[2])