from supercar_ui import SupercarUI
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import ttk
from tkinter import messagebox
import matplotlib.pyplot as plt
from tkinter import Toplevel

class SupercarController:
    """Controller class for the calculator application."""

    def __init__(self, model):
        self.ui = SupercarUI(self)
        self.model = model

    def show_search_result(self):
        search_text = self.ui.search_results_frame.search.get()
        if not search_text:
            self.ui.search_results_frame.result_box.delete(0, tk.END)
            self.ui.search_results_frame.result_label.config(
                text=f"Results: (0 results)")
            return
        result = self.model.get_search_result(search_text)
        self.ui.search_results_frame.result_box.delete(0, tk.END)
        for car in result:
            self.ui.search_results_frame.result_box.insert(tk.END, f"{car['Car Make']} - {car['Car Model']}")
        if len(result)==1:
            self.ui.search_results_frame.result_label.config(
                text=f"Results: (1 result)")
        else:
            self.ui.search_results_frame.result_label.config(text=f"Result: ({len(result)} results)")

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

    def add_to_compare_list(self):
        selected_index = self.ui.search_results_frame.result_box.curselection()
        if selected_index:
            if self.ui.comparison_frame.compare_box.size() == 2:
                messagebox.showerror("Error", "You can select at most 2 cars in compare box.")
                return
            selected_car = self.ui.search_results_frame.result_box.get(selected_index)
            self.ui.comparison_frame.add_to_compare(selected_car)

    def generate_comparison(self):
        if self.ui.comparison_frame.compare_box.size() != 2:
            messagebox.showerror("Error","Please select 2 cars to continue comparing.")
            return
        car1 = self.ui.comparison_frame.compare_box.get(0)
        car2 = self.ui.comparison_frame.compare_box.get(1)

        # Retrieve data for the selected cars from the model
        car1_data = self.model.car_getter(car1)
        car2_data = self.model.car_getter(car2)
        # Extract attributes for comparison
        fig = self.model.comparison_plotter(car1_data, car2_data)
        comparison_window = tk.Tk()
        comparison_window.title('Comparison Graph')
        comparison_window.geometry('800x600')

        # Embed the plot in the new window
        canvas = FigureCanvasTkAgg(fig, master=comparison_window)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        plt.close()
        comparison_window.mainloop()
        return

    def clear_comparison(self):
        self.ui.comparison_frame.compare_box.delete(0, tk.END)

    def remove_selected(self):
        selected_indices = self.ui.comparison_frame.compare_box.curselection()
        self.ui.comparison_frame.compare_box.delete(selected_indices)

    def show_descriptive(self):
        data = self.model.get_descriptive_statistics()
        self.ui.show_descriptive_window(data)

    def show_distribution(self):
        self.ui.show_distribution_window()

    def show_correlation(self):
        self.ui.show_correlation_window()

    def show_part_to_whole(self):
        self.ui.show_part_to_whole_window()

    def show_time_series(self):
        self.ui.show_time_series_window()

    def generate_distribution(self, attribute):
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
        canvas.get_tk_widget().pack(side=tk.RIGHT, anchor='n',padx=10, pady=10, fill=tk.BOTH, expand=True)

    def generate_correlation(self, attribute1, attribute2):
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
        data = self.model.get_info_for_part_to_whole()
        # Pie chart
        fig = self.model.part_to_whole_plotter(data)
        # Embed histogram in frame
        canvas = FigureCanvasTkAgg(fig, master=self.ui.main_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.RIGHT, anchor='n', padx=10,
                                    pady=10, fill=tk.BOTH, expand=True)

    def generate_time_series(self, attribute):
        pass
