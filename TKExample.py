import tkinter

def sayHello():
    print("Hello Adirut!")

main_window = tkinter.Tk()
main_window.title("Programming Example")
button = tkinter.Button(main_window, text="Click Me Please", command=sayHello)
button.place(x=50, y=50)
main_window.mainloop()