# draw polygon and split line using randomly generated, counterclockwise (or not) vertices
import json
import pyglet
from poly_rand_points import rand_list
from pyglet.gl import *
from poly_a import split_polygon
#from poly_b import split_polygon, sortList
 

data =  rand_list(5)
size = len(data)
x,y  = split_polygon(data)
print "x,y =",x,y

#poly_a:
vert_temp = json.dumps(data)

#poly_b:
# data_sorted = sortList(data)
# vert_temp = json.dumps(data_sorted)

vertices = json.loads(vert_temp) 

W = 200
H = 200
scale1 = 4
scale = 4
win = pyglet.window.Window(scale1*W,scale1*H)

@win.event
def on_draw():
 
        # Clear buffers
        glClear(GL_COLOR_BUFFER_BIT)
        # Draw some stuff
        glBegin(GL_LINE_STRIP)
        for i in range(0,size):
        	glVertex2f(scale1*W/2 + scale*vertices[i][0], scale1*H/2 + scale*vertices[i][1])
        glVertex2f(scale1*W/2 + scale*vertices[0][0], scale1*H/2 + scale*vertices[0][1])
        glVertex2f(scale1*W/2.0 + scale*x, scale1*H/2 + scale*y)

        glEnd()
 
pyglet.app.run()

