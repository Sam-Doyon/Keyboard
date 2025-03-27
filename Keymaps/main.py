print("Starting")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.split import Split, SplitSide
from kmk.scanners.keypad import KeysScanner
from kmk.modules.sticky_keys import StickyKeys
from kmk.modules.layers import Layers
from kmk.extensions.media_keys import MediaKeys
from kmk.modules.macros import Press, Release, Tap, Macros

pins = [
    board.GP21, board.GP9,  board.GP7, board.GP4, board.GP2, board.GP28,
    board.GP20, board.GP12, board.GP8, board.GP5, board.GP3, board.GP27,
    board.GP19, board.GP11, board.GP6, board.GP13, board.GP15, board.GP26,
                                                                                 board.GP16, board.GP17, board.GP18,
    ]



class dactyl_kb(KMKKeyboard):
    def __init__(self):
        super().__init__() 

        self.matrix = KeysScanner(pins, value_when_pressed=False)

        self.coord_mapping = [
            0,  1,  2,  3,  4, 5,       26, 25, 24, 23, 22, 21,
            6,  7,  8,  9, 10, 11,      32, 31, 30, 29, 28, 27,
            12, 13, 14, 15, 16, 17,     38, 37, 36, 35, 34, 33,
                        18, 19, 20,     41, 40, 39, 
                        ]
        

        

keyboard = dactyl_kb()

# boardside = "LEFT"  
boardside = "RIGHT" 

if boardside =="RIGHT":
    split = Split(
        split_flip=False, 
        data_pin=board.GP0,
        data_pin2=board.GP1,
        split_side=SplitSide.RIGHT,
        split_target_left=False, 
        # Using the default wasn't working, try pio
        use_pio=True,
        uart_flip=False,
    )
elif boardside =="LEFT": 
    split = Split(
        split_flip=False,
        data_pin=board.GP1,
        data_pin2=board.GP0,
        split_side=SplitSide.LEFT,
        split_target_left=False,
        # Using the default wasn't working, try pio
        use_pio=True,
        uart_flip=False,
    )
keyboard.modules = [split, Layers(), StickyKeys(release_after=500,), Macros(), MediaKeys()]

BLKEY = KC.TG(0)
L1KEY = KC.SK(KC.MO(1), defer_release=False,retap_cancel=False, )
L2KEY = KC.SK(KC.MO(2), defer_release=False,retap_cancel=False,)
L3KEY = KC.MO(3)
sticky_shift = KC.SK(KC.LEFT_SHIFT, defer_release=False, retap_cancel=False)
# sticky_control = KC.SK(KC.LEFT_CONTROL, defer_release=False, retap_cancel=False)
# sticky_alt = KC.SK(KC.RIGHT_ALT, defer_release=False, retap_cancel=False)

CNTRL_ALT_DEL_Macro = KC.MACRO(
    Press(KC.RCTL),
    Press(KC.RIGHT_ALT),
    Tap(KC.DELETE),
    Release(KC.RIGHT_ALT),
    Release(KC.RCTL),
)




keyboard.keymap = [
    [
    KC.ESC, KC.Q, KC.W, KC.E, KC.R, KC.T,                                    KC.Y, KC.U, KC.I,     KC.O,   KC.BACKSPACE, KC.DELETE,
    L1KEY, KC.A, KC.S, KC.D, KC.F, KC.G,                                    KC.H, KC.J, KC.K,     KC.L,   KC.P, L3KEY,
    L2KEY, KC.Z, KC.X, KC.C, KC.V, KC.B,                                    KC.N, KC.M, KC.COMMA, KC.DOT, KC.SLASH, KC.LGUI,
                KC.LEFT_CONTROL, KC.SPACE, sticky_shift,           sticky_shift, KC.ENTER, KC.RIGHT_ALT,
    ],

    [
    BLKEY, KC.EXLM, KC.AT, KC.HASH, KC.DLR, KC.PERC,                        KC.PLUS, KC.LPRN, KC.RPRN, KC.ASTR, KC.BACKSPACE, KC.DELETE,
    KC.TRNS,KC.NO, KC.TAB, KC.AMPR, KC.PIPE, KC.EQUAL,                      KC.COLON, KC.LBRC, KC.RBRC, KC.SCOLON, KC.CIRC, KC.TRNS,
    KC.TRNS, KC.GRAVE, KC.TILDE, KC.QUOTE, KC.DQUO, KC.UNDS,                  KC.MINUS, KC.LCBR, KC.RCBR, KC.DOT, KC.BSLS, KC.TRNS,
                        KC.LEFT_CONTROL, KC.SPACE, KC.LEFT_SHIFT,           KC.LEFT_SHIFT, KC.ENTER, KC.RIGHT_ALT,
    ],

    [
    BLKEY, KC.EXLM, KC.AT, KC.HASH, KC.DLR, KC.PERC,                        KC.MINUS, KC.N7, KC.N8, KC.N9, KC.BACKSPACE, KC.DELETE,
    KC.TRNS,KC.NO, KC.TAB, KC.AMPR, KC.PIPE, KC.EQUAL,                      KC.COLON, KC.N4, KC.N5, KC.N6, KC.N0, KC.TRNS,
    KC.TRNS, KC.GRAVE, KC.TILDE, KC.QUOTE, KC.DQUO, KC.UNDS,                  KC.COMMA, KC.N1, KC.N2, KC.N3, KC.DOT, KC.TRNS,
                        KC.LEFT_CONTROL, KC.SPACE, KC.LEFT_SHIFT,           KC.LEFT_SHIFT, KC.ENTER, KC.RIGHT_ALT,
    ],

    [
    BLKEY, KC.NO, KC.NO, KC.UP, KC.PGUP, KC.VOLU,                        CNTRL_ALT_DEL_Macro, KC.CAPS, KC.NO, KC.NO, KC.BACKSPACE, KC.DELETE,
    KC.TRNS,KC.HOME, KC.LEFT, KC.DOWN, KC.RIGHT, KC.END,                      KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.TRNS,
    KC.TRNS, KC.NO, KC.TILDE, KC.NO, KC.PGDN, KC.VOLD,                  KC.VOLU, KC.VOLD, KC.NO, KC.NO, KC.NO, KC.TRNS,
                        KC.LEFT_CONTROL, KC.SPACE, KC.LEFT_SHIFT,           KC.LEFT_SHIFT, KC.ENTER, KC.RIGHT_ALT,
    ],
]

if __name__ == '__main__':
    keyboard.go()



