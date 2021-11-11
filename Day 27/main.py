from tkinter import *

# Window
window = Tk()
window.title("Day 27 Project Unit Converter")
window.config(padx=20, pady=20)

# Labels
conversion_input_label = Label(text="Miles")
is_equal_to_label = Label(text="Is Equal To")
conversion_output = Label(text="0")
conversion_output_label = Label(text="Km")


def conversion_type_change():
    global conversion_type
    global conversion_input_label
    global conversion_output_label
    if conversion_type.get() == 1:
        conversion_input_label["text"] = "Miles"
        conversion_output_label["text"] = "Km"
    elif conversion_type.get() == 2:
        conversion_input_label["text"] = "Inch"
        conversion_output_label["text"] = "Foot"
    elif conversion_type.get() == 3:
        conversion_input_label["text"] = "m"
        conversion_output_label["text"] = "cm"
    covert()


def covert():
    global conversion_type
    global conversion_input
    global conversion_output
    input_value = int(conversion_input.get())
    output_value = 0
    if conversion_type.get() == 1:
        output_value = round(input_value * 1.6, 2)
    elif conversion_type.get() == 2:
        output_value = round(input_value / 12, 2)
    elif conversion_type.get() == 3:
        output_value = round(input_value * 100, 2)
    conversion_output["text"] = output_value


# Radio Buttons
conversion_type = IntVar()
mile_km = Radiobutton(window, text="Mile To Km", value=1, variable=conversion_type, command=conversion_type_change)
inch_foot = Radiobutton(window, text="Inch To Foot", value=2, variable=conversion_type, command=conversion_type_change)
m_cm = Radiobutton(window, text="Meter To Centimeter", value=3, variable=conversion_type,
                   command=conversion_type_change)

# Entry
conversion_input = Entry(width=10)
conversion_input.insert(END, string="0")
conversion_input.focus()

# Button
convert_button = Button(text="Convert", command=covert)

# Widgets Placement
mile_km.grid(column=0, row=0)
inch_foot.grid(column=1, row=0)
m_cm.grid(column=2, row=0)
conversion_input.grid(column=1, row=1)
conversion_input_label.grid(column=2, row=1)
is_equal_to_label.grid(column=0, row=2)
conversion_output.grid(column=1, row=2)
conversion_output_label.grid(column=2, row=2)
convert_button.grid(column=1, row=3)
window.mainloop()
