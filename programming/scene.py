# Example 1

# Import the functions from the Draw 2-D library
# so that they can be used in this program.
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing

def main():
    scene_width = 800
    scene_height = 500

    # Call the start_drawing function in the draw2d.py
    # library which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)

    # Call the draw_sky and draw_ground functions in this file.
    draw_sky(canvas, scene_width, scene_height)
    draw_ground(canvas, scene_width, scene_height)
    #draw_grid(canvas, scene_width, scene_height, 50)

    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)


def draw_sky(canvas, scene_width, scene_height):
    """Draw the sky and all the objects in the sky."""
    draw_rectangle(canvas, 0, scene_height / 3,
        scene_width, scene_height, width=0, fill="skyBlue2")
    draw_cloud(canvas)


def draw_ground(canvas, scene_width, scene_height):
    """Draw the ground and all the objects on the ground."""
    draw_rectangle(canvas, 0, 0,
        scene_width, scene_height / 1.4, width=0, fill="skyBlue4")
    
    draw_rectangle(canvas, 0, 0, scene_width, scene_height / 2, width=1, outline="darkGreen", fill="darkGreen")
    
    draw_rectangle(canvas, 0, 0,
        scene_width, scene_height / 2.5, width=0, fill="burlyWood3")
    
    draw_rectangle(canvas, 0, 0,
        scene_width, scene_height / 5, width=0, fill="springGreen3")
    draw_rectangle(canvas, 0, 0,
        scene_width, scene_height / 8, width=0, fill="springGreen2")
    
    # Draw
    draw_mountain(canvas)
    draw_buildings(canvas)
    draw_grass(canvas)
    draw_stairs(canvas)


def draw_cloud(canvas):
    draw_oval(canvas, 750, 450, 500, 350, width=0, fill="snow1")
    draw_oval(canvas, x0 = 400, y0 = 480, x1 = 100, y1 = 400,  width=0, fill="snow1")
    draw_rectangle(canvas, 600, 450, 0, 380, width=0, fill="snow1")
    draw_rectangle(canvas, 300, 400, 150, 350, width=0, fill="snow1")
    draw_rectangle(canvas, 800, 460, 600, 400, width=0, fill="snow1")
    draw_rectangle(canvas, 250, 480, 30, 460, width=0, fill="snow1")
    draw_rectangle(canvas, 650, 360, 400, 350, width=0, fill="snow1")


def draw_mountain(canvas):
    #mountains background
    draw_polygon(canvas, x0 = 150, y0 = 250, x1 = 350, y1 = 250, x2 = 250, y2 = 300, width=0, fill="skyBlue4")
    draw_oval(canvas, 100, 480, -400, 200, width=0, fill="skyBlue4")
    draw_oval(canvas, 900, 400, 750, 300, width=0, fill="skyBlue4")
    draw_oval(canvas, 450, 380, 315, 300, width=0, fill="skyBlue4")

    #big mountains
    draw_polygon(canvas, x0 = 250, y0 = 250, x1 = 650, y1 = 250, x2 = 450, y2 = 480, width=0, outline="dark green", fill="dark green")
    draw_polygon(canvas, x0 = 150, y0 = 250, x1 = 350, y1 = 250, x2 = 250, y2 = 300, width=0, outline="dark green", fill="dark green")
    draw_rectangle(canvas, x0 = 700, y0 = 320, x1 = 550, y1 = 250, width=0, outline="dark green", fill="darkGreen")
    draw_polygon(canvas, x0 = 700, y0 = 250, x1 = 800, y1 = 250, x2 = 700, y2 = 320, width=0, outline="dark green", fill="dark green")
    draw_rectangle(canvas, x0 = 800, y0 = 270, x1 = 550, y1 = 250, width=0, outline="dark green", fill="darkGreen")

    #cloud
    draw_rectangle(canvas, 440, 450, 0, 380, width=0, fill="snow1")
    
    #shades of mountains
    draw_polygon(canvas, 150, 250, 220, 250, 250, 300, width=0, outline="darkSlateGray", fill="darkSlateGray")
    draw_polygon(canvas, 270, 290, 420, 200, 450, 480, width=0, outline="darkSlateGray", fill="darkSlateGray")
    draw_polygon(canvas, 700, 230, 800, 230, 700, 300, width=0, outline="darkSlateGray", fill="darkSlateGray")
    draw_rectangle(canvas, 700, 320, 600, 200, width=0, outline="darkSlateGray", fill="darkSlateGray")


