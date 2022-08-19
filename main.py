from tkinter import *
from tkinter import messagebox
import work_data
from work_data import *
import pandas
import random

root = Tk()
root.title('Bird Data Manager')
root.geometry('500x500')
root.configure(background='white', padx=20, pady=20, cursor="arrow", bg="white")

file = pandas.read_csv('stored_data_birds.csv')
bird_names = pandas.read_csv('Popis ptica Hrvatske_BIOM.csv')
observers_list = pandas.read_csv("Book1.csv")
observers_list_2 = observers_list.columns.to_list()
OPTIONS = observers_list_2


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
            ring_num.config(bg="black", fg="white")
            current_session_input.config(bg="black", fg="white")
            all_time_label.config(bg="black", fg="white")
            root.config(bg="black")

        def light_mode():
            bird_species.config(bg="white", fg="black")
            bird_num.config(bg="white", fg="black")
            location_drop.config(bg="white", fg="black")
            observer_drop.config(bg="white", fg="black")
            configure_button.config(bg="white", fg="black")
            Add_button.config(bg="white", fg="black")
            ring_num.config(bg="white", fg="black")
            current_session_input.config(bg="white", fg="black")
            all_time_label.config(bg="white", fg="black")
            root.config(bg="white")

        def lsd_mode():
            bird_species.config(bg=random.choice(colors), fg=random.choice(colors))
            bird_num.config(bg=random.choice(colors), fg=random.choice(colors))
            location_drop.config(bg=random.choice(colors), fg=random.choice(colors))
            observer_drop.config(bg=random.choice(colors), fg=random.choice(colors))
            configure_button.config(bg=random.choice(colors), fg=random.choice(colors))
            Add_button.config(bg=random.choice(colors), fg=random.choice(colors))
            ring_num.config(bg=random.choice(colors), fg=random.choice(colors))
            current_session_input.config(bg=random.choice(colors), fg=random.choice(colors))
            all_time_label.config(bg=random.choice(colors), fg=random.choice(colors))
            root.config(bg=random.choice(colors))

        class AddUser(Toplevel):

            def __init__(self, master=None):
                super().__init__(master=root)
                self.title("Add/delete user(s)")
                self.geometry("250x250")
                add_user_1 = Label(self, text="Add user", padx=10, pady=10)
                add_user_1.grid(row=0, column=0)
                add_user_1_entry = Entry(self)
                add_user_1_entry.grid(row=0, column=1)

                def add_user_function():
                    added = add_user_1_entry.get()
                    messagebox.askyesno(title="Add user warning", message=f"Do you want add {added}")
                    added_df = pandas.DataFrame({
                        "observer": [added]
                    })
                    added_df.to_csv('Book1.csv', mode='a', index=False, header=False)
                    add_user_1_entry.delete(0, END)

                def delete_user_function():
                    deleted = delete_user_1_entry.get()
                    for index, row in observers_list.iterrows():
                        if deleted == row['observer']:
                            observers_list.drop(observers_list.index[observers_list['observer'] == deleted], inplace=True)
                            delete_user_1_entry.delete(0, END)

                add_user_1_bttn = Button(self, text="Add", command=add_user_function)
                add_user_1_bttn.grid(row=0, column=2)
                delete_user_1 = Label(self, text="Delete user", padx=10, pady=10)
                delete_user_1.grid(row=1, column=0)
                delete_user_1_entry = Entry(self)
                delete_user_1_entry.grid(row=1, column=1)
                delete_user_1_bttn = Button(self, text="Delete", command=delete_user_function)
                delete_user_1_bttn.grid(row=1, column=2)

        dark_mode = Button(self, text="Dark mode", command=dark_mode)
        dark_mode.grid(row=1, column=0)
        light_mode = Button(self, text="Light mode", command=light_mode)
        light_mode.grid(row=1, column=1)
        lsd_mode = Button(self, text="LSD mode", command=lsd_mode)
        lsd_mode.grid(row=1, column=2)

        user_label = Label(self, text="User configuration", pady=10, padx=10)
        user_label.grid(row=2, column=1)
        user_config = Button(self, text="Add user(s)", command=AddUser)
        user_config.grid(row=3, column=1)


