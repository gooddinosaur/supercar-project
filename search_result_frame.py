import tkinter as tk


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
        self.result_box = tk.Listbox(self, font=('Arial', 12), width=30, height=18)
        self.result_box.bind("<<ListboxSelect>>", self.controller.on_car_select)
        self.result_box.grid(row=3, column=0, padx=10, pady=5)

        # Show spec button
        self.show_spec_button = tk.Button(self, text="Show specs", command=self.controller.show_car_specs)
        self.show_spec_button.grid(row=4, column=0, sticky="w", padx=35, pady=5)
        self.show_spec_button['state'] = tk.DISABLED

        # Add to compare list button
        self.add_com_button = tk.Button(self, text="Add to compare list")
        self.add_com_button.grid(row=4, column=0, padx=(80, 0), pady=5)
        self.add_com_button['state'] = tk.DISABLED

    def on_search_key_release(self, event):
        self.controller.show_search_result()
