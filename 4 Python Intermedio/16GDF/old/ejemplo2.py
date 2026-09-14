import FreeSimpleGUI as sg

layout = [
    [sg.Text("Texto de ejemplo",
             key="-TEXT-",
             font=("Arial", 16))],

    [sg.Input(key="-COLOR-"),
     sg.ColorChooserButton("Color", target="-COLOR-")],

    [sg.Button("Aplicar")]
]

window = sg.Window("Cambiar Color", layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == "Aplicar":
        window["-TEXT-"].update(
            text_color=values["-COLOR-"]
        )

window.close()