bird_species = Label(text='bird species:')
bird_species.place(rely=0.05, relx=0.35, anchor=CENTER)
bird_species.config(padx=10, pady=10, background='white', font=('Ariel', 12))
bird_species_entry = Entry()
bird_species_entry.focus()
bird_species_entry.place(rely=0.05, relx=0.65, anchor=CENTER)
bird_num = Label(text='number of birds:')
bird_num.place(rely=0.1, relx=0.18)
bird_num.config(pady=10, padx=10, background='white', font=('Ariel', 12))
bird_num_entry = Entry()
bird_num_entry.place(rely=0.15, relx=0.65, anchor=CENTER)

ring_num = Label(text="Ring number:")
ring_num.config(padx=10, pady=10, bg="white", font=("Ariel", 12))
ring_num.place(relx=0.35, rely=0.25, anchor=CENTER)
ring_num_entry = Entry()
ring_num_entry.place(rely=0.25, relx=0.65, anchor=CENTER)

current_session_input = Label(text="Current input:")
current_session_input.config(padx=10, pady=10, bg="white")
current_session_input.place(relx=0.7, rely=0.45, anchor=CENTER)
current_session_num = Label(text=work_data.c_sInp, bg="white")
current_session_num.place(relx=0.8, rely=0.43)

all_time_label = Label(text="All input:")
all_time_label.config(padx=10, pady=10, bg="white")
all_time_label.place(relx=0.7, rely=0.55, anchor=CENTER)

with open("score.txt", "r") as testr:
    score = int(testr.read())
all_time_num = Label(text=score, bg="white")
all_time_num.place(relx=0.8, rely=0.55, anchor=CENTER)


def add_data():
    sci_bird = bird_species_entry.get()
    eng_real = ""
    for index, row in bird_names.iterrows():
        if sci_bird == row["Znanstveno ime"]:
            eng_real = row["Englesko ime"]
    num_data = bird_num_entry.get()
    observer_data = observer.get()
    location_data = location.get()
    ring_data = ''
    for value in file['ring_num']:
        while value == ring_num_entry.get():
            ring_num_entry.delete(0, END)
            messagebox.showerror(title="Error", message="entered ring number already exists in library\nPlease check "
                                                        "ring number\n")
        else:
            ring_data = ring_num_entry.get()

    if len(sci_bird) > 0 and len(ring_data) > 5:
        df = pandas.DataFrame({'sci_species': [sci_bird],
                               'eng_species': [eng_real],
                               'num_of_birds': [num_data],
                               'ring_num': [ring_data],
                               'Location': [location_data],
                               'observer': [observer_data]
                               })
        df.to_csv('stored_data_birds.csv', mode='a', index=False, header=False)
        work_data.c_sInp += 1
        current_session_num.config(text=str(work_data.c_sInp))
        bird_species_entry.delete(0, END)
        bird_num_entry.delete(0, END)
        ring_num_entry.delete(0, END)
        observer.set("Choose observer")
        location.set("Choose location")
        with open("score.txt", "r+") as hisc:
            highest = int(hisc.read())
            all_time_num.config(text=highest)
            if work_data.c_sInp > 0:
                all_time_num.config(text=1 + highest)
                hisc.seek(0)
                hisc.write(str(1 + highest))
    else:
        messagebox.showerror(title="Error!!!", message="Not a valid input!\nPlease try again\n")


Add_button = Button(text="Add input", command=add_data)
Add_button.place(relx=0.35, rely=0.65, anchor=CENTER)

location = StringVar()
location.set("Choose location")
location_drop = OptionMenu(root, location, *locations)
location_drop.place(relx=0.35, rely=0.45, anchor=CENTER)

observer = StringVar(root)
observer.set(OPTIONS[0])
observer_drop = OptionMenu(root, observer, *observers_list['observer'])
observer_drop.place(rely=0.55, relx=0.35, anchor=CENTER)

configure_button = Button(root, text="Configure")
configure_button.bind("<Button>", lambda e: NewWindow(root).focus())
configure_button.place(rely=0.65, relx=0.65, anchor=CENTER)


root.mainloop()
