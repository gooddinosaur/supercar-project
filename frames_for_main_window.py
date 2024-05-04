import tkinter as tk
from PIL import ImageTk, Image


class SearchResultsFrame(tk.Frame):
    def __init__(self, parent, controller, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.search = tk.StringVar()
        self.controller = controller
        self.init_components()

    def init_components(self) -> None:
        # Search label
        search_label = tk.Label(self, text="Search Box")
        search_label.grid(row=0, column=0, sticky="w", padx=10, pady=5)

        # Search box
        self.search_box = tk.Entry(self, width=45, textvariable=self.search)
        self.search_box.grid(row=1, column=0, padx=10, pady=5)
        self.search_box.bind("<KeyRelease>", self.on_search_key_release)

        # Result label
        result_label = tk.Label(self, text="Results")
        result_label.grid(row=2, column=0, sticky="w", padx=10, pady=5)

        # Result box
        self.result_box = tk.Listbox(self, font=('Arial', 12), width=30,
                                     height=18)
        self.result_box.bind("<<ListboxSelect>>",
                             self.controller.on_car_select)
        self.result_box.grid(row=3, column=0, padx=10, pady=5)

        # Show spec button
        self.show_spec_button = tk.Button(self, text="Show specs",
                                          command=self.controller.show_car_specs)
        self.show_spec_button.grid(row=4, column=0, sticky="w", padx=35,
                                   pady=5)
        self.show_spec_button['state'] = tk.DISABLED

        # Add to compare list button
        self.add_com_button = tk.Button(self, text="Add to compare list")
        self.add_com_button.grid(row=4, column=0, padx=(80, 0), pady=5)
        self.add_com_button['state'] = tk.DISABLED

    def on_search_key_release(self, event):
        self.controller.show_search_result()


class ComparisonFrame(tk.Frame):
    def __init__(self, parent, ui, controller, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.ui = ui
        self.controller = controller
        self.init_components()

    def init_components(self) -> None:
        # Logo
        picture_frame = tk.Frame(self, width=200)
        picture_frame.pack(side=tk.TOP)
        image = Image.open("Images/logo.png")
        image = image.resize((133, 120), Image.LANCZOS)
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
        compare_box = tk.Listbox(self, font=('Arial', 12), width=40, height=10)
        compare_box.pack(side=tk.TOP)

        # Button for interact with comparison box
        interact_buttons = InteractButton(self, self.controller)
        interact_buttons.pack(side=tk.TOP)

        # Back to Main Menu Button
        back_button = tk.Button(self, text="Back to Main Menu",
                                command=self.ui.show_startup_window)
        back_button.pack(side=tk.BOTTOM, pady=(10, 0))


class InteractButton(tk.Frame):
    def __init__(self, parent, controller, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.controller = controller
        self.init_components()

    def init_components(self) -> None:
        configurations = {'side': tk.LEFT, 'padx': 5, 'pady': 10}

        # Button for interact with comparison box
        compare_button = tk.Button(self, text="Compare")
        compare_button.pack(**configurations)

        clear_button = tk.Button(self, text="Clear")
        clear_button.pack(**configurations)

        remove_button = tk.Button(self, text="Remove")
        remove_button.pack(**configurations)


class StatisticFrame(tk.Frame):
    def __init__(self, parent, controller, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.controller = controller
        self.init_components()

    def init_components(self) -> None:
        upper_frame = UpperPart(self, self.controller)
        upper_frame.pack(side=tk.TOP)

        picture_frame = tk.Frame(self, width=200)
        picture_frame.pack(side=tk.TOP)
        image = Image.open('Images/timeseries.png')
        image = image.resize((116, 100), Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)

        picture_label = tk.Label(picture_frame, image=photo)
        picture_label.image = photo
        picture_label.pack(side=tk.TOP)
        button = tk.Button(self, text='Time series')
        button.pack(side=tk.TOP, padx=10, pady=10)


class UpperPart(tk.Frame):

    def __init__(self, parent, controller, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.controller = controller
        self.init_components()

    def init_components(self):
        configurations = {'padx': 10, 'pady': 10}
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
            picture_frame.grid(row=picture['row'], column=picture['column'])
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
                    'command': ''}]
        for button_info in buttons:
            button = tk.Button(self, text=button_info['Name'],
                               command=button_info['command'])
            button.grid(row=button_info['row'], column=button_info['column'],
                        **configurations)