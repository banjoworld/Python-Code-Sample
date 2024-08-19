# Alex Hurtado
# Date: 2024-08-11



import turtle

def drawSquare(t, sz):
    """Get turtle t to draw a square with side length sz."""
    for i in range(4):
        t.forward(sz)  # Move the turtle forward by sz units
        t.left(90)     # Turn the turtle 90 degrees to the left

# Set up the window and background
wn = turtle.Screen()
wn.bgcolor("white")  # Set the background color

# Create a turtle named alex
alex = turtle.Turtle()
alex.color("blue")   # Set the turtle color to blue

# Call the drawSquare function to draw a square with side length 100
drawSquare(alex, 100)

# Close the window when clicked
wn.exitonclick()