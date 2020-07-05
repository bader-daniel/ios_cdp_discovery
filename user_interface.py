import tkinter

def tkinter_ui():
    mainWindow = tkinter.Tk()
    mainWindow.title("Network Discovery Tool")
    mainWindow.geometry('1024x768')

    label = tkinter.Label(mainWindow, text="Network Discovery Tool - Daniel Bader - NK-Tjänst AB")
    label.grid(row=0, column=0, columnspan=4)

    mainWindow.columnconfigure(0, weight=1)
    mainWindow.columnconfigure(1, weight=2)
    mainWindow.columnconfigure(2, weight=1)
    mainWindow.columnconfigure(3, weight=2)
    #mainWindow.columnconfigure(4, weight=4, pad=0)

    #  topScreen = tkinter.Label(mainWindow)
    #  topScreen.grid(row=0, column)

    mainWindow.rowconfigure(0, weight=1)
    mainWindow.rowconfigure(1, weight=2)
    mainWindow.rowconfigure(2, weight=1)
    mainWindow.rowconfigure(3, weight=2)
    mainWindow.rowconfigure(4, weight=1)
    mainWindow.rowconfigure(5, weight=2)
    mainWindow.rowconfigure(6, weight=8)

    RBFrame = tkinter.LabelFrame(mainWindow, text='port-type, command-status')
    RBFrame.grid(row=4, column=3, sticky='ne')

    RBPort_type = tkinter.IntVar()
    RBPort_type.set(4)

    radio1 = tkinter.Radiobutton(RBFrame, text='Access, present', value=1, variable=RBPort_type)
    radio2 = tkinter.Radiobutton(RBFrame, text='Trunk, present', value=2, variable=RBPort_type)
    radio3 = tkinter.Radiobutton(RBFrame, text='Access, missing', value=3, variable=RBPort_type)
    radio4 = tkinter.Radiobutton(RBFrame, text='Trunk, missing', value=4, variable=RBPort_type)

    radio1.grid(row=1, column=0, sticky='w')
    radio2.grid(row=1, column=1, sticky='e')
    radio3.grid(row=2, column=0, sticky='w')
    radio4.grid(row=2, column=1, sticky='e')




    return mainWindow.mainloop()