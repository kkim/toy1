def on_button_pressed_a():
    global B
    B = 1
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global B
    B = 0
input.on_button_pressed(Button.B, on_button_pressed_b)

A = 0
B = 0
basic.show_leds("""
    . . . . .
    . # . # .
    . . . . .
    # . . . #
    . # # # .
    """)

def on_forever():
    global A
    if B == 0:
        A = input.compass_heading()
    else:
        A = input.rotation(Rotation.PITCH)
    if A > 0 and A < 45:
        basic.show_leds("""
            . . # . .
            . # # # .
            # . # . #
            . . # . .
            . . # . .
            """)
    elif A > 90 and A < 135:
        basic.show_leds("""
            . . # . .
            . # . . .
            # # # # #
            . # . . .
            . . # . .
            """)
    elif A > 180 and A < 225:
        basic.show_leds("""
            . . # . .
            . . # . .
            # . # . #
            . # # # .
            . . # . .
            """)
    elif A > 270 and A < 315:
        basic.show_leds("""
            . . # . .
            . . . # .
            # # # # #
            . . . # .
            . . # . .
            """)
    elif A >= 45 and A < 90:
        basic.show_leds("""
            # # # . .
            # # . . .
            # . # . .
            . . . # .
            . . . . #
            """)
    elif A >= 135 and A < 180:
        basic.show_leds("""
            . . . . #
            . . . # .
            # . # . .
            # # . . .
            # # # . .
            """)
    elif A >= 225 and A < 270:
        basic.show_leds("""
            # . . . .
            . # . . .
            . . # . #
            . . . # #
            . . # # #
            """)
    else:
        basic.show_leds("""
            . . # # #
            . . . # #
            . . # . #
            . # . . .
            # . . . .
            """)
basic.forever(on_forever)
