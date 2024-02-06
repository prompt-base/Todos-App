import PySimpleGUI as sg
import functions

label = sg.Text("Type in a to-do: ")
input_box = sg.Input("", tooltip="Enter a to-do ", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(), key="todos",
                      enable_events=True, size=[45, 15])

edit_button = sg.Button("Edit")

window = sg.Window('My todo App',
                   layout=[[label], [input_box, add_button], [list_box, edit_button]],
                   font=("Helvetica", "15"))
while True:
    event, values = window.Read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values["todo"] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
        case "Edit":
            todo_to_edit = values['todos'][0]
            new_todo = values['todo']
            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case 'todos':
            window['todo'].update(value= values['todos'][0])
        case sg.WIN_CLOSED:
            break

window.close()
