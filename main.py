def on_gesture_shake():
    global kivi_paperi_sakset
    kivi_paperi_sakset = randint(1, 3)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_button_pressed_a():
    basic.show_leds("""
        . . . . .
        . . # . .
        . # . # .
        . # # # .
        . # . # .
        """)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    basic.show_leds("""
        . # # # .
        . # . # .
        . # # . .
        . # . # .
        . # # # .
        """)
input.on_button_pressed(Button.B, on_button_pressed_b)

kivi_paperi_sakset = 0
basic.show_leds("""
    . # . # .
    . . . . .
    # . . . #
    . # . # .
    . . # . .
    """)