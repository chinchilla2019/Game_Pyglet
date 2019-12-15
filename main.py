import pyglet
from pyglet import gl
from pyglet.window import key
from pyglet.gl import *
import math

W, H = 780, 630
BG_COLOR = (0.75, 0.75, 0.75, 1.0)

RADIUS = 30
x = W // 2
y = H // 2

window = pyglet.window.Window(width=W, height=H, caption='GAME')
window.set_location(5, 30)
window.set_mouse_visible(visible=False)
counter = pyglet.window.FPSDisplay(window=window)


def update(dt):
    pass


@window.event
def on_draw():
    window.clear()
    glLoadIdentity()
    glColor4f(1., 0., 0., 0.75)
    glBegin(GL_TRIANGLE_FAN)
    for angle in range(0, 360, 10):
        rads = math.radians(angle)
        s = RADIUS * math.sin(rads)
        c = RADIUS * math.cos(rads)
        glVertex3f(x + c, y + s, 0 )
    glEnd()
    counter.draw()



gl.glClearColor(*BG_COLOR)
gl.glEnable(gl.GL_BLEND)
gl.glBlendFunc(pyglet.gl.GL_SRC_ALPHA, pyglet.gl.GL_ONE_MINUS_SRC_ALPHA)
pyglet.clock.schedule_interval(update, 1 / 60.0)
pyglet.app.run()