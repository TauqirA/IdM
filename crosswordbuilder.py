from graphics import *

def main():
    size = 6
    BOX = 600
    
    win = GraphWin("CrossWord Puzzle", BOX, BOX)
    string = "- - -   - -\n- 11 - - - -"
    string = string.replace("   ", " * ")
    string = string.replace("\n", " \n ")
    chars = string.split(" ")
    print(len(chars))
    x1 = 0
    y1 = 0
    inc = BOX/size
    count = 1
    for c in chars:
        r = Rectangle(Point(x1,y1), Point(x1+inc,y1+inc))
        r.setOutline("white")
        if c == "-":
            r.setFill("black")
            x1 = x1 + inc
            r.draw(win)

        elif c == "*":
            r.setFill("white")
            x1 = x1 + inc
            r.draw(win)
            
        elif c == "\n":
            x1 = 0
            y1 = count*inc
            count = count + 1
        else:
            t = Text(r.getCenter(), c)
            t.setTextColor("red")
            r.setFill("white")
            #t.draw(r)
            r.draw(win)
            t.draw(win)
            x1 = x1 + inc


    win.getMouse()
    win.close()
        
main()
