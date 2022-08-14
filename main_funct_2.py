import main


# def open_new_window(root):
#     new_window = Toplevel(root)
#     new_window.title("Configure")
#     new_window.geometry("500x500")
#     colour_label = Label(new_window, text="App colour")
#     colour_label.grid(row=0, column=1)

def add_data():
    with open('data_collection', 'w') as file:
        bird_sp_data = main.bird_species_entry.get()
        num_data = main.bird_num_entry.get()
        file.write(bird_sp_data)
