print("Starting")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

keyboard = KMKKeyboard()

keyboard.col_pins = (
    board.GP21, board.GP9,  board.GP7, board.GP4, board.GP2, board.GP28,
    board.GP20, board.GP12, board.GP8, board.GP5, board.GP3, board.GP27,
    board.GP19, board.GP11, board.GP6, board.GP13, board.GP15, board.GP26,
                                                                                 board.GP16, board.GP17, board.GP18,
    )
keyboard.row_pins = (board.GP1,)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [
    [
                                        KC.Q, KC.W, KC.E, KC.R, KC.BACKSPACE, KC.N0,
                                        KC.A, KC.S, KC.D, KC.F, KC.G, KC.N1,
                                        KC.Z, KC.X, KC.C, KC.V, KC.B, KC.N2,
    KC.LEFT_CONTROL, KC.SPACE, KC.LEFT_SHIFT,
    ]
]

if __name__ == '__main__':
    keyboard.go()