def beer(n):
    
    beer_left = n
    for i in range(n, 0 , -1):
        beer_left = beer_left -1
        print(i, "Bottles of beer on the wall,",i ,"bottles of beer, Take one down, pass it around,", beer_left,"bottles of beer on the wall\n")
#multiplication table

def table(n):
    for row in range(1,n+1):
        for colum in range(1,n+1):
            tab=(colum*row)
            print(tab, end ='\t')
        print()
            
#Summation of squares
def Summation(n):
    total = 0
    for i in range(1 , n+1):
        s = i ** 2
        total = total + s
        print(i, ' + ', sep='^2', end='')
    print('=',total)
        


#n = int(input("how much beer?:" ))
#beer(n)
#n = int(input("what number do you want to mulitply: "))
#table(n)
#n = int(input("what number up to do you want to square to add: "))
#Summation(n)

#DrawSquare

import turtle
ja = turtle.Turtle()
ja.speed('fast')


def drawSquare(ja, squareSize):
    for i in range(squareSize):
        ja.fd(20)
        ja.right(360/squareSize)
        
#drawSquare(ja,4)

#Drawing a Row of Squares

def drawRow(alice, length, squareSize):
    for i in range(length):
        drawSquare(alice,4)
        alice.fd(20)

        
#drawRow(ja,5,4)

#Drawing a Grid
def drawGrid(alice, size, squareSize):
    for i in range(size):
        drawRow(alice,5,4)
        alice.right(90)
        alice.fd(20)
        alice.left(90)
        alice.backward(100)
#drawGrid(ja,5,4)

#Drawing a Stair of Squares

def drawSquareStairs(alice, height, squareSize):
    n=1
    bc=0
    for i in range(height):
        drawRow(alice,n,4)
        n=n+1
        bc=bc+20
        alice.backward(bc)
        alice.right(90)
        alice.fd(20)
        alice.left(90)        
#drawSquareStairs(ja,5,4)

#Spirals
def drawNgon(alice, numSides, sideLength):
    for i in range(numSides):
        alice.fd(100)
        alice.right(360/numSides)

#drawNgon(ja,6,50)

#Super Spiral
def drawNgonSpiral(alice, numSides, sideLength, numShapes):
    
    for i in range(numShapes):
        drawNgon(ja,6,50)
        alice.right(720/35)
        alice.fd(100)
    alice.right(90)
    alice.up()
    alice.fd(280)
    alice.down()
    for i in range(numShapes):
        drawNgon(ja,6,50)
        alice.right(720/35)
        alice.fd(20)
#drawNgonSpiral(ja,6,100,35)


#Hourglass
def hourglass(n):
    lst = ('\::::::::/')
    print(" |````````|")
    r = 0
    q = 0
    t = lst[0]
    m = lst[0]
    v = lst[-1]
    b = lst[-1]
    for i in range (n):
        t =  " " + t
        r = r + 1
        q = q - 1
        print(t + lst[r:q] + v)
    print("     ||")
    g = 5
    h = -5
    for s in range(n):
        b =  " " * (n-s) + lst[-1]
        g = g - 1
        h = h + 1
        print(b + lst[g:h]+ m)
    print(" |````````|")
   
hourglass(4)