def draw_buildings(canvas):
    draw_rectangle(canvas, 400, 220, 0, 200, fill="burlyWood3")
    draw_rectangle(canvas, 800, 230, 550, 200, fill="burlyWood3")
    draw_rectangle(canvas, 150, 290, 0, 200, fill="burlyWood3")
    draw_rectangle(canvas, 100, 325, 0, 200, outline='burlyWood3', fill="burlyWood3")
    draw_rectangle(canvas, 500, 280, 400, 200, outline='burlyWood3', fill="burlyWood3")
    draw_rectangle(canvas, 750, 260, 650, 200, outline='burlyWood3', fill="burlyWood3")
    draw_rectangle(canvas, 750, 270, 700, 200, outline='burlyWood3', fill="burlyWood3")
    draw_polygon(canvas, 0, 300, 100, 300, 0, 350, width=0, outline='burlyWood3', fill="burlyWood3")
    draw_rectangle(canvas, 320, 240, 0, 200, outline='burlyWood3', fill="burlyWood3")
    draw_rectangle(canvas, 500, 290, 490, 280, outline='burlyWood3', fill="burlyWood3")
    draw_rectangle(canvas, 560, 240, 550, 230, outline='burlyWood3', fill="burlyWood3")

    #shadow
    draw_rectangle(canvas, 100, 190, 50, 100, outline="saddleBrown", fill="saddleBrown")
    draw_rectangle(canvas, 50, 240, 0, 100, outline="saddleBrown", fill="saddleBrown")
    draw_rectangle(canvas, 610, 210, 580, 90, outline="saddleBrown", fill="saddleBrown")

    #windows
    draw_rectangle(canvas, 480, 250, 470, 220, outline="burlyWood1", fill="orange3")
    draw_rectangle(canvas, 430, 250, 420, 220, outline="burlyWood1", fill="orange3")

    draw_rectangle(canvas, 200, 220, 180, 200, outline="burlyWood1", fill="orange3")
    draw_rectangle(canvas, 260, 220, 240, 200, outline="burlyWood1", fill="orange3")

    draw_rectangle(canvas, 740, 240, 730, 200, outline="orange3", fill="burlyWood1")
    draw_rectangle(canvas, 700, 240, 690, 200, outline="orange3", fill="burlyWood1")


def draw_grass(canvas):
    draw_polygon(canvas, 0, 100, 150, 100, 0, 200, outline='springGreen3', fill='springGreen3')
    draw_polygon(canvas, 0, 250, 50, 250, 100, 290, outline='springGreen3', fill='springGreen3')
    draw_polygon(canvas, 50, 200, 100, 200, 150, 290, outline='springGreen3', fill='springGreen3')
    draw_rectangle(canvas, 350, 110, 250, 100, outline='springGreen3', fill='springGreen3')
    draw_rectangle(canvas, 400, 60, 390, 50, outline='springGreen3', fill="burlyWood3")
    draw_polygon(canvas, 0, 50, 150, 50, 0, 150, outline='springGreen2', fill="springGreen2")


def draw_stairs(canvas):
    draw_rectangle(canvas, 550, 200, 500, 75, outline="burlyWood", fill="burlyWood")
    draw_rectangle(canvas, 550, 170, 500, 155, outline='burlyWood', fill="burlyWood3")
    draw_rectangle(canvas, 550, 120, 500, 105, outline='burlyWood', fill="burlyWood3")



def draw_grid(canvas, width, height, interval, color="blue"):
    # Draw a vertical line at every x interval.
    label_y = 15
    for x in range(interval, width, interval):
        draw_line(canvas, x, 0, x, height, fill=color)
        draw_text(canvas, x, label_y, f"{x}", fill=color)

    # Draw a horizontal line at every y interval.
    label_x = 15
    for y in range(interval, height, interval):
        draw_line(canvas, 0, y, width, y, fill=color)
        draw_text(canvas, label_x, y, f"{y}", fill=color)

# Call the main function so that
# this program will start executing.
main()