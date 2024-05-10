"""UI for supercar project"""
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import ImageTk, Image
from frames_for_main_window import SearchResultsFrame, ComparisonFrame, \
    StatisticFrame
from frames_for_statistic import DistributionFrame, CorrelationFrame, \
    DescriptiveFrame, TimeSeriesFrame


class SupercarUI(tk.Tk):
    """Main UI class for the Supercar choosing helper and analysis application."""

    def __init__(self, controller):
        super().__init__()
        self.title("Supercar choosing helper and analysis")
        self.search = tk.StringVar()
        self.controller = controller
        self.protocol("WM_DELETE_WINDOW", self.on_close)
        self.init_main_window()

    def init_main_window(self):
        """Initialize the main window of the application."""
        self.main_frame = tk.Frame(self)
        self.main_frame.pack(fill="both", expand=True)
        self.minsize(1100, 550)
        self.show_startup_window()

    def show_startup_window(self):
        """Show the startup window of the application."""
        self.main_frame.destroy()
        self.main_frame = tk.Frame(self)
        self.main_frame.pack(fill="both", expand=True)

        # New frame for showing pictures
        picture_frame = tk.Frame(self.main_frame, width=200)
        picture_frame.pack(side="left", fill="both", expand=True)

        # Import and display picture
        image = Image.open("Images/startup_image.jpg")
        image = image.resize((883, 523), Image.LANCZOS)
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
        """Show the storytelling window of the application."""

        # Clear previous content
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        upper_part = UpperPartStoryFrame(self.main_frame, self)
        upper_part.pack(side=tk.TOP, anchor='w')
        bottom_part = BottomPartStoryFrame(self.main_frame)
        bottom_part.pack(side=tk.LEFT, anchor='n')

    def show_main_window(self):
        """Show the main window of the application."""
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
        """Quit the program."""
        self.destroy()

    def on_close(self):
        """Handle window close events."""
        quit_ok = messagebox.askokcancel(
            title="Confirm Quit",
            message="Do you really want to quit?")
        if quit_ok:
            # exit the mainloop
            self.destroy()

    def run(self):
        """Run the application."""
        self.mainloop()

    def show_descriptive_window(self, datas):
        """Show the descriptive window with statistics."""

        # Clear previous content
        configurations = {'padx': 10, 'pady': 10, 'sticky': 'nsew'}
        for widget in self.main_frame.winfo_children():
            widget.destroy()
        ttk.Label(self.main_frame,
                  text="Descriptive Statistics of all attributes:",
                  font=("TkDefaultFont", 13)).grid(row=0,
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
        """Show the distribution window."""
        # Clear previous content
        for widget in self.main_frame.winfo_children():
            widget.destroy()
        distribution_interacter = DistributionFrame(self.main_frame, self,
                                                    self.controller)
        distribution_interacter.pack(side=tk.LEFT, anchor='n')

    def show_correlation_window(self):
        """Show the correlation window."""
        # Clear previous content
        for widget in self.main_frame.winfo_children():
            widget.destroy()
        correlation_interacter = CorrelationFrame(self.main_frame, self,
                                                  self.controller)
        correlation_interacter.pack(side=tk.LEFT, anchor='n')

    def show_part_to_whole_window(self):
        """Show the part to whole window."""
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
                       "total number of cars.",
                  font=('Arial', 13, 'bold')).pack(
            side=tk.TOP, **configurations)

        self.controller.generate_part_to_whole()

    def show_time_series_window(self):
        """Show the time series window."""
        # Clear previous content
        for widget in self.main_frame.winfo_children():
            widget.destroy()
        time_series_interacter = TimeSeriesFrame(self.main_frame, self,
                                                 self.controller)
        time_series_interacter.pack(side=tk.LEFT, anchor='n')


