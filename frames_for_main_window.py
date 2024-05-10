"""All frames for showing main window"""
import tkinter as tk
from tkinter import messagebox, ttk
from PIL import ImageTk, Image



class SearchResultsFrame(tk.Frame):
    """ A frame for displaying search results and search tools in the main window."""
    def __init__(self, parent, controller, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.search = tk.StringVar()
        self.min = tk.StringVar()
        self.max = tk.StringVar()
        self.selected_attribute = tk.StringVar()
        self.controller = controller
        self.init_components()

    def init_components(self) -> None:
        """Initialize all the UI components of the frame."""
        # Configure row and column weights for expansion
        for row in range(8):
            self.grid_rowconfigure(row, weight=1)
        for col in range(2):
            self.grid_columnconfigure(col, weight=1)

        # Attribute label and selector
        attribute_label = tk.Label(self, text="Attribute:")
        attribute_label.grid(row=3, column=0, sticky="w", padx=10, pady=5)
        self.attribute_selector = tk.OptionMenu(self, self.selected_attribute,
                                                '', 'Year', 'Engine Size (L)',
                                                'Horsepower', 'Torque (lb-ft)',
                                                '0-60 MPH Time (seconds)',
                                                'Price (in USD)',
                                                command=self.on_attribute_change)
        self.attribute_selector.grid(row=3, column=0, sticky="ew", padx=100,
                                     pady=5)

        # Search label
        search_label = tk.Label(self, text="Search Box (Search from car name)")
        search_label.grid(row=0, column=0, sticky="w", padx=10, pady=5)

        # Search box
        self.search_box = tk.Entry(self, width=45, textvariable=self.search)
        self.search_box.grid(row=1, column=0, sticky='nsew', padx=10, pady=5)
        self.search_box.bind("<KeyRelease>", self.on_search_key_release)

        # Min price label and entry
        min_price_label = tk.Label(self, text="Min:")
        min_price_label.grid(row=5, column=0, sticky="w", padx=10, pady=5)
        self.min_entry = tk.Entry(self, textvariable=self.min)
        self.min_entry.grid(row=5, column=0, sticky='nsew', padx=100, pady=5)
        self.min_entry.bind("<KeyRelease>", self.on_search_key_release)

        # Max price label and entry
        max_price_label = tk.Label(self, text="Max:")
        max_price_label.grid(row=4, column=0, sticky="w", padx=10, pady=5)
        self.max_entry = tk.Entry(self, textvariable=self.max)
        self.max_entry.grid(row=4, column=0, sticky='nsew', padx=100, pady=5)
        self.max_entry.bind("<KeyRelease>", self.on_search_key_release)

        # Tool label
        tool_label = tk.Label(self, text="Search Tool")
        tool_label.grid(row=2, column=0, sticky="w", padx=10, pady=5)

        # Result label
        self.result_label = tk.Label(self, text="Results: (0 results)")
        self.result_label.grid(row=6, column=0, sticky="nw", padx=10, pady=5)

        # Result box
        self.result_box = tk.Listbox(self, font=('Arial', 12), width=40,
                                     height=12)
        self.result_box.bind("<<ListboxSelect>>",
                             self.controller.on_car_select)
        self.result_box.grid(row=7, column=0, sticky='nsew', padx=10, pady=5)

        # Scrollbar for the result box
        scrollbar = tk.Scrollbar(self, orient="vertical",
                                 command=self.result_box.yview)
        scrollbar.grid(row=7, column=1, sticky='ns', pady=5)
        self.result_box.config(yscrollcommand=scrollbar.set)

        # Show spec button
        self.show_spec_button = tk.Button(self, text="Show specs",
                                          command=self.controller.show_car_specs)
        self.show_spec_button.grid(row=8, column=0, sticky="w", padx=70,
                                   pady=5)
        self.show_spec_button['state'] = tk.DISABLED

        # Add to compare list button
        self.add_com_button = tk.Button(self, text="Add to compare list",
                                        command=self.controller.add_to_compare_list)
        self.add_com_button.grid(row=8, column=0, padx=(95, 0), pady=5)
        self.add_com_button['state'] = tk.DISABLED

    def on_search_key_release(self, event):
        """Callback function triggered when a key is released in the
        search box or price entry fields."""
        min_val = self.min.get()
        max_val = self.max.get()
        error_message = ""
        try:
            if min_val and float(min_val) < 0:
                error_message = "Min value must be a positive number."
            elif max_val and float(max_val) < 0:
                error_message = "Max value must be a positive number."
            elif min_val and max_val and float(min_val) > float(max_val):
                error_message = "Min value cannot be greater than Max value."
        except ValueError:
            error_message = "Invalid input. Please enter a valid number."

        if error_message:
            messagebox.showerror("Error", error_message)
            self.min.set('')
            self.max.set('')
        else:
            self.controller.show_search_result()

    def on_attribute_change(self, event):
        """Callback function triggered when the selected attribute changes."""
        self.min.set('')
        self.max.set('')
        self.controller.show_search_result()


class ComparisonFrame(tk.Frame):
    """Frame for comparing selected cars and displaying comparison results."""
    def __init__(self, parent, ui, controller, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.ui = ui
        self.controller = controller
        self.init_components()

    def init_components(self) -> None:
        """Initialize all the UI components of the frame."""
        # Logo
        picture_frame = tk.Frame(self, width=200)
        picture_frame.pack(side=tk.TOP)
        image = Image.open("Images/logo.png")
        image = image.resize((133, 130), Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)

        picture_label = tk.Label(picture_frame, image=photo)
        picture_label.image = photo
        picture_label.pack(side=tk.TOP)

        # Welcome Label
        main_label = tk.Label(self,
                              text="Supercar choosing helper and analysis",
                              font=("Helvetica", 16))
        main_label.pack(side=tk.TOP)

        # Comparison box
        compare_lable = tk.Label(self, text="Comparison box",
                                 font=("Helvetica", 12))
        compare_lable.pack(side=tk.TOP, anchor="w")
        self.compare_box = tk.Listbox(self, font=('Arial', 12), width=40,
                                      height=2)
        self.compare_box.pack(side=tk.TOP, anchor='w', fill=tk.BOTH,
                              expand=True)

        # Button for interact with comparison box
        interact_buttons = InteractButton(self, self.controller)
        interact_buttons.pack(side=tk.TOP, fill='y', expand=True)

        # Compare results
        compare_result = tk.Label(self, text="Comparison result:",
                                  font=("Helvetica", 12))
        compare_result.pack(side=tk.TOP, anchor="w")
        self.result_box = CompareResultFrame(self, self.controller)
        self.result_box.pack(side=tk.TOP, anchor='w', fill=tk.BOTH,
                             expand=True)

        # Back to Main Menu Button
        back_button = tk.Button(self, text="Back to Main Menu", width=20,
                                command=self.ui.show_startup_window)
        back_button.pack(side=tk.BOTTOM, pady=10, fill='y', expand=True)

    def add_to_compare(self, car):
        """Add a car to the comparison list."""
        self.compare_box.insert(tk.END, car)


class InteractButton(tk.Frame):
    """Frame for interaction buttons within the comparison frame."""
    def __init__(self, parent, controller, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.controller = controller
        self.init_components()

    def init_components(self) -> None:
        """Initialize all the UI components of the frame."""
        configurations = {'side': tk.LEFT, 'padx': 5, 'pady': 10,
                          'fill': tk.BOTH, 'expand': True}

        # Button for interact with comparison box
        compare_button = tk.Button(self, text="Compare", width=10,
                                   command=self.controller.generate_comparison)
        compare_button.pack(**configurations)

        clear_button = tk.Button(self, text="Clear", width=10,
                                 command=self.controller.clear_comparison)
        clear_button.pack(**configurations)

        remove_button = tk.Button(self, text="Remove", width=10,
                                  command=self.controller.remove_selected)
        remove_button.pack(**configurations)


class StatisticFrame(tk.Frame):
    """Frame for displaying statistical analysis options."""
    def __init__(self, parent, controller, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.controller = controller
        self.init_components()

    def init_components(self) -> None:
        """Initialize all the UI components of the frame."""
        upper_frame = UpperPart(self, self.controller)
        upper_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        picture_frame = tk.Frame(self, width=200)
        picture_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        image = Image.open('Images/timeseries.png')
        image = image.resize((116, 100), Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)

        picture_label = tk.Label(picture_frame, image=photo)
        picture_label.image = photo
        picture_label.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        button = tk.Button(self, text='Time series', width=12,
                           command=self.controller.show_time_series)
        button.pack(side=tk.TOP, anchor='n', padx=10, pady=10, fill='y',
                    expand=True)


class UpperPart(tk.Frame):
    """Frame for displaying statistical analysis options."""

    def __init__(self, parent, controller, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.controller = controller
        self.init_components()

    def init_components(self):
        """Initialize all the UI components of the frame."""
        # Configure row and column weights for expansion
        for row in range(4):
            self.grid_rowconfigure(row, weight=1)
        for col in range(2):
            self.grid_columnconfigure(col, weight=1)

        configurations = {'padx': 5, 'pady': 5}
        pictures = [{'File Name': 'Images/descriptive statistic.png', 'row': 0,
                     'column': 0},
                    {'File Name': 'Images/distribution.png', 'row': 0,
                     'column': 1},
                    {'File Name': 'Images/correlation.png', 'row': 2,
                     'column': 0},
                    {'File Name': 'Images/parttowhole.png', 'row': 2,
                     'column': 1}]
        for picture in pictures:
            picture_frame = tk.Frame(self, width=200)
            picture_frame.grid(row=picture['row'], column=picture['column'],
                               sticky="nsew")
            image = Image.open(picture['File Name'])
            image = image.resize((120, 120), Image.LANCZOS)
            photo = ImageTk.PhotoImage(image)

            picture_label = tk.Label(picture_frame, image=photo)
            picture_label.image = photo
            picture_label.pack(side=tk.TOP)

        buttons = [{'Name': 'Descriptive statistic', 'row': 1, 'column': 0,
                    'command': self.controller.show_descriptive},
                   {'Name': 'Distribution', 'row': 1, 'column': 1,
                    'command': self.controller.show_distribution},
                   {'Name': 'Correlation', 'row': 3, 'column': 0,
                    'command': self.controller.show_correlation},
                   {'Name': 'Part-to-whole', 'row': 3, 'column': 1,
                    'command': self.controller.show_part_to_whole}]
        for button_info in buttons:
            button = tk.Button(self, text=button_info['Name'],
                               command=button_info['command'])
            button.grid(row=button_info['row'], column=button_info['column'],
                        **configurations, sticky="nsew")


class CompareResultFrame(tk.Frame):
    """Frame for displaying comparison results."""
    def __init__(self, parent, data, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.data = data
        self.init_components()

    def init_components(self):
        """Initialize all the UI components of the frame."""
        # Configurations
        configurations = {'padx': 10, 'pady': 3, 'anchor': 'w'}
        self.config(borderwidth=4, relief="groove", width=600, height=350)
        self.year_label = ttk.Label(self, text='', font=("TkDefaultFont", 10))
        self.engine_label = ttk.Label(self, text='',
                                      font=("TkDefaultFont", 10))
        self.horse_label = ttk.Label(self, text='', font=("TkDefaultFont", 10))
        self.torque_label = ttk.Label(self, text='',
                                      font=("TkDefaultFont", 10))
        self.time_label = ttk.Label(self, text='', font=("TkDefaultFont", 10))
        self.price_label = ttk.Label(self, text='', font=("TkDefaultFont", 10))

        # Pack labels
        self.year_label.pack(side=tk.TOP, **configurations)
        self.engine_label.pack(side=tk.TOP, **configurations)
        self.horse_label.pack(side=tk.TOP, **configurations)
        self.torque_label.pack(side=tk.TOP, **configurations)
        self.time_label.pack(side=tk.TOP, **configurations)
        self.price_label.pack(side=tk.TOP, **configurations)
