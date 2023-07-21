import tkinter as tk

def on_click(event):
    current_text = result_label["text"]
    clicked_text = event.widget.cget("text")

    if clicked_text == "=":
        try:
            result = eval(current_text)
            result_label["text"] = str(result)
        except Exception as e:
            result_label["text"] = "Error"
    elif clicked_text == "C":
        result_label["text"] = ""
    else:
        result_label["text"] = current_text + clicked_text

# Create the main application window
root = tk.Tk()
root.title("Calculator")

# Create the result label
result_label = tk.Label(root, text="", bg="white", fg="black", font=("Helvetica", 20))
result_label.pack(fill=tk.BOTH, expand=True)

# Create the calculator buttons
button_texts = [
    ("7", "8", "9", "/"),
    ("4", "5", "6", "*"),
    ("1", "2", "3", "-"),
    ("C", "0", "=", "+")
]

for row in button_texts:
    frame = tk.Frame(root)
    frame.pack(fill=tk.BOTH, expand=True)

    for button_text in row:
        button = tk.Button(frame, text=button_text, font=("Helvetica", 16), relief="ridge")
        button.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        button.bind("<Button-1>", on_click)

# Start the main event loop
root.mainloop()
