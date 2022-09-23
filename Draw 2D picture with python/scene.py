# Import the functions from the Draw 2-D library
# so that they can be used in this program.
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing
import random

def main():
    # Width and height of the scene in pixels

    scene_width = 800 #Total width pixels in the scene
    scene_height = 500 #Total height pixels in the scene

    # Call the start_drawing function in the draw2d.py
    # library which will open a window and create a canvas.

    canvas = start_drawing("Scene", scene_width, scene_height) #Start to draw insede the scene_width and scene_height

########################################################################################################################################################################
####################################################################### PRINTS ↓ ###########################################################################
########################################################################################################################################################################


    # Call your drawing functions such
    # as draw_sky and draw_ground here.

    ####################################################################### SKY PRINT ########################################################################
   
    #Create sky
    draw_sky(canvas,800,650 )

    #Create sun
    draw_sun(canvas,300,300)

    #Create clouds
    draw_clouds(canvas,800,450,clouds=30)

########################################################################################################################################################################

########################################################################################################################################################################


    ####################################################################### GROUND PRINT ########################################################################

    #Create snow-sensation on the floor
    draw_oval(canvas,120,100,scene_height,240, fill="white", width=0)
    draw_oval(canvas,250,100,-100,225, fill="white", width=0)
    draw_oval(canvas,120,100,1200,230, fill="white", width=0)

    #Create floor
    draw_floor(canvas,800,650 )

    #Create "secuencial" pine_tress
    for x in range(100, 800, 150):
        draw_pine_tree(canvas, x, 200, 80)
        
    for x in range(110, 800, 180):
        draw_pine_tree(canvas, x, 165, 105)
    draw_pine_tree(canvas, 550, 150, 180)
    draw_pine_tree(canvas, 200, 100, 250)


    ####################################################################### GRID PRINT ########################################################################

    #Create grid (coord. points)
    draw_grid(canvas, scene_width, scene_height,50) #Each 50 pixels (interval)

    # Call the finish_drawing function
    # in the draw2d.py library.

    finish_drawing(canvas)

########################################################################################################################################################################
############################################################################# FUNCTIONS ↓ ########################################################################
########################################################################################################################################################################

# Define your functions such as
# draw_sky and draw_ground here.

############################################################################# SKY FUNCTIONS ########################################################################

def draw_sky(canvas, scene_width, scene_height):
    draw_rectangle(canvas, 0, scene_height / 3,
        scene_width, scene_height, width=0, fill="sky blue")
def draw_sun(canvas, scene_width, scene_height):
    draw_oval(canvas, 400, scene_width, scene_height, 200, fill="darkOrange",width=0)
def draw_clouds(canvas,scene_width,scene_height,clouds=25):
    min_diam = 30
    max_diam = 50
    # Draw 50 circles, each with
    # a random location and diameter.
    for i in range(clouds):
        x = random.randint(0, scene_width - max_diam)
        y = random.randint(250, scene_height)
        diameter = random.randint(min_diam, max_diam)
        draw_oval(canvas, x, y, (x + diameter*3), y + diameter,
                fill="white", width=0)

############################################################################# GROUND FUNCTIONS ######################################################################

def draw_floor(canvas, scene_width, scene_height):
    draw_rectangle(canvas, 0, 0,scene_width, scene_height / 3, width=0, fill="white")
def draw_pine_tree(canvas, center_x, bottom, height):
    
    #Draw the trunk of the tree
    trunk_width = height / 10
    trunk_height = height / 6
    left_trunk = center_x - trunk_width / 2
    bottom_trunk = bottom
    right_trunk = center_x + trunk_height / 2
    trunk_top = bottom + trunk_height
    draw_rectangle(canvas, left_trunk, bottom_trunk, right_trunk, trunk_top, fill="tan4")

    #Draw the skirt of the tree
    skirt_width = height / 2
    skirt_left = center_x - skirt_width / 2
    skirt_bottom = trunk_top
    peak_x = center_x
    peak_y = bottom + height
    skirt_right = center_x + skirt_width / 2
    draw_polygon(canvas,skirt_left, skirt_bottom, peak_x, peak_y, skirt_right, skirt_bottom,fill="darkGreen")

############################################################################# GRID FUNCTIONS #########################################################################

def draw_grid(canvas,width, height,interval):
    #draw vertical lines
    label_y = 15 #pixels for label
    for x in range(interval, width, interval):
        draw_line(canvas, x, 0, x, height)
        draw_text(canvas, x, label_y, f"{x}")
    #draw horizontal lines
    label_x = 15 #pixels for label
    for y in range(interval, height, interval):
        draw_line(canvas, 0, y, width, y)
        draw_text(canvas, label_x, y, f"{y}")


########################################################################################################################################################################
########################################################################## PROGRAM START ###############################################################################
########################################################################################################################################################################

# Call the main function so that
# this program will start executing.
main()