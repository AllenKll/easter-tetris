import pyglet

class GameTick(object):
    def __init__(self, tickOnFirstCall = False):
        self.tick = tickOnFirstCall
        self.started = tickOnFirstCall

    def isTick(self, nextTickTime):
        def setTick(dt):
            self.tick = True

        if not self.started:
            self.started = True
            pyglet.clock.schedule_once(setTick, nextTickTime)
            return False
        elif self.tick:
            self.tick = False
            pyglet.clock.schedule_once(setTick, nextTickTime)
            return True
        else:
            return False
