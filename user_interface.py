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

    mainWindow.rowconfigure(0, weight=0)
    mainWindow.rowconfigure(1, weight=0)
    mainWindow.rowconfigure(2, weight=0)
    mainWindow.rowconfigure(3, weight=0)
    mainWindow.rowconfigure(4, weight=0)
    mainWindow.rowconfigure(5, weight=0)
    mainWindow.rowconfigure(6, weight=4)

    # username label and entry-field
    user_name_label = tkinter.Label(mainWindow, text='Username')
    user_name_label.grid(row=1, column=0, sticky='e')
    user_name_entry = tkinter.Entry(mainWindow)
    user_name_entry.grid(row=1, column=1, sticky='w')

    # password label and entry-field
    password_label = tkinter.Label(mainWindow, text='Password')
    password_label.grid(row=2, column=0, sticky='e')
    password_entry = tkinter.Entry(mainWindow)
    password_entry.grid(row=2, column=1, sticky='w')

    # hostlist label and entry-field
    hosts_label = tkinter.Label(mainWindow, text='Hosts')
    hosts_label.grid(row=3, column=0, sticky='e')
    hosts_entry = tkinter.Entry(mainWindow)
    hosts_entry.grid(row=3, column=1, sticky='w')

    # skiplist label and entry-field
    skiplist_label = tkinter.Label(mainWindow, text='Ignored hosts')
    skiplist_label.grid(row=4, column=0, sticky='ne')
    skiplist_entry = tkinter.Entry(mainWindow)
    skiplist_entry.grid(row=4, column=1, sticky='nw')

    # mac address number label and drop-down-field
    mac_no_label = tkinter.Label(mainWindow, text='Max allowed Mac addresses')
    mac_no_label.grid(row=1, column=2, sticky='e')
    mac_no_entry = tkinter.Entry(mainWindow) # TODO: make it a drop-down
    mac_no_entry.grid(row=1, column=3, sticky='w')

    # mac address location label and entry-field
    mac_loc_label = tkinter.Label(mainWindow, text='Mac addresses to locate')
    mac_loc_label.grid(row=2, column=2, sticky='e')
    mac_loc_entry = tkinter.Entry(mainWindow)
    mac_loc_entry.grid(row=2, column=3, sticky='w')

    # config search label and entry-field
    config_search_label = tkinter.Label(mainWindow, text='Config-line to find')
    config_search_label.grid(row=3, column=2, sticky='e')
    config_search_entry = tkinter.Entry(mainWindow)
    config_search_entry.grid(row=3, column=3, sticky='w')

    # Radiobuttons for command search
    RBFrame = tkinter.LabelFrame(mainWindow, text='port-type, command-status')
    RBFrame.grid(row=4, column=3, sticky='w')

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

    # buttonwindow
    button_window_label = tkinter.Label(mainWindow, text='Clear')
    button_window_label.grid(row=5, column=3)

    # Clear and Run buttons
    clear_button = tkinter.Button(button_window_label, text='Clear')
    clear_button.grid(row=0, column=0)
    run_button = tkinter.Button(button_window_label, text='Run!')
    run_button.grid(row=0, column=1)

    # main output label and entry-field
    main_output_label = tkinter.Label(mainWindow, text='', relief='ridge', border=2)
    main_output_label.grid(row=6, column=0, columnspan=4, sticky='nsew')





    return mainWindow.mainloop()