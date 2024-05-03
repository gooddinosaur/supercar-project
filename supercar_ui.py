import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image


class SupercarUI(tk.Tk):
    def __init__(self, controller):
        super().__init__()
        self.title("Supercar choosing helper and analysis")
        self.search = tk.StringVar()
        self.controller = controller
        self.init_main_window()

    def init_main_window(self):
        self.main_frame = tk.Frame(self)
        self.main_frame.pack(fill="both", expand=True)
        self.minsize(1200, 500)
        self.show_startup_window()

    def show_startup_window(self):
        self.main_frame.destroy()
        self.main_frame = tk.Frame(self)
        self.main_frame.pack(fill="both", expand=True)

        # New frame for showing pictures
        picture_frame = tk.Frame(self.main_frame, width=200)
        picture_frame.pack(side="left", fill="y")

        # Import and display picture
        image = Image.open("startup_image.jpg")
        image = image.resize((850, 500), Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)

        picture_label = tk.Label(picture_frame, image=photo)
        picture_label.image = photo
        picture_label.pack(pady=10)

        configurations = {'pady': 10}
        startup_label = tk.Label(self.main_frame, text="Supercar choosing helper and analysis", font=("Helvetica", 12))
        startup_label.pack(**configurations)

        startup_button = tk.Button(self.main_frame, text="Start", width=10, height=2, command=self.show_main_window)
        startup_button.pack(**configurations)

        quit_button = tk.Button(self.main_frame, text="Quit", width=10, height=2, command=self.quit_program)
        quit_button.pack(**configurations)

    def show_main_window(self):
        self.main_frame.destroy()
        self.main_frame = tk.Frame(self)
        self.main_frame.pack(fill="both", expand=True)

        # Configurations

        # Search Box
        search_box_label = tk.Label(self.main_frame, text="Search Box")
        search_box_label.grid(row=0, column=0)
        self.search_box = tk.Entry(self.main_frame, width=25, textvariable=self.search)
        self.search_box.grid(row=1, column=0)
        search_button = tk.Button(self.main_frame, text="Search", command=self.controller.show_search_result)
        search_button.grid(row=1, column=1)

        # Result list box
        result_label = tk.Label(self.main_frame, text="Results")
        result_label.grid(row=2, column=0)
        self.result_box = tk.Listbox(self.main_frame, font=('Arial', 12), width=30)
        self.result_box.bind("<<ListboxSelect>>", self.controller.on_car_select)
        self.result_box.grid(row=3, column=0)

        # Show spec button
        self.show_spec_button = tk.Button(self.main_frame, text="Show specs", command=self.controller.show_car_specs)
        self.show_spec_button.grid(row=4, column=0)
        self.show_spec_button['state'] = tk.DISABLED

        # Add to compare list button
        self.add_com_button = tk.Button(self.main_frame, text="Add to compare list")
        self.add_com_button.grid(row=4, column=1)
        self.add_com_button['state'] = tk.DISABLED

        # Welcome Label
        main_label = tk.Label(self.main_frame, text="Welcome to the Main Window")


        # Back to Main Menu Button
        main_button = tk.Button(self.main_frame, text="Back to Main Menu",
                                command=self.show_startup_window)

    def quit_program(self):
        self.destroy()

    def run(self):
        self.mainloop()
