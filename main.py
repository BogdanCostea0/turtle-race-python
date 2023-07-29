from turtle import Turtle, Screen
import random 


screen = Screen() # creates the screen
screen.setup(width=500, height=400) # sets the screen size

user_bet = screen.textinput(title= "make your bet", prompt="which turtle will win the race? enter a color:") # asks the user to make a bet

print(user_bet) # prints the user's bet

is_race_on = False

colors = ["red", "orange", "yellow", "green", "blue", "purple"] # list of colors
y_positions = [-100, -70, -40, -10, 20, 50] # list of y positions
names = ["tim", "tommy", "jerry", "jimmy", "jim", "joe"] # list of names
all_turtles = [] # list of all the turtles

def define_turtle(name, color, xpos, ypos): # function to define the turtle
    name = Turtle()
    name.shape("turtle")
    name.color(color)
    name.penup()
    name.goto(x= xpos, y = ypos)
    all_turtles.append(name)


for turtle_index in range(0,6): # for loop to define all the turtles
    define_turtle(name=names[turtle_index], color=colors[turtle_index], xpos= -230, ypos= y_positions[turtle_index])

if user_bet: 
    is_race_on = True

while is_race_on: # while loop to make the turtles move
    for turtle in all_turtles:
        if turtle.xcor() > 230: # if statement to check if the turtle has reached the end of the screen
            is_race_on = False # false flag to stop the while loop
            winner = turtle.pencolor()
            if winner == user_bet: # if statement to check if the user won or lost
                print(f"you've won! the {winner} turtle is the winner!")
            else:
                print(f"you've lost! the {winner} turtle is the winner!")
            

        random_distance = random.randint(0, 10)    # random distance for the turtle to move
        turtle.forward(random_distance) # moves the turtle forward

screen.exitonclick() # keeps the screen open until the user clicks on it