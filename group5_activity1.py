import turtle
'''Created variables for each shape and set a degree to it '''
HEX_SIDE = 50 # 50 is the degree for the hexagon side
SQUARE_SIDE = 90 # 90 is the degree for the square side
CIRCLE_RADIUS = 45 # 45 is the degree for the circle radius
'''Created a function named setPos and added "turta" "x" "y" as parameters'''
def setPos(turta, x, y):
    turta.penup()
    turta.goto(x, y)
    turta.pendown()
'''Created a function named hexagon and added "turta" "hexa_color" "border_color" '''
def hexagon(turta, hexa_color, border_color):   
    turta.fillcolor(hexa_color)
    turta.pencolor(border_color)
    turta.begin_fill()

    turta.forward(HEX_SIDE)
    turta.right(60)
    turta.forward(HEX_SIDE)
    turta.right(60)
    turta.forward(HEX_SIDE)
    turta.right(60)
    turta.forward(HEX_SIDE)
    turta.right(60)
    turta.forward(HEX_SIDE)
    turta.right(60)
    turta.forward(HEX_SIDE)

    turta.end_fill()
'''Created a function named square and added "turta" "square_color" "border_color" '''
def square(turta, square_color, border_color):
    turta.fillcolor(square_color)
    turta.pencolor(border_color)
    turta.begin_fill()

    turta.forward(SQUARE_SIDE)
    turta.right(90)
    turta.forward(SQUARE_SIDE)
    turta.right(90)
    turta.forward(SQUARE_SIDE)
    turta.right(90)
    turta.forward(SQUARE_SIDE)

    turta.end_fill()
'''Created a function named circle and added "turta" "circle_color" "border_color" '''
def circle(turta, circle_color, border_color):
    turta.fillcolor(circle_color)
    turta.pencolor(border_color)
    turta.begin_fill()

    turta.circle(CIRCLE_RADIUS)

    turta.end_fill()
'''Created a function named pattern and inside the function we added multiple variables with using input so the user can enter the color they want'''
def pattern():
    hexagon_color = input("Enter the color of hexagon: ")
    circle_color = input("Enter the color of circle: ")
    square_color = input("Enter the color of square: ")
    border_color = input("Enter the color of shape borders: ")
    # First column for hexagon
    turta1 = turtle.Turtle()
    turta1.speed(5)
    setPos(turta1, -150, 100) # As you can see here we set the coordinates for the first hexagon
    hexagon(turta1, hexagon_color, border_color)

    turta2 = turtle.Turtle()
    turta2.speed(5)
    setPos(turta2, -100, 0) # As you can see here we set the coordinates for the second hexagon
    hexagon(turta2, hexagon_color, border_color)

    turta3 = turtle.Turtle()
    turta3.speed(5)
    setPos(turta3, -50, -100) # As you can see here we set the coordinates for the third hexagon
    hexagon(turta3, hexagon_color, border_color)
    # Second column for circle
    turta4 = turtle.Turtle()
    turta4.speed(5)
    setPos(turta4, 0, 0) # As you can see here we set the coordinates for the first circle
    circle(turta4, circle_color, border_color)

    turta5 = turtle.Turtle()
    turta5.speed(5)
    setPos(turta5, 50, -100) # As you can see here we set the coordinates for the second circle
    circle(turta5, circle_color, border_color)

    turta6 = turtle.Turtle()
    turta6.speed(5)
    setPos(turta6, 100, -200) # As you can see here we set the coordinates for the third circle
    circle(turta6, circle_color, border_color)
    # Third column for square
    turta7 = turtle.Turtle()
    turta7.speed(5)
    setPos(turta7, 100, 100) # As you can see here we set the coordinates for the first square
    square(turta7, square_color, border_color)

    turta8 = turtle.Turtle()
    turta8.speed(5)
    setPos(turta8, 150, 0) # As you can see here we set the coordinates for the second square
    square(turta8, square_color, border_color)

    turta9 = turtle.Turtle()
    turta9.speed(5)
    setPos(turta9, 200, -100) # As you can see here we set the coordinates for the third square
    square(turta9, square_color, border_color)

    turtle.done()

'''Created a main function and called pattern in it as well as set the background color for the screen'''
def main():
    screen = turtle.Screen()
    screen.bgcolor("sky blue")
    pattern()

main()
