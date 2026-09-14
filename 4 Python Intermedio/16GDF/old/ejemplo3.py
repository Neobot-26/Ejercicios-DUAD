import FreeSimpleGUI as sg

datos = [
    ["Motor 1", "COLOR1"],
    ["Motor 2", "COLOR2"],
    ["Motor 3", "COLOR3"],
    ["Motor 4", "COLOR1"],
    ["Motor 5", "COLOR2"],
    ["Motor 6", "COLOR3"],
    ["Motor 7", "UNKNOWN"],
]

CONFIG_COLORES = {
    "color1":"#00FF00",
    "color2":"#FF0000",
    "color3":"#FFFF00",
    "unknown":"#000081"
    
}
layout = [
    [sg.Table(
        values=datos,
        headings=["Equipo", "Estado"],
        key="-TABLE-",
        num_rows=10,
        auto_size_columns=True
    )]
]

window = sg.Window(
    "Tabla Coloreada",
    layout,
    finalize=True
)

tree = window["-TABLE-"].Widget
for tag, color in CONFIG_COLORES.items():
    tree.tag_configure(tag,foreground=color)

items = tree.get_children()
for index,fila in enumerate(datos):
    estado = fila[1].lower()

    if estado in CONFIG_COLORES:
        tree.item(items[index], tags=(estado,))
    else:
        tree.item(items[index],tags=("unknown",))

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

window.close()