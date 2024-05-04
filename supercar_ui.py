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
        image = Image.open("Images/startup_image.jpg")
        image = image.resize((850, 500), Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)

        picture_label = tk.Label(picture_frame, image=photo)
        picture_label.image = photo
        picture_label.pack(pady=10)

        configurations = {'pady': 10}
        startup_label = tk.Label(self.main_frame, text="Supercar choosing helper and analysis", font=("Helvetica", 12))
        startup_label.pack(**configurations)

        startup_button = tk.Button(self.main_frame, text="Start", width=10, height=2, command=self.show_main_window)
        startup_button.pack(side="top", padx=20, pady=10)

        quit_button = tk.Button(self.main_frame, text="Quit", width=10, height=2, command=self.quit_program)
        quit_button.pack(side="top", padx=20, pady=10)

    def show_main_window(self):
        self.main_frame.destroy()
        self.main_frame = tk.Frame(self)
        self.main_frame.pack(fill="both", expand=True)

        # Configurations
        configurations = {'padx': 10}

        # Search Box
        search_box_label = tk.Label(self.main_frame, text="Search Box")
        search_box_label.grid(row=0, column=0, sticky="w", **configurations)
        self.search_box = tk.Entry(self.main_frame, width=45, textvariable=self.search)
        self.search_box.grid(row=1, column=0, **configurations)
        self.search_box.bind("<KeyRelease>", self.on_search_key_release)

        # Result list box
        result_label = tk.Label(self.main_frame, text="Results")
        result_label.grid(row=2, column=0, sticky="w", **configurations)
        self.result_box = tk.Listbox(self.main_frame, font=('Arial', 12), width=30, height=18)
        self.result_box.bind("<<ListboxSelect>>", self.controller.on_car_select)
        self.result_box.grid(row=3, column=0, **configurations)

        # Show spec button
        self.show_spec_button = tk.Button(self.main_frame, text="Show specs", command=self.controller.show_car_specs)
        self.show_spec_button.grid(row=4, column=0, sticky="w", padx=30, pady=20)
        self.show_spec_button['state'] = tk.DISABLED

        # Add to compare list button
        self.add_com_button = tk.Button(self.main_frame, text="Add to compare list")
        self.add_com_button.grid(row=4, column=0, padx=(80,0), pady=20)
        self.add_com_button['state'] = tk.DISABLED

        # Welcome Label
        main_label = tk.Label(self.main_frame, text="Supercar choosing helper and analysis", font=("Helvetica", 16))
        main_label.grid(row=0, column=1)


        # Back to Main Menu Button
        main_button = tk.Button(self.main_frame, text="Back to Main Menu", command=self.show_startup_window)

        # Analysis button
        analysis_buttons = {
            "Descriptive Statistic": self.show_statistic_window,
            "Distribution": self.show_distribution_window,
            "Correlation": self.show_correlation_window,
            "Part-to-Whole": self.show_part_to_whole_window,
            "Time-Series": self.show_time_series__window
        }
        row_index = 0
        for button_text, button_command in analysis_buttons.items():
            button = tk.Button(self.main_frame, text=button_text, command=button_command)
            button.grid(row=row_index, column=3, sticky='e', **configurations)
            row_index += 1

        # Decoration pictures

        # picture_frame = tk.Frame(self.main_frame, width=200)
        # picture_frame.grid(row=1, column=2, padx=10, pady=10)
        # image = Image.open("Images/descriptive statistic.png")
        # # image = image.resize((850, 500), Image.LANCZOS)
        # photo = ImageTk.PhotoImage(image)
        #
        # picture_label = tk.Label(picture_frame, image=photo)
        # picture_label.image = photo
        # picture_label.pack(pady=10)

    def on_search_key_release(self, event):
        self.controller.show_search_result()

    def quit_program(self):
        self.destroy()

    def run(self):
        self.mainloop()

    def show_statistic_window(self):
        pass
    def show_distribution_window(self):
        # Clear previous content
        for widget in self.main_frame.winfo_children():
            widget.destroy()


        # Configurations
        configurations = {'padx': 10, 'pady': 10}

        # Add combobox to select attribute
        ttk.Label(self.main_frame, text="Select Attribute:").grid(row=0, column=0, **configurations)
        attribute_combo = ttk.Combobox(self.main_frame, values=['Year', 'Engine Size (L)', 'Horsepower', 'Torque (lb-ft)', '0-60 MPH Time (seconds)', 'Price (in USD)'])
        attribute_combo.grid(row=0, column=1, **configurations)

        # Add button to generate distribution graph
        ttk.Button(self.main_frame, text="Generate", command=lambda: self.controller.generate_distribution(attribute_combo.get())).grid(row=1, column=0, columnspan=2, **configurations)
        ttk.Button(self.main_frame, text="Back", command=self.show_main_window).grid(row=2, column=0, columnspan=2, **configurations)

    def show_correlation_window(self):
        pass

    def show_part_to_whole_window(self):
        pass

    def show_time_series__window(self):
        pass