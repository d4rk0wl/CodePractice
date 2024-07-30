from tkinter import *


class MainInterface:
    def __init__(self, generate_function):
        self.generate = generate_function
        self.window = Tk()
        self.window.title("CW Phrase Generator")
        self.window.config(padx=20, pady=20, bg='#f0f0f0')
        self.callsign = StringVar(self.window, "")
        self.name = StringVar(self.window, "")
        self.random = BooleanVar(self.window, False)
        self.callsign_label = Label(self.window, text='Callsign', pady=10)
        self.callsign_entry = Entry(self.window, textvariable=self.callsign)
        self.name_label = Label(self.window, text='Name', pady=10)
        self.name_entry = Entry(self.window, textvariable=self.name)
        self.random_check = Checkbutton(self.window, text='Random Callsigns', variable=self.random, pady=10,
                                        onvalue=True, offvalue=False)
        self.submit = Button(self.window, text='Generate', command=lambda: self.generate(self.callsign.get(), self.name.get(), self.random.get()))

        self.callsign_label.grid(row=0, column=0)
        self.callsign_entry.grid(row=0, column=1)

        self.name_label.grid(row=1, column=0)
        self.name_entry.grid(row=1, column=1)

        self.random_check.grid(row=2, column=0, columnspan=2)

        self.submit.grid(row=3, column=0, columnspan=2)

        self.window.mainloop()
