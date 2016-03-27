import tetromino
import input

class Board(object):

    STARTING_ZONE_HEIGHT = 4 # starting zone is where the dodad spawns above the playfield
    NEXT_X = -5 # location for the 'next' block
    NEXT_Y = 20
    label = None
    def __init__(self, x, y, gridWidth, gridHeight, blockSize):
        self.x = x
        self.y = y # location of the lower left of the playfield
        self.gridWidth = gridWidth
        self.gridHeight = gridHeight # playfiels area in blocks
        self.spawnX = int(gridWidth / 3)
        self.spawnY = gridHeight # location of new block on the playfield.
        self.nextTetromino = tetromino.Tetromino()
        self.fallingTetromino = None
        self.spawnTetromino()
        self.tetrominos = [] # list of settled tetrominos
        self.blockSize = blockSize

    def spawnTetromino(self):
        self.fallingTetromino = self.nextTetromino
        self.nextTetromino = tetromino.Tetromino()
        self.fallingTetromino.setPosition(self.spawnX, self.spawnY)
        self.nextTetromino.setPosition(Board.NEXT_X, Board.NEXT_Y)

    def commandFallingTetromino(self, command):
        self.fallingTetromino.command(command)
        if not self.isValidPosition():
            self.fallingTetromino.undoCommand(command)

    def isValidPosition(self):
        # checks to see if falling tetromino is out of bounds or overalapping
        # a settled tetromino
        settledBlockCoords = []
        for tetro in self.tetrominos:
            settledBlockCoords.extend(tetro.blockBoardCoords)

        for coord in self.fallingTetromino.blockBoardCoords:
            # out of bounds if too far left, too far right, or too far down
            outOfBounds = coord[0] < 0 or coord[0] >= self.gridWidth or coord[1] < 0
            overlapping = coord in settledBlockCoords
            if ( outOfBounds or overlapping ):
                return False
        return True

    # return list fo all grid rows that are filled
    def findFullRows(self):
        # get all the settle block coords
        settledBlockCoords = []
        for tetro in self.tetrominos:
            settledBlockCoords.extend(tetro.blockBoardCoords)

        # loop over all rows from bottom to top of starting zone
        # first initialize the count in the rows to zero
        rowCounts = {}
        for i in range(self.gridHeight + Board.STARTING_ZONE_HEIGHT):
            rowCounts[i] = 0
        # now loop across block coord and add to row
        for coord in settledBlockCoords:
            rowCounts[coord[1]] += 1

        # loop over the rows and look for full ones
        fullRows = []
        for row in rowCounts:
            if rowCounts[row] == self.gridWidth:
                fullRows.append(row)

        return fullRows

    def clearRow(self, gridRow):
        newTetrominos = []
        for tetromino in self.tetrominos:
            if tetromino.clearRowAndAdjustDown(gridRow):
                newTetrominos.append(tetromino)

        self.tetrominos = newTetrominos

    def clearRows(self, girdRows):
        girdRows.sort(reverse=True) # sort for some optimization
        for row in girdRows:
            self.clearRow(row)

    def updateTick(self):
        gameLost = False
        numClearedRows = 0;
        # move down the falling guy,
        self.fallingTetromino.command(input.Input.MOVE_DOWN)
        # if it is invalid
        if not self.isValidPosition():
            # undo the down, put it as settled
            self.fallingTetromino.undoCommand(input.Input.MOVE_DOWN)
            self.tetrominos.append(self.fallingTetromino)
            # check for clearable rows and clear them
            fullRows = self.findFullRows()
            self.clearRows(fullRows)
            gameLost = self.isInStartZone(self.fallingTetromino)
            if not gameLost:
                self.spawnTetromino()
            numClearedRows = len(fullRows)

        # return cleard rows, and gamelost bool
        return (numClearedRows, gameLost)

    def isInStartZone(this, dodad):
        for coords in dodad.blockBoardCoords:
            if ( coords[1] >= this.gridHeight):
                return True
        return False

    def gridCoordsToScreenCoords(self, coords):
        screenCoords = []
        for coord in coords:
            coord = (self.x + coord[0] * self.blockSize, self.y + coord[1] * self.blockSize)
            screenCoords.append(coord)
        return screenCoords

    def draw(self):
        for dodad in self.tetrominos:
            screenCoords = self.gridCoordsToScreenCoords(dodad.blockBoardCoords)
            dodad.draw(screenCoords)

        screenCoords = self.gridCoordsToScreenCoords(self.fallingTetromino.blockBoardCoords)
        self.fallingTetromino.draw(screenCoords)

        screenCoords = self.gridCoordsToScreenCoords(self.nextTetromino.blockBoardCoords)
        self.nextTetromino.draw(screenCoords)

        if self.label: self.label.draw()
