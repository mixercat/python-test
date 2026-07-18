from tkinter import Tk, Button

def Left_Click_Button(event):
    print("Left button clicked!")

def Right_Click_Button(event):
    print("Right button clicked!")

def middle_click(event):
    print("Middle button clicked!")

def double_click(event):
    print("Double clicked!")

main = Tk()
main.title("Event Driven Example")
button = Button(main, text="Click Me Please",width=100, height=5,fg="blue", bg="yellow",font=("Arial", 16, "bold"))
button.pack()
button.bind("<Button-1>", Left_Click_Button)
button.bind("<Button-3>", Right_Click_Button)
button.bind("<Button-2>", middle_click)
button.bind("<Double-1>", double_click)
main.mainloop()