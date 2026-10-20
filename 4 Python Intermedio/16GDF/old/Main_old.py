import FreeSimpleGUI as sg

counter = 0

layout = [
    [sg.Text("Haz click en lo que quieras hacer")],
    [sg.Text(counter, key="-COUNTER-")],
    # Añadimos un segundo botón en la misma fila (misma lista)
    [sg.Button("Add New Category"), sg.Button("Restar"), sg.Button("Maximizar"),sg.Button("Normal")],
]

window = sg.Window("Personal Finance Manager", layout, resizable=True, finalize=True)
window.maximize()

while True:
    event, values = window.read()
    
    if event == sg.WIN_CLOSED:
        break
    elif event == "Add New Category":
        layout_secundario = [
            [sg.Text("Categories")],
            # Añadimos un segundo botón en la misma fila (misma lista)
            [sg.Button("Close")],
        ]
        secondary_window = sg.Window(
            "Ventana Secundaria",
            layout_secundario,
        )
        while True:
            event2,v2 = secondary_window.read()
            if event2 in (sg.WIN_CLOSED, "Close"):
                break
        secondary_window.close()
    elif event == "Restar":
        counter -= 1
    elif event == "Maximizar":
        window.maximize()
    elif event == "Normal":
        window.normal()

    # Refrescamos la pantalla con el nuevo valor
    window["-COUNTER-"].update(counter)

window.close()