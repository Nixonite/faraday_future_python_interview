from Tkinter import Tk, Label, OptionMenu, StringVar, Entry
import pandas as pd

class Application:

    def __init__(self, master):
        self.master = master
        self.master.title("City Information")
        self.master.geometry('350x200')

        self.data = pd.read_json('ca.json')
        self.tkvar = StringVar(master)
        self.choices = set(self.data.name)
        self.tkvar.set(self.data.name.values[0])
        self.dropdown = OptionMenu(master, self.tkvar, *self.choices, command=self.onSelectChange)
        self.dropdown.grid(column=1, row=0)

        self.cityLabel = Label(master, text="City")
        self.cityLabel.grid(column=0, row=0)

        self.countyLabel = Label(master, text="County")
        self.countyLabel.grid(column=0, row=1)

        self.countyEntry = Entry(master, width=25)
        self.countyEntry.configure(state='readonly')
        self.countyEntry.grid(column=1, row=1)

        self.latLabel = Label(master, text='Latitude')
        self.latLabel.grid(column=0, row=2)

        self.latEntry = Entry(master, width=25)
        self.latEntry.configure(state='readonly')
        self.latEntry.grid(column=1, row=2)

        self.longLabel = Label(master, text='Longitude')
        self.longLabel.grid(column=0, row=3)

        self.longEntry = Entry(master, width=25)
        self.longEntry.configure(state='readonly')
        self.longEntry.grid(column=1, row=3)

        self.onSelectChange()
    
    def onSelectChange():
        self.
    

if __name__=="__main__":
    root = Tk()
    gui = Application(root)
    root.mainloop()