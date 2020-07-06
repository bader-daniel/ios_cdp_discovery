import tkinter


class UserInterface:

    def __init__(self):
        # values_from_inputs = []
        self.mainWindow = tkinter.Tk()
        self.mainWindow.title("Network Discovery Tool")
        self.mainWindow.geometry('1024x768')
        self.mainWindow['padx'] = 9
        self.mainWindow['pady'] = 9

        self.label = tkinter.Label(self.mainWindow, text="Network Discovery Tool - Daniel Bader - NK-Tjänst AB")
        self.label.grid(row=0, column=0, columnspan=6)

        self.mainWindow.columnconfigure(0, weight=0)
        self.mainWindow.columnconfigure(1, weight=0)
        self.mainWindow.columnconfigure(2, weight=0)
        self.mainWindow.columnconfigure(3, weight=0)
        self.mainWindow.columnconfigure(4, weight=0)
        self.mainWindow.columnconfigure(5, weight=0)

        #  topScreen = tkinter.Label(mainWindow)
        #  topScreen.grid(row=0, column)

        self.mainWindow.rowconfigure(0, weight=0)
        self.mainWindow.rowconfigure(1, weight=0)
        self.mainWindow.rowconfigure(2, weight=0)
        self.mainWindow.rowconfigure(3, weight=0)
        self.mainWindow.rowconfigure(4, weight=0)
        self.mainWindow.rowconfigure(5, weight=0)
        self.mainWindow.rowconfigure(6, weight=5)

        # username label and entry-field
        self.user_name_label = tkinter.Label(self.mainWindow, text='Username')
        self.user_name_label.grid(row=1, column=0, sticky='e')
        self.user_name_entry = tkinter.Entry(self.mainWindow)
        self.user_name_entry.grid(row=1, column=1, sticky='w')

        # password label and entry-field
        self.password_label = tkinter.Label(self.mainWindow, text='Password')
        self.password_label.grid(row=2, column=0, sticky='e')
        self.password_entry = tkinter.Entry(self.mainWindow)
        self.password_entry.grid(row=2, column=1, sticky='w')

        # hostlist label and entry-field
        self.hosts_label = tkinter.Label(self.mainWindow, text='Hosts')
        self.hosts_label.grid(row=3, column=0, sticky='e')
        self.hosts_entry = tkinter.Entry(self.mainWindow)
        self.hosts_entry.grid(row=3, column=1, sticky='w')

        # skiplist label and entry-field
        self.skiplist_label = tkinter.Label(self.mainWindow, text='Ignored hosts')
        self.skiplist_label.grid(row=4, column=0, sticky='ne')
        self.skiplist_entry = tkinter.Entry(self.mainWindow)
        self.skiplist_entry.grid(row=4, column=1, sticky='nw')

        # mac address number label and drop-down-field

        # Set up variables to be used in drop-down
        self.man_number_var_type = tkinter.IntVar()
        self.man_number_var_type.set(0)

        self.mac_no_label = tkinter.Label(self.mainWindow, text='Max allowed Mac addresses')
        self.mac_no_label.grid(row=1, column=2, sticky='e')
        self.mac_no_entry = tkinter.OptionMenu(self.mainWindow, self.man_number_var_type, *(0, 1, 2, 3, 4, 5, 6, 7, 8, 9))
        self.mac_no_entry.grid(row=1, column=3, sticky='w')

        # mac address location label and entry-field
        self.mac_loc_label = tkinter.Label(self.mainWindow, text='Mac addresses to locate')
        self.mac_loc_label.grid(row=2, column=2, sticky='e')
        self.mac_loc_entry = tkinter.Entry(self.mainWindow)
        self.mac_loc_entry.grid(row=2, column=3, sticky='w')

        # config search label and entry-field
        self.config_search_label = tkinter.Label(self.mainWindow, text='Config-line to find')
        self.config_search_label.grid(row=1, column=4, sticky='e')
        self.config_search_entry = tkinter.Entry(self.mainWindow)
        self.config_search_entry.grid(row=1, column=5, sticky='w')

        # Search access or trunk radiobuttons and Label
        self.port_type_label = tkinter.Label(self.mainWindow, text='Search Access or Trunk ports?')
        self.port_type_label.grid(row=2, column=4, sticky='e')
        self.port_type_rb_frame = tkinter.LabelFrame(self.mainWindow, text='port-type')
        self.port_type_rb_frame.grid(row=2, column=5, sticky='w')

        self.port_type_rb_type = tkinter.IntVar()
        self.port_type_rb_type.set(2)

        self.radio1 = tkinter.Radiobutton(self.port_type_rb_frame, text='Access', value=1, variable=self.port_type_rb_type)
        self.radio2 = tkinter.Radiobutton(self.port_type_rb_frame, text='Trunk', value=2, variable=self.port_type_rb_type)

        self.radio1.grid(row=1, column=0, sticky='w')
        self.radio2.grid(row=1, column=1, sticky='e')

        # Search for present or missing string radiobuttons and Label
        self.port_command_label = tkinter.Label(self.mainWindow, text='Command Absent or Present?')
        self.port_command_label.grid(row=3, column=4, sticky='e')
        self.port_command_rb_frame = tkinter.LabelFrame(self.mainWindow, text='command-status')
        self.port_command_rb_frame.grid(row=3, column=5, sticky='w')

        self.port_command_rb_type = tkinter.IntVar()
        self.port_command_rb_type.set(2)

        self.radio1 = tkinter.Radiobutton(self.port_command_rb_frame, text='present', value=1, variable=self.port_command_rb_type)
        self.radio2 = tkinter.Radiobutton(self.port_command_rb_frame, text='absent', value=2, variable=self.port_command_rb_type)

        self.radio1.grid(row=1, column=0, sticky='w')
        self.radio2.grid(row=1, column=1, sticky='e')

        # buttonwindow
        self.button_window_label = tkinter.Label(self.mainWindow, text='Clear')
        self.button_window_label.grid(row=5, column=3)

        # Clear and Run buttons
        self.clear_button = tkinter.Button(self.button_window_label, text='Clear')
        self.clear_button.grid(row=0, column=0)
        self.run_button = tkinter.Button(self.button_window_label, text='Run!', command=self.run_main)
        self.run_button.grid(row=0, column=1)

        # main output label and entry-field
        self.main_output_label = tkinter.Label(self.mainWindow, text='', relief='ridge', border=2)
        self.main_output_label.grid(row=6, column=0, columnspan=6, sticky='nsew')

        self.mainWindow.mainloop()

    def run_main(self):
        #  checks to see that all necessary information is present
        #  if not: open popup that explains what is needed
        #  if yes, run main loop
        print('running!')
        return

    def generated_map(self):
        pass





