def on_forever():
    led.plot_bar_graph(input.sound_level(), 255)
basic.forever(on_forever)
