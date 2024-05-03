from supercar_ui import SupercarUI
import tkinter as tk
import tkinter.messagebox as messagebox

class SupercarController:
    """Controller class for the calculator application."""

    def __init__(self, data):
        self.ui = SupercarUI(self)
        self.data = data

    def show_search_result(self):
        search_text = self.ui.search.get()
        if not search_text:
            messagebox.showerror("Error", "The search box is empty.")
            self.ui.result_box.delete(0, tk.END)
            return
        result = []
        for car in self.data:
            if search_text.lower() in car['Car Make'].lower() + "-" + car['Car Model'].lower():
                result.append(car)
        self.ui.result_box.delete(0, tk.END)
        for car in result:
            self.ui.result_box.insert(tk.END, f"{car['Car Make']} - {car['Car Model']}")

    def on_car_select(self, event):
        # Get the selected car from the result box
        selected_index = self.ui.result_box.curselection()
        if selected_index:
            index = int(selected_index[0])
            self.selected_car = self.data[index]

            # Enable the "Show specs" button and "Add to compare list" button
            self.ui.show_spec_button['state'] = tk.NORMAL
            self.ui.add_com_button['state'] = tk.NORMAL

    def show_car_specs(self):
        # Get the selected car from the result box
        selected_index = self.ui.result_box.curselection()
        if selected_index:
            index = int(selected_index[0])
            selected_car = self.ui.result_box.get(index)
            print(selected_car)
            selected_car_info = self.car_getter(selected_car)
            # Create a new window to display the information about the selected car
            car_specs_window = tk.Toplevel()
            car_specs_window.title("Car Specs")
            car_specs_frame = tk.Frame(car_specs_window)
            car_specs_frame.pack()
            # Display car information in labels
            for key, value in selected_car_info.items():
                label = tk.Label(car_specs_frame, text=f"{key}: {value}")
                label.pack()

    def car_getter(self, text):
        for car in self.data:
            if car['Car Make'] + " - " + car['Car Model'] == text:
                return car

