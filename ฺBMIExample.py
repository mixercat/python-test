from tkinter import Entry, Tk, Button, Label, font

def calculate_bmi():
    height = float(textHeight.get())
    height_cm = height / 100
    weight = float(textWeight.get())
    bmi = weight / (height_cm ** 2)
    resultLabel.config(text=f"BMI: {bmi}")
    resultCriterionLabel.config(text=f"Criterion: {criterion(bmi)}")
    print(f"Height: {height} cm, Weight: {weight} kg, BMI: {bmi}, Criterion: {criterion(bmi)}")

def criterion(bmi):
        if bmi < 18.5:
            return "Underweight"
        elif 18.5 <= bmi < 24.9:
            return "Normal weight"
        elif 25 <= bmi < 29.9:
            return "Overweight"
        else:
            return "Obesity"

main = Tk()
main.title("BMI Calculator")

labelHeight = Label(main, text="Height (cm):", font=("Arial", 20), width=20).grid(row=0, column=0)
textHeight = Entry(main, font=("Arial", 20))
textHeight.grid(row=0, column=1)

labelWeight = Label(main, text="Weight (kg):", font=("Arial", 20), width=20).grid(row=1, column=0)
textWeight = Entry(main, font=("Arial", 20))
textWeight.grid(row=1, column=1)

buttonCalculate = Button(main, text="Calculate BMI", font=("Arial", 20), command=calculate_bmi)
buttonCalculate.grid(row=2, column=0, columnspan=2)

resultLabel = Label(main, text="BMI: ", font=("Arial", 20), width=20)
resultLabel.grid(row=3, column=0, columnspan=2)

resultCriterionLabel = Label(main, text="Criterion: ", font=("Arial", 20), width=20)
resultCriterionLabel.grid(row=4, column=0, columnspan=2)

main.mainloop()