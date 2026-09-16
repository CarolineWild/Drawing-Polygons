from p5 import *
from coordsys import *
import random

#CONSTANTS
WINDOW_WIDTH  = 1000        #define sized of drawing window
WINDOW_HEIGHT = 1000

COORD_FRAME__MAX_X = 1      #define coordinate system
COORD_FRAME__MIN_X = -1     #center is (0,0)
COORD_FRAME__MAX_Y = 1
COORD_FRAME__MIN_Y = -1

                            #class is blueprint for creating polygons
class Polygon:             
    def __init__(self,sides,x,y,size, chosen_orientation):
        self.sides = sides      #self.sides - self refers to the specific polygon object created
        self.x = x #0
        self.y = y  #0
        self.size = size #.09 radius
        self.chosen_orientation = chosen_orientation

        #color
        self.r = random.randint(0, 255)
        self.g = random.randint(0, 255)
        self.b = random.randint(0, 255)


    def draw(self):
        stroke_weight(5)
        stroke(self.r, self.g, self.b)
        noFill()

        begin_shape()
                                        #repeat once for every vertex of polygon
        for i in range(self.sides):     #calculates verticies in polygon object
            if self.chosen_orientation == 1:
                angle = -PI / 2 + TWO_PI * i / self.sides
                                                        #TWO PI is 6.28 radians, 360 degrees
                                                        #i/sides i is each vertex divided by the num of sides-
                                                        #-which evenly spaces each point around the circle in degrees
                                                        #for each vertex PI/2 is where to start rotation, TWO_PI +I/sides is how far to move around circle
            elif self.chosen_orientation == 2:
                angle = -PI / 2 + PI / self.sides + TWO_PI * i / self.sides

            x = self.x + self.size * cos(angle)  #turn back to cartesian value
            y = self.y + self.size * sin(angle) #y = 0(center) + 0.9(radius) *

            vertex(x, y)            

        end_shape(CLOSE)

def get_input_orientation():
    while True:
        user_input_2 = input(
            "Please enter '1', or '2' \n"
            "Option 1: Draw polygons with the first vertex centered at the bottom of the window \n"
            "Option 2: Draw polygons with the bottom side parallel to the bottom edge of the window\n"
            ).strip()   #removes blank spaces before and after
            
        if user_input_2 == "1":
            return 1
        
        elif user_input_2 == "2":
            return 2
        
        else:
            print("Please enter 1 or 2.")
    

def get_input_sides(chosen_orientation):

    polygons = []

    while True:
        try:
            user_input = input("\nPlease enter a number of sides: ").strip()

            if " " in user_input:                   #Dont allow multiple sizes
                print("Enter one size at a time.")
                continue

            num_of_sides = int(user_input)      

            if num_of_sides < 0:
                break
                            #creating an instance of an object, creates new polygon object
            polygons.append(Polygon(num_of_sides, 0, 0, 0.9, chosen_orientation))
    
        except ValueError:
            print("Enter a number.")
            continue

    return polygons     #sends list out of the function

        
chosen_orientation = get_input_orientation()    #get the user's drawing preference FIRST
polygons = get_input_sides(chosen_orientation)      #executes get_input function
                        #return polygons sends list back to whatever called get_input function which is here 

#PROCESSING          
def setup():
    size(WINDOW_WIDTH,WINDOW_HEIGHT)

def draw():
    background(255)
    coordinate_frame(COORD_FRAME__MIN_X, COORD_FRAME__MIN_Y, COORD_FRAME__MAX_X, COORD_FRAME__MAX_Y)

    for polygon in polygons:
        polygon.draw()

run()
