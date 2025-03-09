import tkinter as tk

# Function for custom button styles
def style_button(btn, bg, hover_bg):
    btn.config(
        bg=bg,
        fg="black",  # Set button text to black
        activebackground=hover_bg,
        activeforeground="black",
        relief="flat",
        borderwidth=0,
        padx=10,
        pady=5,
        font=("Arial", 12)
    )

    # Hover effect
    def on_enter(e):
        btn.config(bg=hover_bg)

    def on_leave(e):
        btn.config(bg=bg)

    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)

# Function template for volume calculation windows
def open_volume_window(title, fields, calc_func):
    window = tk.Toplevel()
    window.title(title)
    window.geometry("500x500")
    window.configure(bg="#2c3e50")  # Dark blue-gray background

    tk.Label(window, text=title, font=("Arial", 14, "bold"), bg="#2c3e50", fg="#ecf0f1").pack(pady=10)

    entries = {}
    for field in fields:
        tk.Label(window, text=f"Enter {field}:", font=("Arial", 12), bg="#2c3e50", fg="#ecf0f1").pack()
        entry = tk.Entry(window, font=("Arial", 12))
        entry.pack()
        entries[field] = entry

    # Unit of measurement selection
    tk.Label(window, text="Select unit of measurement:", font=("Arial", 12), bg="#2c3e50", fg="#ecf0f1").pack()
    unit_var = tk.StringVar(window)
    unit_var.set("cm")  # Default unit

    # Dropdown menu for units
    unit_menu = tk.OptionMenu(window, unit_var, "cm", "m", "in", "ft", "yd")
    unit_menu.config(font=("Arial", 12), bg="#34495e", fg="white", relief="flat")
    unit_menu.pack()

    # Function to calculate volume
    def calculate_volume():
        try:
            values = {field: float(entries[field].get()) for field in fields}
            unit = unit_var.get()
            volume = calc_func(values)
            result_label.config(text=f"Volume: {volume:.2f} {unit}³", font=("Arial", 12, "bold"), fg="#ecf0f1")
        except ValueError:
            result_label.config(text="Please enter valid numbers!", font=("Arial", 12, "bold"), fg="#e74c3c")

    # Calculate button
    calc_button = tk.Button(window, text="Calculate", command=calculate_volume)
    calc_button.pack(pady=10)
    style_button(calc_button, bg="#3498db", hover_bg="#2980b9")

    # Home button to return to main page
    def go_home():
        window.destroy()

    home_button = tk.Button(window, text="Home", command=go_home)
    home_button.pack(pady=5)
    style_button(home_button, bg="#f1c40f", hover_bg="#f39c12")

    # Result label
    result_label = tk.Label(window, text="", bg="#2c3e50")
    result_label.pack()

# Shape-specific calculation functions
def triangle_volume(values):
    return 0.5 * values["base"] * values["height"]

def triangular_prism_volume(values):
    base_area = 0.5 * values["base"] * values["height"]
    return base_area * values["length"]

def rectangular_prism_volume(values):
    return values["length"] * values["width"] * values["height"]

def trapezoidal_prism_volume(values):
    base_area = 0.5 * (values["base1"] + values["base2"]) * values["height"]
    return base_area * values["length"]

# Main window setup
main_window = tk.Tk()
main_window.title("Volume Calculator")
main_window.geometry("800x400")
main_window.configure(bg="#34495e")

# Main layout
main_frame = tk.Frame(main_window, bg="#34495e")
main_frame.pack(fill="both", expand=True, padx=20, pady=20)

# Image section
left_frame = tk.Frame(main_frame, bg="#34495e")
left_frame.grid(row=0, column=0, sticky="n")

image = tk.PhotoImage(file="logo.png")
image_label = tk.Label(left_frame, image=image, bg="#34495e")
image_label.pack()

# Right section for buttons
right_frame = tk.Frame(main_frame, bg="#34495e")
right_frame.grid(row=0, column=1, sticky="n", padx=50)

tk.Label(right_frame, text="Choose a shape to calculate:", font=("Arial", 14, "bold"), bg="#34495e", fg="#ecf0f1").pack(pady=10)

# Buttons for different shapes
buttons = [
    ("Triangle", ["base", "height"], triangle_volume),
    ("Triangular Prism", ["base", "height", "length"], triangular_prism_volume),
    ("Rectangular Prism", ["length", "width", "height"], rectangular_prism_volume),
    ("Trapezoidal Prism", ["base1", "base2", "height", "length"], trapezoidal_prism_volume),
]

for text, fields, func in buttons:
    btn = tk.Button(right_frame, text=text, command=lambda t=text, f=fields, func=func: open_volume_window(f"Calculate for {t}", f, func))
    btn.pack(pady=5)
    style_button(btn, bg="#2ecc71", hover_bg="#27ae60")

main_window.mainloop()
