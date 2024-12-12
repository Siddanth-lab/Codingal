from tkinter import *

def convert_to_cm():
    inches = float(entry.get())
    cm = inches * 2.54
    result_label.config(text=f"{cm:.2f} cm")

window = Tk()
window.title("Length Converter")
window.geometry("300x150")

label = Label(window, text="Enter length in inches:")
label.pack()

entry = Entry(window)
entry.pack()

convert_button = Button(window, text="Convert", command=convert_to_cm)
convert_button.pack()

result_label = Label(window, text="")
result_label.pack()

window.mainloop()