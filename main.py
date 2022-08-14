from tkinter import *
import data
import pandas

root = Tk()
root.title('Bird Data Manager')
root.geometry('500x500')
root.configure(background='white', padx=50, pady=50)



# main title
bird_species = Label(text='Bird species')
bird_species.grid(row=0, column=0)
bird_species.config(padx=10, pady=10, background='white', font=('Ariel', 12))
bird_species_entry = Entry()
bird_species_entry.focus()
bird_species_entry.grid(row=0, column=1)

bird_num = Label(text='number')
bird_num.grid(row=1, column=0)
bird_num.config(pady=10, padx=10, background='white', font=('Ariel', 12))
bird_num_entry = Entry()
bird_num_entry.grid(row=1, column=1)
location_label = Label(text='Location')



def transfer():
    x = bird_species_entry.get()
    y = bird_num_entry.get()
    bird_species_entry.delete(0, END)
    bird_num_entry.delete(0, END)


Add_button = Button(text="Add input", command=transfer)
Add_button.grid(row=3, column=1)

location = StringVar()
location.set("Choose location")
location_drop = OptionMenu(root, location, *data.locations)
location_drop.grid(row=2, column=0)

observer = StringVar()
observer.set("Choose observer")
observer_drop = OptionMenu(root, observer, *data.observers)
observer_drop.grid(row=2, column=1)

configure = Button(text="Configure")
configure.grid(row=3, column=0)

root.mainloop()