class UpperPartStoryFrame(tk.Frame):
    """Upper part of the storytelling frame."""

    def __init__(self, parent, ui, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.ui = ui
        self.init_components()

    def init_components(self) -> None:
        """Initialize the components of the frame."""
        configurations = {'padx': 10, 'pady': 5}

        ttk.Button(self, text="Back",
                   command=self.ui.show_startup_window).pack(side=tk.RIGHT,
                                                             anchor='n',
                                                             **configurations)
        ttk.Label(self, text="Storytelling page",
                  font=("Arial", 15)).pack(
            side=tk.TOP, anchor='nw', **configurations)

        # Create picture frame and place the image
        picture_frame = tk.Frame(self, width=200)
        picture_frame.pack(side=tk.LEFT, anchor='n', padx=10, pady=10)

        image = Image.open('Images/rimac.jpg')
        image = image.resize((330, 183), Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)

        picture_label = tk.Label(picture_frame, image=photo)
        picture_label.image = photo
        picture_label.pack()

        ttk.Label(self, text="Fastest car brand is Rimac.\n"
                             "Average horsepower is 1914 hp\n"
                             "Average torque is 1696 lb-ft\n"
                             "Average 0-60 MPH Time is 1.88 seconds\n"
                             "Average price is 2,400,000 USD",
                  font=("Arial", 14)).pack(
            side=tk.TOP, anchor='nw', **configurations)
        ttk.Label(self, text="Meanwhile, the average horsepower of "
                             "all supercars is 616 hp. So, the average "
                             "horsepower of Rimac is 311% higher than the "
                             "average horsepower of supercars. "
                             "And that's a huge number.",
                  font=("Arial", 12), wraplength=530).pack(side=tk.TOP,
                                                           anchor='nw',
                                                           padx=10)
        ttk.Label(self,
                  text="------------------------------------------------------"
                       "--------------------------------------------------",
                  font=("Arial", 12)).pack(side=tk.TOP, anchor='w', padx=10)


class BottomPartStoryFrame(tk.Frame):
    """Bottom part of the storytelling frame."""

    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.init_components()

    def init_components(self) -> None:
        """Initialize the components of the frame."""
        configurations = {'padx': 10, 'pady': 4}
        ttk.Label(self, text="Interesting relationships",
                  font=("Arial", 14)).grid(row=0, column=0, sticky='w',
                                           **configurations)
        ttk.Label(self,
                  text="Relationships between 0-60 MPH and Engine size",
                  font=("Arial", 10)).grid(row=1, column=0, sticky='n',
                                           **configurations)
        ttk.Label(self,
                  text="Relationships between 0-60 MPH and Torque",
                  font=("Arial", 10)).grid(row=1, column=1, sticky='n',
                                           **configurations)

        # Create picture frame and place the image
        picture_frame = tk.Frame(self, width=200)
        picture_frame.grid(row=2, column=0, sticky='w', padx=10, pady=0)
        image = Image.open('Images/Relationship1.png')
        image = image.resize((276, 196), Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)
        picture_label = tk.Label(picture_frame, image=photo)
        picture_label.image = photo
        picture_label.pack(side=tk.LEFT, anchor='n')

        # Create picture frame and place the image
        picture_frame = tk.Frame(self, width=200)
        picture_frame.grid(row=2, column=1, sticky='w', padx=10, pady=0)
        image = Image.open('Images/Relationship2.png')
        image = image.resize((276, 196), Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)
        picture_label = tk.Label(picture_frame, image=photo)
        picture_label.image = photo
        picture_label.pack(side=tk.LEFT, anchor='n')
        ttk.Label(self, text="First pair", font=("Arial", 10)).grid(row=3,
                                                                    column=0,
                                                                    sticky='n',
                                                                    pady=0)
        ttk.Label(self, text="Second pair", font=("Arial", 10)).grid(row=3,
                                                                     column=1,
                                                                     sticky='n',
                                                                     pady=0)
        ttk.Label(self, text="Correlation coefficient of first pair is -0.39\n"
                             "Correlation coefficient of second pair is -0.70\n"
                             " \n"
                             "Most people think that the larger engine size, the\n"
                             "faster 0-60 MPH. But from this, it means that 0-60 MPH\n"
                             "time depends on torque more than the engine size.\n"
                             " \n"
                             "So, I have done some research and found out that some\n"
                             "smaller engine sizes can have more torque some\n"
                             "bigger ones. Because torque depends on several\n"
                             "factors not only engine size such as Engine Tuning,\n"
                             "Cylinder configuration,etc."
                  , font=("Arial", 11)).grid(row=2, column=2, sticky='n',
                                             **configurations)
