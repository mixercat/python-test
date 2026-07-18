import tkinter

def sayHello():
    print("Hello Adirut!")

def sayHello2():
    print("Hello Adirut2!")

main_window = tkinter.Tk()
main_window.title("Programming Example")
button = tkinter.Button(main_window, text="Click Me Please1", command=sayHello,width=100,fg="blue",bg="yellow").grid(row=0, column=0)   
button2 = tkinter.Button(main_window, text="Click Me Please2", command=sayHello2,width=100,fg="blue",bg="yellow").grid(row=1, column=0)
button3 = tkinter.Button(main_window, text="Click Me Please3", command=sayHello2,width=100,fg="blue",bg="yellow").grid(row=2, column=0)
label = tkinter.Label(main_window, text="Hello Adirut",width=100,fg="blue",bg="gray").grid(row=3, column=0)
main_window.mainloop()