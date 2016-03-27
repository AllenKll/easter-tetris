import pyglet

class InfoDisplay(object):
    ''' display of text messages '''
    ROWS_CLEARED_X = 70
    ROWS_CLEARED_Y = 550

    def __init__(self, window):
        self.rowsClearedLabel = pyglet.text.Label('Rows cleared: 0',
                                                    font_size=14,
                                                    x=InfoDisplay.ROWS_CLEARED_X,
                                                    y=InfoDisplay.ROWS_CLEARED_Y)
        self.rowsClearedLabel.set_style('background_color', (0,0,0,127))

        self.pausedLabel = pyglet.text.Label('PAUSED',
                                             font_size=32,
                                             x=window.width // 2,
                                             y=window.height // 2,
                                             anchor_x='center',
                                             anchor_y='center')
        self.pausedLabel.set_style('background_color', (0,0,0,127))

        self.gameoverLabel = pyglet.text.Label('GAME OVER',
                                                font_size=32,
                                                x=window.width // 2,
                                                y=window.height // 2,
                                                anchor_x='center',
                                                anchor_y='center')
        self.gameoverLabel.set_style('background_color', (0,0,0,127))

        self.showPausedLabel = False
        self.showGameoverLabel = False

    def draw(self):
        self.rowsClearedLabel.draw()
        if self.showPausedLabel:
            self.pausedLabel.draw()
        if self.showGameoverLabel:
            self.gameoverLabel.draw()

    def setRowsCleared(self, numRowsCleared):
        self.rowsClearedLabel.text = 'Rows cleared: ' + str(numRowsCleared)
