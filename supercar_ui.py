import tkinter as tk
from tkinter import ttk, PhotoImage
from PIL import ImageTk, Image
from frames_for_main_window import SearchResultsFrame, ComparisonFrame, \
    StatisticFrame
from frames_for_statistic import DistributionFrame, CorrelationFrame, \
    DescriptiveFrame, TimeSeriesFrame


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
        self.minsize(1000, 535)
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
        image = image.resize((800, 454), Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)

        picture_label = tk.Label(picture_frame, image=photo)
        picture_label.image = photo
        picture_label.pack(side="left", fill="both", expand=True)

        startup_label = tk.Label(self.main_frame,
                                 text="Supercar choosing helper\nand analysis",
                                 font=("Helvetica", 13), wraplength=170)
        startup_label.pack(side="top", padx=20, pady=10, expand=True)

        startup_button = tk.Button(self.main_frame, text="Start", width=10,
                                   height=2, font=("Helvetica", 11, 'bold'),
                                   command=self.show_main_window)
        startup_button.pack(side="top", padx=20, pady=10, expand=True)

        story_button = tk.Button(self.main_frame, text="Story", width=10,
                                 height=2, font=("Helvetica", 11, 'bold'),
                                 command=self.show_story_window)
        story_button.pack(side="top", padx=20, pady=10, expand=True)

        quit_button = tk.Button(self.main_frame, text="Quit", width=10,
                                height=2, font=("Helvetica", 11, 'bold'),
                                command=self.quit_program)
        quit_button.pack(side="top", padx=20, pady=10, expand=True)

    def show_story_window(self):
        # Clear previous content
        configurations = {'padx': 10, 'pady': 7}
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        # Label and Back button
        ttk.Button(self.main_frame, text="Back",
                   command=self.show_startup_window).pack(side=tk.RIGHT,
                                                          anchor='n',
                                                          **configurations)
        ttk.Label(self.main_frame, text="Storytelling page", font=("Arial", 15)).pack(
            side=tk.TOP, anchor='nw', **configurations)


        # Create picture frame and place the image
        picture_frame = tk.Frame(self.main_frame, width=200)
        picture_frame.pack(side=tk.LEFT, anchor='n', padx=10, pady=10)

        image = Image.open('Images/jesko.jpg')
        image = image.resize((320, 173), Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)

        picture_label = tk.Label(picture_frame, image=photo)
        picture_label.image = photo
        picture_label.pack()

        ttk.Label(self.main_frame, text="Fastest car brand is Koenigsegg.\n"
                                        "Average horsepower is 1440\n"
                                        "Average torque is 1060 lb-ft\n"
                                        "Average 0-60 MPH Time is 2.3 seconds\n"
                                        "Average price is 2,800,000 USD",
                  font=("Arial", 14)).pack(
            side=tk.TOP, anchor='nw', **configurations)
        ttk.Label(self.main_frame, text="Meanwhile, the average horsepower of "
                                        "all supercars is 616. So, the average horsepower of Koenigsegg is  234% higher than the average horsepower of supercars.",
                  font=("Arial", 12), wraplength=550).pack(side=tk.TOP, anchor='nw', padx=10)

    def show_main_window(self):
        options = {"expand": True, "fill": tk.BOTH, "padx": 10, 'pady': 10}
        self.main_frame.destroy()
        self.main_frame = tk.Frame(self)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Left side frame
        self.search_results_frame = SearchResultsFrame(self.main_frame,
                                                       self.controller)
        self.search_results_frame.pack(side=tk.LEFT, **options)

        # Middle frame
        self.comparison_frame = ComparisonFrame(self.main_frame, self,
                                                self.controller)
        self.comparison_frame.pack(side=tk.LEFT, **options)

        # Right frame
        self.statistic_frame = StatisticFrame(self.main_frame, self.controller)
        self.statistic_frame.pack(side=tk.LEFT, **options)

    def quit_program(self):
        self.destroy()

    def run(self):
        self.mainloop()

    def show_descriptive_window(self, datas):
        # Clear previous content
        configurations = {'padx': 10, 'pady': 10, 'sticky': 'nsew'}
        for widget in self.main_frame.winfo_children():
            widget.destroy()
        ttk.Label(self.main_frame,
                  text="Descriptive Statistics of all attributes:", font=("TkDefaultFont", 13)).grid(row=0,
                                                                         column=0, **configurations)
        ttk.Button(self.main_frame, text="Back",
                   command=self.show_main_window).grid(row=0, column=4,
                                                       **configurations)
        col = 0
        r = 2
        for data in datas:
            if col == 3:
                r += 1
                col = 0
            frame = DescriptiveFrame(self.main_frame, data)
            frame.grid(row=r, column=col, **configurations)
            col += 1

    def show_distribution_window(self):
        # Clear previous content
        for widget in self.main_frame.winfo_children():
            widget.destroy()
        distribution_interacter = DistributionFrame(self.main_frame, self,
                                                    self.controller)
        distribution_interacter.pack(side=tk.LEFT, anchor='n')

    def show_correlation_window(self):
        # Clear previous content
        for widget in self.main_frame.winfo_children():
            widget.destroy()
        correlation_interacter = CorrelationFrame(self.main_frame, self,
                                                  self.controller)
        correlation_interacter.pack(side=tk.LEFT, anchor='n')

    def show_part_to_whole_window(self):
        # Clear previous content
        for widget in self.main_frame.winfo_children():
            widget.destroy()
        configurations = {'padx': 10, 'pady': 10}
        ttk.Button(self.main_frame, text="Back",
                   command=self.show_main_window).pack(side=tk.RIGHT,
                                                       anchor='nw',
                                                       **configurations)
        ttk.Label(self.main_frame,
                  text="The pie graph visually represents the "
                       "proportion of cars from each brand relative to the "
                       "total number of cars.", font=('Arial', 12)).pack(
            side=tk.TOP, anchor='w', **configurations)

        self.controller.generate_part_to_whole()

    def show_time_series_window(self):
        # Clear previous content
        for widget in self.main_frame.winfo_children():
            widget.destroy()
        time_series_interacter = TimeSeriesFrame(self.main_frame, self,
                                                 self.controller)
        time_series_interacter.pack(side=tk.LEFT, anchor='n')
