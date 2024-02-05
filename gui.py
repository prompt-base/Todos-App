import PySimpleGUI as sg
import functions

label = sg.Text("Type in a to-do: ")
input_box = sg.Input("", tooltip = "Enter a to-do ", key="todo")
add_button = sg.Button("Add")

window= sg.Window('My todo App',
                  layout=[[label], [input_box, add_button ]],
                  font=("Helvetica", "20"))
while True:
    event, values = window.Read()
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values["todo"] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
        case sg.WIN_CLOSED:
            break

window.close()