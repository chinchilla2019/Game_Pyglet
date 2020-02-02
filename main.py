import pyglet
from pyglet import gl
import math
from pyglet.window import key

level = [
    '--------------------------',
    '-                        -',
    '-                        -',
    '-                        -',
    '-                        -',
    '-                        -',
    '-                        -',
    '-                        -',
    '-                        -',
    '-                        -',
    '-                        -',
    '-                        -',
    '-                        -',
    '-                        -',
    '-                        -',
    '-                        -',
    '-                        -',
    '-                        -',
    '-                        -',
    '-                        -',
    '--------------------------'
]

level.reverse()

W, H = 780, 630
BG_COLOR = (0.75, 0.75, 0.75, 1.0)

SPEED_CIRCLE = 3
RADIUS = 20
RADIUS2 = RADIUS // 4
RADIUS3 = RADIUS2 // 2
RADIUS4 = RADIUS // 2
SIZE = 30
COLOR = (0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0)
COLOR_2 = (1, 0, 0)
x = W // 2
y = H // 2

window = pyglet.window.Window(width=W, height=H, caption='GAME')
window.set_location(5, 30)
window.set_mouse_visible(visible=False)
counter = pyglet.window.FPSDisplay(window=window)

batch = pyglet.graphics.Batch()
background = pyglet.graphics.OrderedGroup(0)
foreground = pyglet.graphics.OrderedGroup(1)

keys = key.KeyStateHandler()
window.push_handlers(keys)

# start QUARD
polygon_list = []
x = y = 0
for raw in level:
    for col in raw:
        if col == '-':
            polygon = batch.add(
                4, pyglet.gl.GL_QUADS, background,
                ('v2f', [x, y, x, y + SIZE, x + SIZE, y + SIZE, x + SIZE, y]),
                ('c3f', COLOR)
            )
            polygon_list.append(polygon)
        x += SIZE
    y += SIZE
    x = 0
# stop QUARD

# start smile
x1, y1 = W // 2, H // 2
point_list = []


def smile(a, b, c, d, e, f):
    for angle in range(a, b, c):
        rads = math.radians(angle)
        s = d * math.sin(rads)
        c = d * math.cos(rads)
        point_list.append(e + c)
        point_list.append(f + s)
    NP = len(point_list) // 2
    circle_list = batch.add(
        NP, pyglet.gl.GL_POINTS, foreground,
        ('v2f', point_list),
        ('c4f', [0, 1, 0, .5] * NP),
    )

    face_list.append(circle_list)
    return circle_list

# stop smile


def update(dt):
    if keys[key.LEFT]:
        for ver in face_list:
            ver.vertices = [element - SPEED_CIRCLE * dtif index % 2 == 0 else element for index, element in enumerate(ver.vertices)]
    if keys[key.RIGHT]:
        for ver in face_list:
            ver.vertices = [element + SPEED_CIRCLE * dt if index % 2 == 0 else element for index, element in enumerate(ver.vertices)]
    if keys[key.UP]:
        for ver in face_list:
            ver.vertices = [element + SPEED_CIRCLE * dt if index % 2 != 0 else element for index, element in enumerate(ver.vertices)]
    if keys[key.DOWN]:
        for ver in face_list:
            ver.vertices = [element - SPEED_CIRCLE * dt if index % 2 != 0 else element for index, element in enumerate(ver.vertices)]

    # Collision
    if circle_list.vertices[0] < W - RADIUS * 2:
        for ver in polygon_list:
            nx = max()


@window.event
def on_draw():
    window.clear()
    batch.draw()
    counter.draw()


gl.glPointSize(3)
gl.glEnable(gl.GL_POINT_SMOOTH)
gl.glClearColor(*BG_COLOR)
gl.glEnable(gl.GL_BLEND)
gl.glBlendFunc(pyglet.gl.GL_SRC_ALPHA, pyglet.gl.GL_ONE_MINUS_SRC_ALPHA)

face_list = []
circle_list = smile(0, 360, 6, RADIUS, x1, y1)
smile(0, 360, 37, RADIUS3, x1 + RADIUS2, y1 + RADIUS2)
smile(0, 360, 37, RADIUS3, x1 - RADIUS2, y1 + RADIUS2)
smile(210, 340, 10, RADIUS2, x1, y1 - RADIUS // 4)

pyglet.clock.schedule_interval(update, 1 / 60.0)
pyglet.app.run()

'''
glLoadIdentity()
glColor4f(1., 0., 0., 0.75)
glBegin(GL_TRIANGLE_FAN)
for angle in range(0, 360, 10):
    rads = math.radians(angle)
    s = RADIUS * math.sin(rads)
    c = RADIUS * math.cos(rads)
    glVertex3f(x + c, y + s, 0)
glEnd()
'''
