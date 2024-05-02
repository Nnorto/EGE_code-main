import turtle
import math
import time

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400
CANNON_X = -300  # Keep the cannon's X-coordinate unchanged
CANNON_Y = -7  # Move the cannon to the center along the Y-coordinate
SHOT_SPEED = 5 #СКОРОСТЬ
ANGLE_DEGREES = 45 #УГОЛ
print("СКОРОСТЬ")
SHOT_SPEED = int(input())
print("УГОЛ")
ANGLE_DEGREES = int(input())


# Set up the screen
screen = turtle.Screen()
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen.title("Cannon Shot")
ground1 = turtle.Turtle()
ground1.speed(0)
ground1.penup()
ground1.goto(0,-235)  # Position for the first wheel
ground1.pendown()
ground1.shape("square")
ground1.color("green")
ground1.shapesize(stretch_wid=20, stretch_len=50)  # Make it smaller

sky1 = turtle.Turtle()
sky1.speed(0)
sky1.penup()
sky1.goto(0,165)  # Position for the first wheel
sky1.pendown()
sky1.shape("square")
sky1.color("blue")
sky1.shapesize(stretch_wid=20, stretch_len=50)  # Make it smaller

# Create the cannon with black color
cannon = turtle.Turtle()
cannon.speed(0)
cannon.penup()
cannon.goto(CANNON_X, CANNON_Y)
cannon.pendown()
cannon.setheading(45)  # Rotate the cannon shape to look like 45 degrees
cannon.shape("square")
cannon.color("brown")
cannon.shapesize(stretch_wid=1, stretch_len=3)

time.sleep(2)

# Add black wheels to the cannon
wheel1 = turtle.Turtle()
wheel1.speed(0)
wheel1.penup()
wheel1.goto(CANNON_X + 5, CANNON_Y - 20)  # Position for the first wheel
wheel1.pendown()
wheel1.shape("circle")
wheel1.color("black")
wheel1.shapesize(stretch_wid=0.5, stretch_len=1)  # Make it smaller

wheel2 = turtle.Turtle()
wheel2.speed(0)
wheel2.penup()
wheel2.goto(CANNON_X + 5, CANNON_Y - 20)  # Position for the second wheel
wheel2.pendown()
wheel2.shape("circle")
wheel2.color("black")
wheel2.shapesize(stretch_wid=0.5, stretch_len=1)  # Make it smaller

# Calculate initial velocity components
initial_velocity = SHOT_SPEED
angle_radians = math.radians(ANGLE_DEGREES)
initial_x_velocity = initial_velocity * math.cos(angle_radians)
initial_y_velocity = initial_velocity * math.sin(angle_radians)

# Calculate the position of the goal before the gunshot
GOAL_X = CANNON_X + 500  # Adjust the position of the goal
GOAL_Y = CANNON_Y

# Create the goal before the gunshot
goal = turtle.Turtle()
goal.speed(0)
goal.penup()
goal.goto(GOAL_X, GOAL_Y-17)
goal.pendown()
goal.shape("square")
goal.color("lime")
goal.shapesize(stretch_wid=1, stretch_len=1)

# Create the gunshot with a smaller circle
gunshot = turtle.Turtle()
gunshot.speed(0)
gunshot.penup()
gunshot.goto(CANNON_X, CANNON_Y)
gunshot.pendown()
gunshot.shape("circle")
gunshot.color("cyan")
gunshot.shapesize(stretch_wid=0.5, stretch_len=0.5)  # Make it smaller

# Main loop
gravity = 0.1  # Add gravity to the simulation
while True:
    x, y = gunshot.position()
    x += initial_x_velocity
    y += initial_y_velocity - gravity  # Subtract gravity each iteration
    initial_y_velocity -= gravity  # Update y-velocity

    gunshot.goto(x, y)

    # Check if the gunshot touches the goal
    if GOAL_X - 5 <= x <= GOAL_X + 5 and GOAL_Y - 25 <= y <= GOAL_Y + 25:
        print("Прилет")
        boom1 = turtle.Turtle()
        boom1.speed(0)
        boom1.penup()
        boom1.goto(GOAL_X + 1, GOAL_Y + 4)  # Position for the second wheel
        boom1.pendown()
        boom1.shape("circle")
        boom1.color("yellow")
        boom1.shapesize(stretch_wid=4, stretch_len=3)  # Make it smaller

        boom2 = turtle.Turtle()
        boom2.speed(0)
        boom2.penup()
        boom2.goto(GOAL_X + 1, GOAL_Y)  # Position for the second wheel
        boom2.pendown()
        boom2.shape("circle")
        boom2.color("orange")
        boom2.shapesize(stretch_wid=3, stretch_len=2)  # Make it smaller

        boom3 = turtle.Turtle()
        boom3.speed(0)
        boom3.penup()
        boom3.goto(GOAL_X + 1, GOAL_Y + 40)  # Position for the second wheel
        boom3.pendown()
        boom3.shape("circle")
        boom3.color("orange")
        boom3.shapesize(stretch_wid=1, stretch_len=4)  # Make it smaller
        break

    # Check if the gunshot goes off the screen
    if y < CANNON_Y-20:
        print("НЕ попал")
        break

# Close the window on click
screen.exitonclick()
