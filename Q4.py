# Script to find the area of a Triangle from the coordinates of 3 points provided by user

import math

X1 = int( input("Please enter coordinate x1: ") )
Y1 = int( input("Please enter coordinate y1: ") )
X2 = int( input("Please enter coordinate x2: ") )
Y2 = int( input("Please enter coordinate y2: ") )
X3 = int( input("Please enter coordinate x3: ") )
Y3 = int( input("Please enter coordinate y3: ") )

def distance(x1,y1,x2,y2):
    """Function to find length of line between two points"""
    dx = x2 - x1
    dy = y2 - y1
    d = math.sqrt(dx**2 + dy**2)
    return d

def areaTriangle(ptx1,pty1,ptx2,pty2,ptx3,pty3):
    """Function to find area of triangle defined by 3 points"""
    # This uses Heron's Formula - Google it if you want to know more
    side1 = distance(ptx1,pty1,ptx2,pty2)
    side2 = distance(ptx2,pty2,ptx3,pty3)
    side3 = distance(ptx3,pty3,ptx1,pty1)
    p = (side1 + side2 + side3)/2
    t1 = p-side1
    t2 = p-side2
    t3 = p-side2
    if t1==0 or t2==0 or t3==0:
        print("ERROR: Does not form a triangle")
        return None
    area = math.sqrt( p*(p-side1)*(p-side2)*(p-side3) )
    return(area)

A = areaTriangle(X1, Y1, X2, Y2, X3, Y3)
if A!=None:
    print("Area of your triangle is " + str(A) )
