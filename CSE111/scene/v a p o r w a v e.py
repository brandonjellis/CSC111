import tkinter as tk
from random import randint


def main():
    # The width and height of the scene window.
    width = 800
    height = 500

    # Create the Tk root object.
    root = tk.Tk()
    root.geometry(f"{width}x{height}")

    # Create a Frame object.
    frame = tk.Frame(root)
    frame.master.title("Scene")
    frame.pack(fill=tk.BOTH, expand=1)

    # Create a canvas object that will draw into the frame.
    canvas = tk.Canvas(frame)
    canvas.pack(fill=tk.BOTH, expand=1)

    # Call the draw_scene function.
    draw_scene(canvas, 0, 0, width-1, height-1)

    root.mainloop()


def draw_scene(canvas, scene_left, scene_top, scene_right, scene_bottom):
    """Draw a scene in the canvas. scene_left, scene_top,
    scene_right, and scene_bottom contain the extent in
    pixels of the region where the scene should be drawn.
    Parameters
        scene_left: left side of the region; less than scene_right
        scene_top: top of the region; less than scene_bottom
        scene_right: right side of the region
        scene_bottom: bottom of the region
    Return: nothing

    If needed, the width and height of the
    region can be calculated like this:
    scene_width = scene_right - scene_left + 1
    scene_height = scene_bottom - scene_top + 1
    """
    # Call your functions here, such as draw_sky, draw_ground,
    # draw_snowman, draw_tree, draw_shrub, etc.
    
    draw_ground(canvas, scene_left, scene_right, scene_bottom)

    draw_sun(canvas,scene_left,scene_right,scene_top,scene_bottom,flip=True)
    draw_planet(canvas,150,350,50,"#f753b4")

    draw_grid(canvas,scene_left,scene_right,scene_top,scene_bottom)

    draw_sky(canvas, scene_left, scene_top, scene_right, scene_bottom)

    draw_sun(canvas,scene_left,scene_right,scene_top,scene_bottom)

    
    starcount = 25
    for _ in range(starcount+1):
        star_x = randint(scene_left,scene_right)
        star_y = randint(scene_top,int(scene_bottom*3/5))
        star_scale = randint(50,130)/100
        draw_star(canvas, star_x, star_y, scale=star_scale)

    draw_planet(canvas,150,75,50,"#fd33aa")


# Define more functions here, like draw_sky, draw_ground,
# draw_cloud, draw_tree, draw_kite, draw_snowflake, etc.

def draw_sky(canvas, left, top, right, bottom):
    sky_bottom = bottom * 3/5
    canvas.create_rectangle(left, top, right, sky_bottom, width=0, fill="#025370")

def draw_ground(canvas, left, right, bottom):
    ground_thickness = bottom * 2/5
    ground_top = bottom - ground_thickness
    canvas.create_rectangle(left, ground_top, right, bottom, width=0, fill="#69008c")

def draw_grid(canvas, left, right, top, bottom):
    focusx = right/2
    focusy = top+250
    spacing = 50
    width = 2
    color = "#ff00d0"

    for i in range(0,bottom,int(spacing/2)):
        canvas.create_line(focusx,focusy,left,i,fill=color,width=width)
        canvas.create_line(focusx,focusy,right,i,fill=color,width=width)
        canvas.create_line(left,i,right,i,fill=color,width=width)
    for i in range(0,right+10,spacing):
        canvas.create_line(focusx,focusy,i,bottom,fill=color,width=width)

def draw_star(canvas, x, y, scale=1):
    inner_offset = 2 * scale
    short_offset = 10 * scale
    long_offset = 20 * scale

    x_left = x-short_offset
    x_Ileft = x-inner_offset
    x_Iright = x+inner_offset
    x_right = x+short_offset
    y_top = y-long_offset
    y_Itop = y-inner_offset
    y_Ibottom = y+inner_offset
    y_bottom = y+long_offset

    canvas.create_polygon(x_left,y,x_Ileft,y_Itop,x,y_top,x_Iright,y_Itop,x_right,y,x_Iright,y_Ibottom,x,y_bottom,x_Ileft,y_Ibottom,fill="#ffffff")

def draw_sun(canvas, left, right, top, bottom,flip=False):
    
    radius = 125
    center = right/2
    horizon = bottom * (3/5)
    x1 = center-radius
    y1 = horizon-radius
    x2 = center+radius
    y2 = horizon+radius
    arc_start = 0
    color = "#fdd20a"
    if flip == True:
        arc_start = 180
        color = "#fda05b"
    canvas.create_arc(x1,y1,x2,y2,start=arc_start,extent=180,fill=color,outline="")

def draw_planet(canvas, x, y, r, color):
    x1 = x
    x2 = x + 2*r
    y1 = y
    y2 = y + 2*r
    canvas.create_oval(x1,y1,x2,y2,width=0,fill=color)

#def draw_palm():



# Call the main function so that
# this program will start executing.
main()