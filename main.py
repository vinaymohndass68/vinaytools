import tkinter as tk

def on_button_click():
    user_input = entry.get()  # Get the text from the entry field
    label_result.config(text=f"Hello, {user_input}!",font=("Arial", 14))

# Create the main application window
root = tk.Tk()
root.title("Tkinter Example")

# Add a label
label = tk.Label(root, text="Enter your name:", font=("Arial", 14))
label.pack(pady=10)  # Add some padding around the label

# Add an entry field
entry = tk.Entry(root)
entry.pack(pady=10)

# Add a button
button = tk.Button(root, text="Click Me", command=on_button_click)
button.pack(pady=10)

# Add a result label (to display the result after clicking the button)
label_result = tk.Label(root, text="")
label_result.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()