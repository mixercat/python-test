from tkinter import Entry, Tk, Button, Label, font

def calculate_bmi():
    height = float(textHeight.get())
    height_cm = height / 100
    weight = float(textWeight.get())
    bmi = weight / (height_cm ** 2)
    resultLabel.config(text=f"BMI: {bmi}")
    print(f"Height: {height} cm, Weight: {weight} kg, BMI: {bmi}")

main = Tk()
main.title("BMI Calculator")

labelHeight = Label(main, text="Height (cm):", font=("Arial", 12)).grid(row=0, column=0)
textHeight = Entry(main, font=("Arial", 12))
textHeight.grid(row=0, column=1)

labelWeight = Label(main, text="Weight (kg):", font=("Arial", 12)).grid(row=1, column=0)
textWeight = Entry(main, font=("Arial", 12))
textWeight.grid(row=1, column=1)

buttonCalculate = Button(main, text="Calculate BMI", font=("Arial", 12), command=calculate_bmi)
buttonCalculate.grid(row=2, column=0, columnspan=2)
resultLabel = Label(main, text="BMI: ", font=("Arial", 12))
resultLabel.grid(row=3, column=0, columnspan=2)
main.mainloop()