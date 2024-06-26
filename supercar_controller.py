"""Controller for supercar project"""
from tkinter import messagebox
import tkinter as tk
from supercar_ui import SupercarUI
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt


class SupercarController:
    """Controller class for the supercar choosing helper and analysis
    application."""

    def __init__(self, model):
        self.ui = SupercarUI(self)
        self.model = model

    def show_search_result(self):
        """Display search results based on user input."""
        search_text = self.ui.search_results_frame.search.get()
        attribute = self.ui.search_results_frame.selected_attribute.get()
        min = self.ui.search_results_frame.min.get()
        max = self.ui.search_results_frame.max.get()
        if not search_text and min == '' and max == '':
            self.ui.search_results_frame.result_box.delete(0, tk.END)
            self.ui.search_results_frame.result_label.config(
                text="Results: (0 results)")
            return
        result_text = self.model.get_search_result(search_text)
        result_min_max = self.model.get_search_result_min_max(min, max, attribute)
        if len(result_text) == 0:
            results = result_min_max
        elif len(result_min_max) == 0 and min == '' and max == '':
            results = result_text
        else:
            results = [car for car in result_text if car in result_min_max]

        self.ui.search_results_frame.result_box.delete(0, tk.END)
        for car in results:
            self.ui.search_results_frame.result_box.insert(
                tk.END, f"{car['Car Make']} - {car['Car Model']}")
        if len(results) == 1:
            self.ui.search_results_frame.result_label.config(
                text="Results: (1 result)")
        else:
            self.ui.search_results_frame.result_label.config(
                text=f"Results: ({len(results)} results)")

    def on_car_select(self, event):
        """Handle selection of a car from the search results."""
        # Get the selected car from the result box
        selected_index = self.ui.search_results_frame.result_box.curselection()
        if selected_index:
            index = int(selected_index[0])
            self.selected_car = self.model.data[index]
            self.ui.search_results_frame.show_spec_button['state'] = tk.NORMAL
            self.ui.search_results_frame.add_com_button['state'] = tk.NORMAL

    def show_car_specs(self):
        """Display the specifications of the selected car."""
        # Get the selected car from the result box
        selected_index = self.ui.search_results_frame.result_box.curselection()
        if selected_index:
            index = int(selected_index[0])
            selected_car = self.ui.search_results_frame.result_box.get(index)
            selected_car_info = self.model.car_getter(selected_car)
            # Create a new window to display the information about the selected car
            car_specs_window = tk.Toplevel()
            car_specs_window.title("Car Specs")
            car_specs_window.minsize(230, 170)
            car_specs_frame = tk.Frame(car_specs_window)
            car_specs_frame.pack()
            # Display car information in labels
            for key, value in selected_car_info.items():
                label = tk.Label(car_specs_frame, text=f"{key}: {value}")
                label.pack()

    def add_to_compare_list(self):
        """Add the selected car to the comparison list."""
        selected_index = self.ui.search_results_frame.result_box.curselection()
        if selected_index:
            if self.ui.comparison_frame.compare_box.size() == 2:
                messagebox.showerror("Error", "You can select at most 2 cars in compare box.")
                return
            selected_car = self.ui.search_results_frame.result_box.get(selected_index)
            self.ui.comparison_frame.add_to_compare(selected_car)

    def generate_comparison(self):
        """Generate a comparison between two selected cars."""
        if self.ui.comparison_frame.compare_box.size() != 2:
            messagebox.showerror("Error","Please select 2 cars to continue comparing.")
            return
        car1 = self.ui.comparison_frame.compare_box.get(0)
        car2 = self.ui.comparison_frame.compare_box.get(1)

        # Retrieve data for the selected cars from the model
        car1_data = self.model.car_getter(car1)
        car2_data = self.model.car_getter(car2)

        # Show result in result box
        if car1_data['Year'] > car2_data['Year']:
            car_name = car1_data['Car Make'] + ' - ' + car1_data['Car Model']
            self.ui.comparison_frame.result_box.year_label.config(
                text=f'Newer: {car_name}')
        else:
            car_name = car2_data['Car Make'] + ' - ' + car2_data['Car Model']
            self.ui.comparison_frame.result_box.year_label.config(
                text=f'Newer: {car_name}')

        if car1_data['Engine Size (L)'] > car2_data['Engine Size (L)']:
            car_name = car1_data['Car Make'] + ' - ' + car1_data['Car Model']
            self.ui.comparison_frame.result_box.engine_label.config(
                text=f'Larger engine size: {car_name}')
        else:
            car_name = car2_data['Car Make'] + ' - ' + car2_data['Car Model']
            self.ui.comparison_frame.result_box.engine_label.config(
                text=f'Larger engine size: {car_name}')

        if car1_data['Horsepower'] > car2_data['Horsepower']:
            car_name = car1_data['Car Make'] + ' - ' + car1_data['Car Model']
            self.ui.comparison_frame.result_box.horse_label.config(
                text=f'More horsepower: {car_name}')
        else:
            car_name = car2_data['Car Make'] + ' - ' + car2_data['Car Model']
            self.ui.comparison_frame.result_box.horse_label.config(
                text=f'More horsepower: {car_name}')

        if car1_data['Torque (lb-ft)'] > car2_data['Torque (lb-ft)']:
            car_name = car1_data['Car Make'] + ' - ' + car1_data['Car Model']
            self.ui.comparison_frame.result_box.torque_label.config(
                text=f'More torque: {car_name}')
        else:
            car_name = car2_data['Car Make'] + ' - ' + car2_data['Car Model']
            self.ui.comparison_frame.result_box.torque_label.config(
                text=f'More torque: {car_name}')

        if car1_data['0-60 MPH Time (seconds)'] < car2_data['0-60 MPH Time (seconds)']:
            car_name = car1_data['Car Make'] + ' - ' + car1_data['Car Model']
            self.ui.comparison_frame.result_box.time_label.config(
                text=f'Better 0-60 MPH time: {car_name}')
        else:
            car_name = car2_data['Car Make'] + ' - ' + car2_data['Car Model']
            self.ui.comparison_frame.result_box.time_label.config(
                text=f'Better 0-60 MPH time: {car_name}')

        if car1_data['Price (in USD)'] < car2_data['Price (in USD)']:
            car_name = car1_data['Car Make'] + ' - ' + car1_data['Car Model']
            self.ui.comparison_frame.result_box.price_label.config(
                text=f'Cheaper: {car_name}')
        else:
            car_name = car2_data['Car Make'] + ' - ' + car2_data['Car Model']
            self.ui.comparison_frame.result_box.price_label.config(
                text=f'Cheaper: {car_name}')

        # Extract attributes for comparison
        fig = self.model.comparison_plotter(car1_data, car2_data)
        comparison_window = tk.Tk()
        comparison_window.title('Comparison Graph')

        # Embed the plot in the new window
        canvas = FigureCanvasTkAgg(fig, master=comparison_window)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        plt.close()
        comparison_window.mainloop()
        return

    def clear_comparison(self):
        """Clear the comparison list and result labels."""
        self.ui.comparison_frame.compare_box.delete(0, tk.END)
        for label in self.ui.comparison_frame.result_box.winfo_children():
            label.config(text="")

    def remove_selected(self):
        """Remove the selected car from the comparison list."""
        selected_indices = self.ui.comparison_frame.compare_box.curselection()
        self.ui.comparison_frame.compare_box.delete(selected_indices)

    def show_descriptive(self):
        """Display descriptive statistics."""
        data = self.model.get_descriptive_statistics()
        self.ui.show_descriptive_window(data)

    def show_distribution(self):
        """Display the distribution of selected attributes."""
        self.ui.show_distribution_window()

    def show_correlation(self):
        """Display the correlation between selected attributes."""
        self.ui.show_correlation_window()

    def show_part_to_whole(self):
        """Display the part-to-whole relationship."""
        self.ui.show_part_to_whole_window()

    def show_time_series(self):
        """Display the time series data."""
        self.ui.show_time_series_window()

    def generate_distribution(self, attribute):
        """Generate a distribution histogram for the selected attribute."""
        if not attribute:
            messagebox.showerror("Error", "Please select attribute")
            return
        for widget in self.ui.main_frame.winfo_children():
            if isinstance(widget, tk.Canvas):
                widget.destroy()
        # Create a histogram
        fig = self.model.distribution_histogram_plotter(attribute)
        # Embed histogram in frame
        canvas = FigureCanvasTkAgg(fig, master=self.ui.main_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.RIGHT, anchor='n',padx=10,
                                    pady=10, fill=tk.BOTH, expand=True)

    def generate_correlation(self, attribute1, attribute2):
        """Generate a scatter plot for the correlation between two attributes."""
        if not attribute1 or not attribute2:
            messagebox.showerror("Error", "Please select 2 attributes")
            return
        for widget in self.ui.main_frame.winfo_children():
            if isinstance(widget, tk.Canvas):
                widget.destroy()

        # Create scatter
        fig = self.model.correlation_plotter(attribute1, attribute2)
        # Embed histogram in frame
        canvas = FigureCanvasTkAgg(fig, master=self.ui.main_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.RIGHT, anchor='n', padx=10,
                                    pady=10, fill=tk.BOTH, expand=True)

    def generate_part_to_whole(self):
        """Generate a pie chart for the part-to-whole relationship."""
        data = self.model.get_info_for_part_to_whole()
        # Pie chart
        fig = self.model.part_to_whole_plotter(data)
        # Embed histogram in frame
        canvas = FigureCanvasTkAgg(fig, master=self.ui.main_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.RIGHT, anchor='n', padx=10,
                                    pady=10, fill=tk.BOTH, expand=True)

    def generate_time_series(self, attribute):
        """Generate a time series plot for the selected attribute."""
        if not attribute:
            messagebox.showerror("Error", "Please select attribute")
            return
        for widget in self.ui.main_frame.winfo_children():
            if isinstance(widget, tk.Canvas):
                widget.destroy()
        data = self.model.get_info_time_series(attribute)
        years = list(data.keys())
        values = list(data.values())

        fig, ax = plt.subplots()
        ax.plot(years, values, marker='o')
        ax.set_xlabel('Year')
        ax.set_ylabel(attribute)
        ax.set_title('Time Series of ' + attribute)
        ax.grid(True)

        canvas = FigureCanvasTkAgg(fig, master=self.ui.main_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.RIGHT, anchor='n', padx=10,
                                    pady=10, fill=tk.BOTH, expand=True)
