print("BMI CALCULATOR")
import tkinter as tk

def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())
        bmi = weight / ((height **2 )/10000)
        result_label.config(text=f"Your BMI is: {bmi:0.2f}")
        
    except ValueError:
        result_label.config(text="Invalid input. Please enter numeric values.")

# Create the main application window
app = tk.Tk()
app.title("BMI Calculator")

# Create labels and entry widgets for weight and height
weight_label = tk.Label(app, text="Enter your weight (kg):")
weight_label.pack()
weight_entry = tk.Entry(app)
weight_entry.pack()

height_label = tk.Label(app, text="Enter your height (cm):")
height_label.pack()
height_entry = tk.Entry(app)
height_entry.pack()

# Create a button to calculate BMI
calculate_button = tk.Button(app, text="Calculate BMI", command=calculate_bmi)
calculate_button.pack()

# Create a label to display the result
result_label = tk.Label(app, text="")
result_label.pack()

# Start the GUI main loop
app.mainloop()

