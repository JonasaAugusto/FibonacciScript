import tkinter as tk

def invert_string(event=None):
    text = box_text.get()
    resultado = text[::-1] #codigo para inverter a string
    result.configure(text=resultado)

window = tk.Tk()
window.geometry("300x100")
box_text = tk.Entry(window, width=30)
box_text.pack(pady=10)
box_text.bind('<Return>', invert_string)
button = tk.Button(window, text="Inverter", command=invert_string)
button.pack()
result = tk.Label(window, text="")
result.pack(pady=10)
window.mainloop()

#aperte enter para enviar a string
