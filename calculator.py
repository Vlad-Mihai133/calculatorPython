from tkinter import *

# expresia propriu-zisa
expression = ""


def press(num, equation):
    global expression
    if num == "<-":
        expression = expression[:-1]
    else:
        expression = expression + str(num)
    equation.set(expression)


# pentru operatia 'egal'
def equalpress(equation):
    global expression
    try:
        total = str(eval(expression))
        equation.set(total)
        expression = str(total)
    except:
        equation.set("error")
        expression = ""


def clear(equation):
    global expression
    expression = ""
    equation.set(expression)


# functia ce ne creeaza un GUI
def build_window():
    gui = Tk()
    gui.configure(background="darkgrey")
    gui.title("Calculator")
    gui.geometry("350x360")
    gui.resizable(False, False)
    equation = StringVar()
    equation.set("")
    expression_field = Entry(gui, textvariable=equation, bg="whitesmoke")
    expression_field.grid(columnspan=10, ipadx=120, ipady=20)
    # operanzi
    button1 = Button(gui, text="1", fg="black", bg="gainsboro", activebackground="lightgray",
                     activeforeground="darkgray", command=lambda: press(1, equation), height=3, width=10)
    button1.grid(row=3, column=0)
    button2 = Button(gui, text="2", fg="black", bg="gainsboro", activebackground="lightgray",
                     activeforeground="darkgray", command=lambda: press(2, equation), height=3, width=10)
    button2.grid(row=3, column=1)
    button3 = Button(gui, text="3", fg="black", bg="gainsboro", activebackground="lightgray",
                     activeforeground="darkgray", command=lambda: press(3, equation), height=3, width=10)
    button3.grid(row=3, column=2)
    button4 = Button(gui, text="4", fg="black", bg="gainsboro", activebackground="lightgray",
                     activeforeground="darkgray", command=lambda: press(4, equation), height=3, width=10)
    button4.grid(row=2, column=0)
    button5 = Button(gui, text="5", fg="black", bg="gainsboro", activebackground="lightgray",
                     activeforeground="darkgray", command=lambda: press(5, equation), height=3, width=10)
    button5.grid(row=2, column=1)
    button6 = Button(gui, text="6", fg="black", bg="gainsboro", activebackground="lightgray",
                     activeforeground="darkgray", command=lambda: press(6, equation), height=3, width=10)
    button6.grid(row=2, column=2)
    button7 = Button(gui, text="7", fg="black", bg="gainsboro", activebackground="lightgray",
                     activeforeground="darkgray", command=lambda: press(7, equation), height=3, width=10)
    button7.grid(row=1, column=0)
    button8 = Button(gui, text="8", fg="black", bg="gainsboro", activebackground="lightgray",
                     activeforeground="darkgray", command=lambda: press(8, equation), height=3, width=10)
    button8.grid(row=1, column=1)
    button9 = Button(gui, text="9", fg="black", bg="gainsboro", activebackground="lightgray",
                     activeforeground="darkgray", command=lambda: press(9, equation), height=3, width=10)
    button9.grid(row=1, column=2)
    button0 = Button(gui, text="0", fg="black", bg="gainsboro", activebackground="lightgray",
                     activeforeground="darkgray", command=lambda: press(0, equation), height=3, width=10)
    button0.grid(row=4, column=1)
    # operatori
    buttonclear = Button(gui, text="C", fg="black", bg="gainsboro", activebackground="lightgray",
                         activeforeground="darkgray", command=lambda: clear(equation), height=3, width=10)
    buttonclear.grid(row=4, column=2)
    buttonplus = Button(gui, text="+", fg="black", bg="gainsboro", activebackground="lightgray",
                        activeforeground="darkgray", command=lambda: press("+", equation), height=3, width=10)
    buttonplus.grid(row=1, column=4)
    buttonminus = Button(gui, text="-", fg="black", bg="gainsboro", activebackground="lightgray",
                         activeforeground="darkgray", command=lambda: press("-", equation), height=3, width=10)
    buttonminus.grid(row=2, column=4)
    buttonprod = Button(gui, text="*", fg="black", bg="gainsboro", activebackground="lightgray",
                        activeforeground="darkgray", command=lambda: press("*", equation), height=3, width=10)
    buttonprod.grid(row=3, column=4)
    buttondiv = Button(gui, text="/", fg="black", bg="gainsboro", activebackground="lightgray",
                       activeforeground="darkgray", command=lambda: press("/", equation), height=3, width=10)
    buttondiv.grid(row=4, column=4)
    buttonpd = Button(gui, text="(", fg="black", bg="gainsboro", activebackground="lightgray",
                      activeforeground="darkgray", command=lambda: press("(", equation), height=3, width=10)
    buttonpd.grid(row=5, column=0)
    buttonpi = Button(gui, text=")", fg="black", bg="gainsboro", activebackground="lightgray",
                      activeforeground="darkgray", command=lambda: press(")", equation), height=3, width=10)
    buttonpi.grid(row=5, column=1)
    buttondellast = Button(gui, text="<-", fg="black", bg="gainsboro", activebackground="lightgray",
                           activeforeground="darkgray", command=lambda: press("<-", equation), height=3, width=10)
    buttondellast.grid(row=4, column=0)
    buttonegal = Button(gui, text="=", fg="white", bg="royalblue", activebackground="cornflowerblue",
                        activeforeground="gainsboro", command=lambda: equalpress(equation), height=3, width=10)
    buttonegal.grid(row=5, column=2)

    # functia ce ne deschide fereastra
    gui.mainloop()


if __name__ == '__main__':
    build_window()
