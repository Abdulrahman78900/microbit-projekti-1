input.onGesture(Gesture.Shake, function () {
    kivi_paperi_sakset = randint(1, 3)
})
input.onButtonPressed(Button.A, function () {
    basic.showLeds(`
        . . . . .
        . . # . .
        . # . # .
        . # # # .
        . # . # .
        `)
})
input.onButtonPressed(Button.B, function () {
    basic.showLeds(`
        . # # # .
        . # . # .
        . # # . .
        . # . # .
        . # # # .
        `)
})
let kivi_paperi_sakset = 0
basic.showLeds(`
    . # . # .
    . . . . .
    # . . . #
    . # . # .
    . . # . .
    `)
