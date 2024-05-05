import tkinter as tk
from tkinter import ttk
num_attributes = ['Year', 'Engine Size (L)',
                  'Horsepower', 'Torque (lb-ft)',
                  '0-60 MPH Time (seconds)',
                  'Price (in USD)']


class DistributionFrame(tk.Frame):
    def __init__(self, parent, ui, controller, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.ui = ui
        self.controller = controller
        self.init_components()

    def init_components(self):
        # Configurations
        configurations = {'padx': 10, 'pady': 10}

        # Add combobox to select attribute
        ttk.Label(self, text="Select Attribute:").pack(side=tk.TOP,
                                                                  anchor='nw',
                                                                  **configurations)
        attribute_combo = ttk.Combobox(self, values=num_attributes)
        attribute_combo.pack(side=tk.TOP, anchor='nw', **configurations)

        # Add button to generate distribution graph and back to main window button
        ttk.Button(self, text="Generate",
                   command=lambda: self.controller.generate_distribution(
                       attribute_combo.get())).pack(side=tk.LEFT, anchor='n',
                                                    **configurations)
        ttk.Button(self, text="Back",
                   command=self.ui.show_main_window).pack(side=tk.RIGHT,
                                                       anchor='e',
                                                       **configurations)


class CorrelationFrame(tk.Frame):
    def __init__(self, parent, ui, controller, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.ui = ui
        self.controller = controller
        self.init_components()

    def init_components(self):
        # Configurations
        configurations = {'padx': 10, 'pady': 10}

        # Add combobox to select attribute
        ttk.Label(self, text=f"Select Attribute1:").pack(side=tk.TOP,anchor='nw', **configurations)
        attribute_combo = ttk.Combobox(self, values=num_attributes)
        attribute_combo.pack(side=tk.TOP,anchor='nw', **configurations)

        ttk.Label(self, text=f"Select Attribute2:").pack(side=tk.TOP,anchor='nw', **configurations)
        attribute2_combo = ttk.Combobox(self, values=num_attributes)
        attribute2_combo.pack(side=tk.TOP,anchor='nw', **configurations)
        ttk.Button(self, text="Generate",
                   command=lambda: self.controller.generate_correlation(
                       attribute_combo.get(), attribute2_combo.get())).pack(side=tk.LEFT,anchor='sw',
            **configurations)
        ttk.Button(self, text="Back",
                   command=self.ui.show_main_window).pack(side=tk.LEFT,anchor='sw',**configurations)


class DescriptiveFrame(tk.Frame):
    def __init__(self, parent, data, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.data = data
        self.init_components()

    def init_components(self):
        # Configurations
        configurations = {'padx': 10, 'pady': 5}
        self.config(borderwidth=4, relief="groove", width=300, height=150)
        ttk.Label(self, text=self.data['attribute'].capitalize(), font=("TkDefaultFont", 14, "underline")).pack(side=tk.TOP, **configurations)
        self.data.pop('attribute')
        for keys, values in self.data.items():
            ttk.Label(self, text=f"{keys.capitalize()}: {values}", font=("TkDefaultFont", 11)).pack(side=tk.TOP, **configurations)
