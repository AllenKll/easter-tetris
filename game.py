import gameTick
import input

class Game(object):

    BASE_TICK_SPEED = 0.6

    def __init__(self, board, infoDisplay, input, backgroundImage):
        self.board = board
        self.infoDisplay = infoDisplay
        self.input = input
        self.backgroundImage = backgroundImage
        self.paused = False
        self.lost = False
        self.numRowsCleared = 0
        self.tickSpeed = Game.BASE_TICK_SPEED
        self.ticker = gameTick.GameTick()

    def addRowsCleared(self, num):
        self.numRowsCleared += num
        self.tickSpeed = Game.BASE_TICK_SPEED / (((self.numRowsCleared) / 10) + 1 )
        self.infoDisplay.setRowsCleared(self.numRowsCleared)

    def togglePause(self):
        self.paused = not self.paused
        self.infoDisplay.showPausedLabel = self.paused

    def update(self):
        if self.lost:
            self.infoDisplay.showGameoverLabel = True
        else:
            command = self.input.consume()
            if command == input.Input.TOGGLE_PAUSE:
                self.togglePause()
            if not self.paused:
                if command and command != input.Input.TOGGLE_PAUSE:
                    self.board.commandFallingTetromino(command)
                if self.ticker.isTick(self.tickSpeed):
                    rowsCleared, self.lost = self.board.updateTick()
                    self.addRowsCleared(rowsCleared)

    def draw(self):
        self.backgroundImage.blit(0,0)
        self.board.draw()
        self.infoDisplay.draw()
