import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
from frames_for_main_window import SearchResultsFrame, ComparisonFrame, StatisticFrame
from frames_for_statistic import DistributionFrame, CorrelationFrame

num_attributes = ['Year', 'Engine Size (L)',
                  'Horsepower', 'Torque (lb-ft)',
                  '0-60 MPH Time (seconds)',
                  'Price (in USD)']


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
        self.minsize(1000, 510)
        self.show_startup_window()

    def show_startup_window(self):
        self.main_frame.destroy()
        self.main_frame = tk.Frame(self)
        self.main_frame.pack(fill="both", expand=True)

        # New frame for showing pictures
        picture_frame = tk.Frame(self.main_frame, width=200)
        picture_frame.pack(side="left", fill="both", expand=True)

        # Import and display picture
        image = Image.open("Images/startup_image.jpg")
        image = image.resize((772, 454), Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)

        picture_label = tk.Label(picture_frame, image=photo)
        picture_label.image = photo
        picture_label.pack(pady=10, expand=True)

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

        # Left side frame
        self.search_results_frame = SearchResultsFrame(self.main_frame, self.controller)
        self.search_results_frame.pack(side=tk.LEFT, fill="both", expand=True, padx=10, pady=10)

        # Middle frame
        self.comparison_frame = ComparisonFrame(self.main_frame, self, self.controller)
        self.comparison_frame.pack(side=tk.LEFT, fill="both", expand=True, padx=10, pady=10)

        # Right frame
        self.statistic_frame = StatisticFrame(self.main_frame, self.controller)
        self.statistic_frame.pack(side=tk.LEFT, fill="both", expand=True, padx=10, pady=10)

        self.histogram_frame = tk.Frame(self.main_frame)
        self.histogram_frame.pack(side=tk.LEFT, fill="both", expand=True, padx=10, pady=10)

    def quit_program(self):
        self.destroy()

    def run(self):
        self.mainloop()

    def show_descriptive_window(self, datas):
        configurations = {'padx': 10, 'pady': 10}
        for widget in self.main_frame.winfo_children():
            widget.destroy()
        ttk.Label(self.main_frame, text="Descriptive Statistics").pack(side=tk.LEFT, anchor='n', **configurations)
        ttk.Button(self.main_frame, text="Back",
                   command=self.show_main_window).pack(side=tk.RIGHT,
                                                       anchor='n',
                                                       **configurations)
        print(datas)

    def show_distribution_window(self):
        # Clear previous content
        for widget in self.main_frame.winfo_children():
            widget.destroy()
        distribution_interacter = DistributionFrame(self.main_frame, self, self.controller)
        distribution_interacter.pack(side=tk.LEFT, anchor='n')

    def show_correlation_window(self):
        # Clear previous content
        for widget in self.main_frame.winfo_children():
            widget.destroy()
        correlation_interacter = CorrelationFrame(self.main_frame, self, self.controller)
        correlation_interacter.pack(side=tk.LEFT, anchor='n')
