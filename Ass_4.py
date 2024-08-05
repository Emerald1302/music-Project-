import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry('400x300')
root.title('BMI Calculator')


tk.Label(root, text='Enter Weight in lb').pack()
textbox1 = ttk.Entry(root, textvariable = tk.StringVar())
textbox1.pack()


tk.Label(root, text='Enter Height in cm').pack()
textbox2 = ttk.Entry(root, textvariable = tk.StringVar())
textbox2.pack()

result= tk.Label(root,  text='' ,font=("Helvetica", 14))
result.pack()

def button_clicked():
    weight=int(textbox1.get())
    height_cm=int(textbox2.get())
    height_inches=height_cm*0.393701
    bmi= (weight/height_inches**2 )*703 
    result.config(text=f'Your BMI is: {bmi}')  


button = ttk.Button(root, text='BMI', command=button_clicked)
button.pack()


root.mainloop()
