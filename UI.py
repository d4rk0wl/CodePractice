from tkinter import *
from tkinter import messagebox, filedialog


class MainInterface:
    def __init__(self, generate_function):
        self.generate = generate_function
        self.window = Tk()
        self.window.title("CW Phrase Generator")
        self.window.config(padx=20, pady=10, bg='#f0f0f0')
        self.window.iconbitmap("./icons/app.ico")

        self.callsign = StringVar(self.window, "")
        self.name = StringVar(self.window, "")
        self.mode = StringVar(self.window, "All")
        self.random = BooleanVar(self.window, False)
        self.save_location = StringVar(self.window, "- no location set -")
        self.comma_set = BooleanVar(self.window, False)
        self.status = StringVar(self.window, "Ready!")

        self.callsign_label = Label(self.window, text='Callsign', pady=10)
        self.callsign_entry = Entry(self.window, textvariable=self.callsign)

        self.name_label = Label(self.window, text='Name', pady=10)
        self.name_entry = Entry(self.window, textvariable=self.name)

        self.mode_label = Label(self.window, text='Mode', pady=10)
        self.mode_select = OptionMenu(self.window, self.mode, "All", "POTA/SOTA", "Ragchew")

        self.random_check = Checkbutton(self.window, text='Random Callsigns', variable=self.random,
                                        onvalue=True, offvalue=False, command=self.set_callsign_entry)

        self.comma_check = Checkbutton(self.window, text='Comma Separated', variable=self.comma_set,
                                       onvalue=True, offvalue=False)

        self.save_location_button = Button(self.window, text='Choose Save Location', command=self.choose_save_location)
        self.save_location_label = Label(self.window, textvariable=self.save_location, pady=10)

        self.submit = Button(self.window, text='Generate', command=self.validate_entries, pady=10)

        self.status_label = Label(self.window, textvariable=self.status, bg='#00ff00')

        self.callsign_label.grid(row=0, column=0)
        self.callsign_entry.grid(row=0, column=1)

        self.name_label.grid(row=1, column=0)
        self.name_entry.grid(row=1, column=1)

        self.mode_label.grid(row=2, column=0)
        self.mode_select.grid(row=2, column=1)

        self.random_check.grid(row=3, column=0, columnspan=2)
        self.comma_check.grid(row=4, column=0, columnspan=2)
        self.save_location_button.grid(row=6, column=0, columnspan=2)
        self.save_location_label.grid(row=7, column=0, columnspan=2)
        self.submit.grid(row=8, column=0, columnspan=2)
        self.status_label.grid(row=9, column=0, columnspan=2, pady=(10, 0))

        self.window.mainloop()

    def set_callsign_entry(self):
        if self.random.get():
            self.callsign_entry.config(state='disabled')
        else:
            self.callsign_entry.config(state='normal')

    def choose_save_location(self):
        self.save_location.set(filedialog.askdirectory())

    def validate_entries(self):
        def update_status():
            self.status.set('Complete!')
            self.status_label.config(bg="#00ff00")

        if self.callsign.get() == "" and not self.random.get():
            messagebox.showerror("Invalid Callsign", "Please enter your callsign or choose random callsigns")
            return
        if self.name.get() == "":
            messagebox.showerror("Invalid Name", "Please enter your name")
            return

        if self.save_location.get() == "- no location set -":
            messagebox.showerror("Invalid Save Location", "Please choose a location to export file")
            return

        params = {
            'callsign': self.callsign.get(),
            'name': self.name.get(),
            'random': self.random.get(),
            'separated': self.comma_set.get(),
            'save_location': self.save_location.get(),
            'mode': self.mode.get()
        }

        self.generate(params, update_status)
