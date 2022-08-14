from tkinter import *
from tkinter import messagebox
from data import *
import random

root = Tk()
root.title('Bird Data Manager')
root.geometry('500x500')
root.configure(background='white', padx=20, pady=20, cursor="arrow", bg="white")


class NewWindow(Toplevel):

    def __init__(self, master=None):
        super().__init__(master=root)
        self.title("Configure")
        self.geometry("500x500")
        color = Label(self, text="Color settings", padx=10, pady=10)
        color.grid(row=0, column=1)

        def dark_mode():
            bird_species.config(bg="black", fg="white")
            bird_num.config(bg="black", fg="white")
            location_drop.config(bg="black", fg="white")
            observer_drop.config(bg="black", fg="white")
            configure_button.config(bg="black", fg="white")
            Add_button.config(bg="black", fg="white")
            root.config(bg="black")

        def light_mode():
            bird_species.config(bg="white", fg="black")
            bird_num.config(bg="white", fg="black")
            location_drop.config(bg="white", fg="black")
            observer_drop.config(bg="white", fg="black")
            configure_button.config(bg="white", fg="black")
            Add_button.config(bg="white", fg="black")

        def lsd_mode():
            bird_species.config(bg=random.choice(colors), fg=random.choice(colors))
            bird_num.config(bg=random.choice(colors), fg=random.choice(colors))
            location_drop.config(bg=random.choice(colors), fg=random.choice(colors))
            observer_drop.config(bg=random.choice(colors), fg=random.choice(colors))
            configure_button.config(bg=random.choice(colors), fg=random.choice(colors))
            Add_button.config(bg=random.choice(colors), fg=random.choice(colors))

        dark_mode = Button(self, text="Dark mode", command=dark_mode)
        dark_mode.grid(row=1, column=0)
        light_mode = Button(self, text="Light mode", command=light_mode)
        light_mode.grid(row=1, column=1)
        lsd_mode = Button(self, text="LSD mode", command=lsd_mode)
        lsd_mode.grid(row=1, column=2)

        def add_user():
            pass

        user_label = Label(self, text="User configuration", pady=10, padx=10)
        user_label.grid(row=2, column=1)
        user_config = Button(self, text="Add/Delete user(s)", command=user_configuration)
        user_config.grid(row=3, column=0)
        # transfer classes into ind. modules so they can be imported into main.py
        # make an add/delete/info window in which user/s can be added or deleted; check info for users


bird_species = Label(text='bird species')
bird_species.place(rely=0.05, relx=0.35, anchor=CENTER)
bird_species.config(padx=10, pady=10, background='white', font=('Ariel', 12))
bird_species_entry = Entry()
bird_species_entry.focus()
bird_species_entry.place(rely=0.05, relx=0.65, anchor=CENTER)
bird_num = Label(text='number')
bird_num.place(rely=0.1, relx=0.28)
bird_num.config(pady=10, padx=10, background='white', font=('Ariel', 12))
bird_num_entry = Entry()
bird_num_entry.place(rely=0.15, relx=0.65, anchor=CENTER)
location_label = Label(text='Location')


def add_data():
    bird_sp_data = bird_species_entry.get()
    num_data = bird_num_entry.get()
    observer_data = observer.get()
    location_data = location.get()
    L = [f'{bird_sp_data}, {num_data}, {observer_data}, {location_data}\n']
    if len(bird_sp_data) > 0:
        with open("data_collection.txt", "a") as file:  # make to write into .csv
            file.writelines(L)
        bird_species_entry.delete(0, END)
        bird_num_entry.delete(0, END)
        observer.set("Choose observer")
        location.set("Choose location")
    else:
        messagebox.showerror(title="Error!!!", message="Not a valid input!\nPlease try again\n")


Add_button = Button(text="Add input", command=add_data)
Add_button.place(relx=0.35, rely=0.45, anchor=CENTER)

location = StringVar()
location.set("Choose location")
location_drop = OptionMenu(root, location, *locations)
location_drop.place(relx=0.35, rely=0.25, anchor=CENTER)

observer = StringVar()
observer.set("Choose observer")
observer_drop = OptionMenu(root, observer, *observers)
observer_drop.place(rely=0.35, relx=0.35, anchor=CENTER)

configure_button = Button(root, text="Configure")
configure_button.bind("<Button>", lambda e: NewWindow(root))
configure_button.place(rely=0.45, relx=0.65, anchor=CENTER)

root.mainloop()
