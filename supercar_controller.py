from supercar_ui import SupercarUI
from supercar_model import SupercarModel
import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np
from tkinter import ttk


class SupercarController:
    """Controller class for the calculator application."""

    def __init__(self, model):
        self.ui = SupercarUI(self)
        self.model = model

    def show_search_result(self):
        search_text = self.ui.search_results_frame.search.get()
        if not search_text:
            self.ui.search_results_frame.result_box.delete(0, tk.END)
            return
        result = self.model.get_search_result(search_text)
        self.ui.search_results_frame.result_box.delete(0, tk.END)
        for car in result:
            self.ui.search_results_frame.result_box.insert(tk.END, f"{car['Car Make']} - {car['Car Model']}")

    def on_car_select(self, event):
        # Get the selected car from the result box
        selected_index = self.ui.search_results_frame.result_box.curselection()
        if selected_index:
            index = int(selected_index[0])
            self.selected_car = self.model.data[index]
            self.ui.search_results_frame.show_spec_button['state'] = tk.NORMAL
            self.ui.search_results_frame.add_com_button['state'] = tk.NORMAL

    def show_car_specs(self):
        # Get the selected car from the result box
        selected_index = self.ui.search_results_frame.result_box.curselection()
        if selected_index:
            index = int(selected_index[0])
            selected_car = self.ui.search_results_frame.result_box.get(index)
            selected_car_info = self.model.car_getter(selected_car)
            # Create a new window to display the information about the selected car
            car_specs_window = tk.Toplevel()
            car_specs_window.title("Car Specs")
            car_specs_frame = tk.Frame(car_specs_window)
            car_specs_frame.pack()
            # Display car information in labels
            for key, value in selected_car_info.items():
                label = tk.Label(car_specs_frame, text=f"{key}: {value}")
                label.pack()

    def show_distribution(self):
        # Clear previous content
        for widget in self.ui.main_frame.winfo_children():
            widget.destroy()

        # Configurations
        configurations = {'padx': 10, 'pady': 10}

        # Add combobox to select attribute
        ttk.Label(self.ui.main_frame, text="Select Attribute:").grid(row=0,
                                                                     column=0,
                                                                     **configurations)
        attribute_combo = ttk.Combobox(self.ui.main_frame,
                                       values=['Year', 'Engine Size (L)',
                                               'Horsepower', 'Torque (lb-ft)',
                                               '0-60 MPH Time (seconds)',
                                               'Price (in USD)'])
        attribute_combo.grid(row=0, column=1, **configurations)

        # Add button to generate distribution graph
        ttk.Button(self.ui.main_frame, text="Generate",
                   command=lambda: self.generate_distribution(
                       attribute_combo.get())).grid(row=1, column=0,
                                                    columnspan=2,
                                                    **configurations)
        ttk.Button(self.ui.main_frame, text="Back",
                   command=self.ui.show_main_window).grid(row=2, column=0,
                                                          columnspan=2,
                                                          **configurations)

    def generate_descriptive_statistic(self, attribute):
        pass

    def generate_distribution(self, attribute):
        data = []
        for car in self.model.data:
            try:
                if attribute == 'Price (in USD)':
                    value = eval(car[attribute].replace(',', ''))
                else:
                    value = float(car[attribute])
                data.append(value)
            except (ValueError, TypeError):
                pass

        # Create a histogram
        plt.hist(data)
        plt.title(f'Distribution - Histogram of {attribute}')
        plt.xlabel(attribute)
        plt.ylabel('Frequency')
        plt.show()

    def generate_correlation(self, attribute):
        pass

    def generate_part_to_whole(self, attribute):
        pass

    def generate_time_series(self, attribute):
        pass
