import FreeSimpleGUI as sg

datos = [
    ["Motor 1", "Activo", 25.3],
    ["Motor 2", "Detenido", 0.0],
    ["Motor 3", "Activo", 27.8]
]

layout = [
    [
        sg.Table(
            values=datos,
            headings=["Equipo", "Estado", "Temperatura"],
            auto_size_columns=True,
            display_row_numbers=False,
            justification="center",
            num_rows=10,
            key="-TABLA-"
        )
    ]
]

window = sg.Window("Ejemplo de Tabla", layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

window.close()