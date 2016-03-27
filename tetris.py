import pyglet
import board
import tetrominoType
import game
import input
import infoDisplay

WIDTH = 800
HEIGHT = 600
BOARD_X = 445
BOARD_Y = 13
GRID_WIDTH = 10
GRID_HEIGHT = 20
BLOCK_SIZE = 24

window = pyglet.window.Window(WIDTH, HEIGHT)
window.set_vsync(False)

backgroundImage = pyglet.resource.image('easterback.jpg')
blocksImage = pyglet.resource.image('eggs.png')
tetrominoType.TetrominoType.classInit(blocksImage, BLOCK_SIZE)

# add open gl alpha blending so that RGBA will show as transparent
pyglet.gl.glEnable(pyglet.gl.GL_BLEND)
pyglet.gl.glBlendFunc(pyglet.gl.GL_SRC_ALPHA, pyglet.gl.GL_ONE_MINUS_SRC_ALPHA)

board = board.Board(BOARD_X, BOARD_Y, GRID_WIDTH, GRID_HEIGHT, BLOCK_SIZE)
infoDisplay = infoDisplay.InfoDisplay(window)
input = input.Input()
theGame = game.Game(board, infoDisplay, input, backgroundImage)

@window.event
def on_key_press(symbol, modifiers):
    input.doKeypress(symbol, modifiers)

@window.event
def on_text_motion(motion):
    input.doTextMotion(motion)

@window.event
def on_draw():
    theGame.draw()

def update(dt):
    theGame.update()

pyglet.clock.schedule_interval( update, 1/60.0 )

# run the game engine
pyglet.app.run()
