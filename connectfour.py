#Cody Circle
#12/22/2015
#foursquare.py
#----------------------------------------------------------------------------
from graphics import *
#----------------------------------------------------------------------------
def createCircles(win):
    #create first row of circles on the board
    x = 70
    y = 150
    check = 1
    for i in range(42):
        circle = Circle(Point(x,y), 50)
        circle.draw(win)
        circle.setFill("grey")
        x += 110
        if (check%7 == 0):
            x = 70
            y = y + 110
        check += 1
#----------------------------------------------------------------------------
def checkClick(win, userX, userY, boardState, color):
    x = 70
    y = 150
    check = 1
    
    for i in range(42):
        clickRange = ((userX - x)**2) + ((userY - y)**2)
        if clickRange < (50**2) and boardState[i] != 1:
            circle = Circle(Point(x, y), 50)
            circle.draw(win)
            circle.setFill(color)
            boardState[i] = 1
            #return False
        
        x += 110
        if (check%7 == 0):
            x = 70
            y = y + 110
        check += 1

    #return True
#----------------------------------------------------------------------------
def main():
    win = GraphWin("Connect Four", 800, 800)
    win.setBackground("black")
    mainSquare = Rectangle(Point(1, 93), Point(799, 760))
    mainSquare.draw(win)
    mainSquare.setFill("blue")

    exitSquare = Rectangle(Point(350, 20), Point(450, 50))
    exitSquare.draw(win)
    exitSquare.setFill("white")
    exitText = Text(Point(400, 35), "Quit")
    exitText.draw(win)

    createCircles(win)
    
    boardState = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

    color = "red"
    validClick = True
    
    while True:
        click = win.getMouse()
        x = click.getX()
        y = click.getY()
        

        # click quit button
        if x > 350 and x < 450 and y > 20 and y < 50:
            break

        #while validClick:
        validClick = checkClick(win, x, y, boardState, color)
        
        if color == "red":
            color = "black"
        elif color == "black":
            color = "red"

    print(boardState)   
    win.close()
        
main()

