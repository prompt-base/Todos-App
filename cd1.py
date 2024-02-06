import PySimpleGUI as sg
import convertercd1 as converter
#Texts
feet_text=sg.Text("Enter Feet: ")
inches_text=sg.Text("Enter Inches: ")
#Prompts
feet_prompt = sg.Input("", key="Feet")
inches_prompt = sg.Input("", key="Inches")
result = sg.Text("", key="res")
#Buttons
convert_button = sg.Button("Convert")
#Creating a Window
window = sg.Window("Converter", layout=[[feet_text, feet_prompt],[inches_text, inches_prompt]
                                        ,[convert_button, result]])
while True:
    events, values = window.Read()
    print(events)
    print(values)
    feet = float(values["Feet"])
    inches = float(values["Inches"])
    meters = converter.convert(feet, inches)
    window["res"].update(value=f"{meters}m", text_color="white")

window.Close()

















