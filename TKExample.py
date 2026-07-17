import tkinter

def sayHello():
    print("Hello Adirut!")

main_window = tkinter.Tk()
main_window.title("Programming Example")
button = tkinter.Button(main_window, text="Click Me Please1", command=sayHello)
button.place(x=250, y=250)
button2 = tkinter.Button(main_window, text="Click Me Please2", command=sayHello)
button2.place(x=50, y=50)
main_window.mainloop()