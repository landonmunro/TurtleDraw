# Landon Munro
# Turtle Draw

turtleFile = open("turtle-draw.txt", "r")
turtleTextLine = turtleFile.readline()

while turtleTextLine:
    print(turtleTextLine, end="")
    turtleTextLine = turtleFile.readline()


