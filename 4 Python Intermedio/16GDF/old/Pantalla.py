import FreeSimpleGUI as sg

layout = [
    [sg.Text("Mockups del Proyecto")],
    [sg.Button("Login")],
    [sg.Button("Principal")],
    [sg.Button("Configuración")]
]

window = sg.Window("Mockups", layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == "Login":
        sg.Window(
            "Login",
            [[sg.Text("Usuario")],
             [sg.Input()],
             [sg.Button("Ingresar")]]
        ).read(close=True)

window.close()