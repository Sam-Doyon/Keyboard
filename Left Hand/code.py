print("Starting")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.split import Split, SplitSide

pins = [
    board.GP21, board.GP9,  board.GP7, board.GP4, board.GP2, board.GP28,
    board.GP20, board.GP12, board.GP8, board.GP5, board.GP3, board.GP27,
    board.GP19, board.GP11, board.GP6, board.GP13, board.GP15, board.GP26,
                                                                                 board.GP16, board.GP17, board.GP18,
    ]



class dactyl_kb(KMKKeyboard):
    def __init__(self):
        super.__init__()

        self.Keyscanner(pins, value_when_pressed=False)

        self.coord_mapping = [
            0,  1,  2,  3,  4, 5,       26, 25, 24, 23, 22, 21,
            6,  7,  8,  9, 10, 11,      32, 31, 30, 29, 28, 27,
            12, 13, 14, 15, 16, 17,    37, 36, 35, 34, 33, 32,
                        18, 19, 20,     40, 39, 38,
                        ]
        

keyboard = dactyl_kb()

split = Split(
    # split_flip=True,
    data_pin=board.pins[1],
    split_side=SplitSide.RIGHT,
    split_target_left=False,
    # Using the default wasn't working, try pio
    # use_pio=True,
    # uart_flip=True,
)

keyboard.keymap = [
    [
    KC.N0, KC.Q, KC.W, KC.E, KC.R, KC.T,
    KC.N1, KC.A, KC.S, KC.D, KC.F, KC.G,
    KC.N2, KC.Z, KC.X, KC.C, KC.V, KC.B,
                KC.LEFT_CONTROL, KC.SPACE, KC.LEFT_SHIFT,
    ]
]

if __name__ == '__main__':
    keyboard.go()















# keyboard = KMKKeyboard()

# keyboard.col_pins = (
#     board.GP21, board.GP9,  board.GP7, board.GP4, board.GP2, board.GP28,
#     board.GP20, board.GP12, board.GP8, board.GP5, board.GP3, board.GP27,
#     board.GP19, board.GP11, board.GP6, board.GP13, board.GP15, board.GP26,
#                                                                                  board.GP16, board.GP17, board.GP18,
#     )
# keyboard.row_pins = (board.GP1,)
# keyboard.diode_orientation = DiodeOrientation.COL2ROW

# keyboard.keymap = [
#     [
#     KC.N0, KC.Q, KC.W, KC.E, KC.R, KC.T,
#     KC.N1, KC.A, KC.S, KC.D, KC.F, KC.G,
#     KC.N2, KC.Z, KC.X, KC.C, KC.V, KC.B,
#                                          KC.LEFT_CONTROL, KC.SPACE, KC.LEFT_SHIFT,
#     ]
# ]

# if __name__ == '__main__':
#     keyboard.go()