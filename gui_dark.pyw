import tkinter as tk

root = tk.Tk()
root.title('Heart Rate Calculator')
root.config(bg='#FFC48C')

box_input = tk.Entry(root)
output_label = tk.Label(root, text='Method:', fg='black', bg='#FFC48C')

box_input.grid(row=1, column=1)
output_label.grid(row=3, column=0, columnspan=2)

def calculate_solution():
    method = method_var.get().lower()

    if method == '1500':
        try:
            squares_inp = int(box_input.get())
            solution = 1500 / squares_inp
            output_label.config(text=f'{method} Method: {solution} BPM')
        except ValueError:
            output_label.config(text='Invalid input')
    elif method == '300':
        try:
            box_inp = int(box_input.get())
            solution = 300 / box_inp
            output_label.config(text=f'{method} Method: {solution} BPM')
        except ValueError:
            output_label.config(text='Invalid input')
    elif method == '6sec':
        try:
            sec_inp = int(box_input.get())
            solution = sec_inp * 10
            output_label.config(text=f'{method} Method: {solution} BPM')
        except ValueError:
            output_label.config(text='Invalid input')
    else:
        output_label.config(text=f'Invalid method. "{method}"')

method_var = tk.StringVar(value='1500')

method_1500 = tk.Radiobutton(root, text='1500', variable=method_var, value='1500', bg='#FFC48C')
method_300 = tk.Radiobutton(root, text='300', variable=method_var, value='300', bg='#FFC48C')
method_6sec = tk.Radiobutton(root, text='6sec', variable=method_var, value='6sec', bg='#FFC48C')

calc_button = tk.Button(root, text='Calculate', command=calculate_solution)

method_1500.grid(row=0, column=0)
method_300.grid(row=0, column=1)
method_6sec.grid(row=0, column=2)
calc_button.grid(row=4, column=0, columnspan=2)

root.mainloop()
