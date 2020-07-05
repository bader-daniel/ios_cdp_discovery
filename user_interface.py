import tkinter

def tkinter_ui():
    # values_from_inputs = []
    mainWindow = tkinter.Tk()
    mainWindow.title("Network Discovery Tool")
    mainWindow.geometry('1024x768')

    label = tkinter.Label(mainWindow, text="Network Discovery Tool - Daniel Bader - NK-Tjänst AB")
    label.grid(row=0, column=0, columnspan=6)

    mainWindow.columnconfigure(0, weight=0)
    mainWindow.columnconfigure(1, weight=0)
    mainWindow.columnconfigure(2, weight=0)
    mainWindow.columnconfigure(3, weight=0)
    mainWindow.columnconfigure(4, weight=0)
    mainWindow.columnconfigure(5, weight=0)

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

    # Set up variables to be used in drop-down
    man_number_var_type = tkinter.IntVar()
    man_number_var_type.set(0)

    mac_no_label = tkinter.Label(mainWindow, text='Max allowed Mac addresses')
    mac_no_label.grid(row=1, column=2, sticky='e')
    mac_no_entry = tkinter.OptionMenu(mainWindow, man_number_var_type, *(0, 1, 2, 3, 4, 5, 6, 7, 8, 9))
    mac_no_entry.grid(row=1, column=3, sticky='w')

    # mac address location label and entry-field
    mac_loc_label = tkinter.Label(mainWindow, text='Mac addresses to locate')
    mac_loc_label.grid(row=2, column=2, sticky='e')
    mac_loc_entry = tkinter.Entry(mainWindow)
    mac_loc_entry.grid(row=2, column=3, sticky='w')

    # config search label and entry-field
    config_search_label = tkinter.Label(mainWindow, text='Config-line to find')
    config_search_label.grid(row=1, column=4, sticky='e')
    config_search_entry = tkinter.Entry(mainWindow)
    config_search_entry.grid(row=1, column=5, sticky='w')

    # Search access or trunk radiobuttons and Label
    port_type_label = tkinter.Label(mainWindow, text='Search Access or Trunk ports?')
    port_type_label.grid(row=2, column=4, sticky='e')
    port_type_rb_frame = tkinter.LabelFrame(mainWindow, text='port-type')
    port_type_rb_frame.grid(row=2, column=5, sticky='w')

    port_type_rb_type = tkinter.IntVar()
    port_type_rb_type.set(2)

    radio1 = tkinter.Radiobutton(port_type_rb_frame, text='Access', value=1, variable=port_type_rb_type)
    radio2 = tkinter.Radiobutton(port_type_rb_frame, text='Trunk', value=2, variable=port_type_rb_type)

    radio1.grid(row=1, column=0, sticky='w')
    radio2.grid(row=1, column=1, sticky='e')


    # Search for present or missing string radiobuttons and Label

    port_command_label = tkinter.Label(mainWindow, text='Command Absent or Present?')
    port_command_label.grid(row=3, column=4, sticky='e')
    port_command_rb_frame = tkinter.LabelFrame(mainWindow, text='command-status')
    port_command_rb_frame.grid(row=3, column=5, sticky='w')

    port_command_rb_type = tkinter.IntVar()
    port_command_rb_type.set(2)

    radio1 = tkinter.Radiobutton(port_command_rb_frame, text='present', value=1, variable=port_command_rb_type)
    radio2 = tkinter.Radiobutton(port_command_rb_frame, text='absent', value=2, variable=port_command_rb_type)

    radio1.grid(row=1, column=0, sticky='w')
    radio2.grid(row=1, column=1, sticky='e')


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
    main_output_label.grid(row=6, column=0, columnspan=6, sticky='nsew')

    return mainWindow.mainloop()


def generated_map():
    pass