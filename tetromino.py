import tetrominoType
import input

class Tetromino(object):
    RIGHT, DOWN, LEFT, UP = range(4)
    CLOCKWISE_ROTATION = {RIGHT:DOWN, DOWN:LEFT, LEFT:UP, UP:RIGHT}

    def __init__(self):
        # x,y is location in 'blocks' from lower LEFT
        self.x = 0
        self.y = 0
        # initialize with a random type
        self.tetrominoType = tetrominoType.TetrominoType.getRandomTetromino()
        self.orientation = Tetromino.RIGHT
        self.blockBoardCoords = self.calcBLockBoardCoords()

    # calculate the coordinates of each block on the board,
    # using the self.x and y and the coords of the Type
    def calcBLockBoardCoords(self):
        localBlockCoords = self.tetrominoType.localBlockCoordsByOrientation[self.orientation]
        gridCoords = []
        for coord in localBlockCoords:
            gridCoord = (coord[0] + self.x, coord[1] + self.y)
            gridCoords.append(gridCoord)
        return gridCoords

    # location methods
    def setPosition(self,x,y):
        self.x = x
        self.y = y
        self.blockBoardCoords = self.calcBLockBoardCoords()

    def moveDown(self):
        self.y = self.y - 1
        self.blockBoardCoords = self.calcBLockBoardCoords()

    def moveUp(self):
        self.y = self.y + 1
        self.blockBoardCoords = self.calcBLockBoardCoords()

    def moveLeft(self):
        self.x = self.x - 1
        self.blockBoardCoords = self.calcBLockBoardCoords()

    def moveRight(self):
        self.x = self.x + 1
        self.blockBoardCoords = self.calcBLockBoardCoords()

    def rotateClockwise(self):
        self.orientation = Tetromino.CLOCKWISE_ROTATION[self.orientation]
        self.blockBoardCoords = self.calcBLockBoardCoords()

    def rotateCounterClockwise(self):
        self.orientation = Tetromino.CLOCKWISE_ROTATION[self.orientation]
        self.orientation = Tetromino.CLOCKWISE_ROTATION[self.orientation]
        self.orientation = Tetromino.CLOCKWISE_ROTATION[self.orientation]
        self.blockBoardCoords = self.calcBLockBoardCoords()

    def command(self, command):
        if command == input.Input.MOVE_DOWN:
            self.moveDown()
        elif command == input.Input.MOVE_RIGHT:
            self.moveRight()
        elif command == input.Input.MOVE_LEFT:
            self.moveLeft()
        elif command == input.Input.ROTATE_CLOCKWISE:
            self.rotateClockwise()

    def undoCommand(self, command):
        if command == input.Input.MOVE_DOWN:
            self.moveUp()
        elif command == input.Input.MOVE_RIGHT:
            self.moveLeft()
        elif command == input.Input.MOVE_LEFT:
            self.moveRight()
        elif command == input.Input.ROTATE_CLOCKWISE:
            self.rotateCounterClockwise()

    def clearRowAndAdjustDown(self, boardGridRow):
        # so, if this tetromino has a y componsent greater than the boardgridrow
        # move it down.  If it is less, leave it alone, if it is equal, remove it
        # from the coords all together.
        newBlockBoardCoords = []
        for coord in self.blockBoardCoords:
            if coord[1] > boardGridRow:
                adjusted = (coord[0], coord[1]-1)
                newBlockBoardCoords.append(adjusted)
            if coord[1] < boardGridRow:
                newBlockBoardCoords.append(coord)

        self.blockBoardCoords = newBlockBoardCoords
        # finally return a status indicating if there are any blocks left on
        # the board. This helps to tell the board it's okay to stop tracking
        # this one.
        return len(self.blockBoardCoords) > 0

    # draw the dodad to the screen.  screen coords is in pixels
    # the board class figures the pixel location of each block and this class
    # just draws the block at that location
    def draw(self, screenCoords):
        image = self.tetrominoType.blockImage
        for coords in screenCoords:
            image.blit(coords[0], coords[1])
