import random
import tetromino

class TetrominoType(object):
    def __init__(self, blockImage, localBlockCoordsByOrientation):
        self.blockImage = blockImage
        self.localBlockCoordsByOrientation =localBlockCoordsByOrientation;

    @staticmethod
    def classInit(blocksImage, blockSize):
        a = blocksImage.get_region(x=0,y=0, width=blockSize, height=blockSize)
        b = blocksImage.get_region(x=blockSize,y=0, width=blockSize, height=blockSize)
        c = blocksImage.get_region(x=blockSize*2,y=0, width=blockSize, height=blockSize)
        d = blocksImage.get_region(x=blockSize*3,y=0, width=blockSize, height=blockSize)
        e = blocksImage.get_region(x=blockSize*4,y=0, width=blockSize, height=blockSize)
        f = blocksImage.get_region(x=blockSize*5,y=0, width=blockSize, height=blockSize)
        g = blocksImage.get_region(x=blockSize*6,y=0, width=blockSize, height=blockSize)

        # this is like an enum class
        TetrominoType.TYPES = [   # line shape
            TetrominoType(g,
                {
                    tetromino.Tetromino.RIGHT: [(0, 1), (1, 1), (2, 1), (3, 1)],
                    tetromino.Tetromino.DOWN:  [(1, 0), (1, 1), (1, 2), (1, 3)],
                    tetromino.Tetromino.LEFT:  [(0, 2), (1, 2), (2, 2), (3, 2)],
                    tetromino.Tetromino.UP:    [(2, 0), (2, 1), (2, 2), (2, 3)],
                }),
            TetrominoType(b,   # square shape
                {
                    tetromino.Tetromino.RIGHT: [(0, 0), (0, 1), (1, 0), (1, 1)],
                    tetromino.Tetromino.DOWN:  [(0, 0), (0, 1), (1, 0), (1, 1)],
                    tetromino.Tetromino.LEFT:  [(0, 0), (0, 1), (1, 0), (1, 1)],
                    tetromino.Tetromino.UP:    [(0, 0), (0, 1), (1, 0), (1, 1)],
                }),
            TetrominoType(c,  # L shape
                {
                    tetromino.Tetromino.RIGHT: [(0, 1), (1, 1), (2, 1), (2, 2)],
                    tetromino.Tetromino.DOWN: [(1, 2), (1, 1), (1, 0), (2, 0)],
                    tetromino.Tetromino.LEFT: [(0, 0), (0, 1), (1, 1), (2, 1)],
                    tetromino.Tetromino.UP: [(0, 2), (1, 2), (1, 1), (1, 0)]
                }
            ),
            TetrominoType(d,  # reverse L shape
                {
                    tetromino.Tetromino.RIGHT: [(0, 2), (0, 1), (1, 1), (2, 1)],
                    tetromino.Tetromino.DOWN: [(2, 2), (1, 2), (1, 1), (1, 0)],
                    tetromino.Tetromino.LEFT: [(0, 1), (1, 1), (2, 1), (2, 0)],
                    tetromino.Tetromino.UP: [(0, 0), (1, 0), (1, 1), (1, 2)]
                }
            ),
            TetrominoType(e,   # Z shape
                {
                    tetromino.Tetromino.RIGHT: [(0, 2), (1, 2), (1, 1), (2, 1)],
                    tetromino.Tetromino.DOWN: [(2, 2), (2, 1), (1, 1), (1, 0)],
                    tetromino.Tetromino.LEFT: [(0, 1), (1, 1), (1, 0), (2, 0)],
                    tetromino.Tetromino.UP: [(0, 0), (0, 1), (1, 1), (1, 2)]
                }
            ),
            TetrominoType(f,    # S shape
                {
                    tetromino.Tetromino.RIGHT: [(0, 1), (1, 1), (1, 2), (2, 2)],
                    tetromino.Tetromino.DOWN: [(1, 2), (1, 1), (2, 1), (2, 0)],
                    tetromino.Tetromino.LEFT: [(0, 0), (1, 0), (1, 1), (2, 1)],
                    tetromino.Tetromino.UP: [(0, 2), (0, 1), (1, 1), (1, 0)]
                }
            ),
            TetrominoType(a, # T shape
                {
                    tetromino.Tetromino.RIGHT: [(0, 1), (1, 1), (1, 2), (2, 1)],
                    tetromino.Tetromino.DOWN: [(1, 2), (1, 1), (1, 0), (2, 1)],
                    tetromino.Tetromino.LEFT: [(0, 1), (1, 1), (1, 0), (2, 1)],
                    tetromino.Tetromino.UP: [(0, 1), (1, 0), (1, 1), (1, 2)]
                }
            )]
    @staticmethod
    def getRandomTetromino():
        return random.choice(TetrominoType.TYPES)
