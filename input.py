import pyglet

class Input(object):
    TOGGLE_PAUSE, MOVE_DOWN, MOVE_RIGHT, MOVE_LEFT, ROTATE_CLOCKWISE = range(5)

    def __init__(this):
        this.action = None

    def doKeypress(this, symbol, modifiers):
        if ( symbol == pyglet.window.key.SPACE ):
            this.action = Input.TOGGLE_PAUSE

    def doTextMotion(this, motion):
        if motion == pyglet.window.key.MOTION_UP:
            this.action = Input.ROTATE_CLOCKWISE
        elif motion == pyglet.window.key.MOTION_LEFT:
            this.action = Input.MOVE_LEFT
        elif motion == pyglet.window.key.MOTION_RIGHT:
            this.action = Input.MOVE_RIGHT
        elif motion == pyglet.window.key.MOTION_DOWN:
            this.action = Input.MOVE_DOWN

    def consume(this):
        action = this.action
        this.action = None
        return action
