import url_shortener
import tkinter as tk

def submit():
    input_text = input_field.get()
    short_url = url_shortener.shorten_url(input_text)
    output_field.config(state="normal")
    output_field.delete("1.0", tk.END)
    output_field.insert("1.0", short_url)
    output_field.config(state="disabled")

root = tk.Tk()
root.title("Input-Output Example")
root.config(bg="lightblue")

input_label = tk.Label(root, text="Input:", font=("Arial", 16), bg="lightblue")
input_label.grid(row=0, column=0, pady=10)

input_field = tk.Entry(root, font=("Arial", 16), bg="white", relief="ridge", bd=5)
input_field.grid(row=0, column=1, pady=10)

submit_button = tk.Button(root, text="Submit", command=submit, font=("Arial", 16), bg="green", relief="groove", bd=5)
submit_button.grid(row=1, column=0, columnspan=2, pady=10)

output_label = tk.Label(root, text="Output:", font=("Arial", 16), bg="lightblue")
output_label.grid(row=2, column=0, pady=10)

output_field = tk.Text(root, font=("Arial", 16), bg="lightgray", relief="sunken", bd=5, height=5, width=20)
output_field.grid(row=2, column=1, pady=10)
output_field.config(state="disabled")

root.mainloop()

