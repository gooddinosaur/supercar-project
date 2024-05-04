import tkinter as tk
from PIL import ImageTk, Image


class ComparisonFrame(tk.Frame):
    def __init__(self, parent, ui,controller, *args, **kwargs):
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
        main_label = tk.Label(self, text="Supercar choosing helper and analysis", font=("Helvetica", 16))
        main_label.pack(side=tk.TOP)

        # Comparison box
        compare_lable = tk.Label(self, text="Comparison box", font=("Helvetica", 12))
        compare_lable.pack(side=tk.TOP, anchor="w")
        compare_box = tk.Listbox(self, font=('Arial', 12), width=40, height=10)
        compare_box.pack(side=tk.TOP)

        # Button for interact with comparison box
        interact_buttons = InteractButton(self, self.controller)
        interact_buttons.pack(side=tk.TOP)

        # Back to Main Menu Button
        back_button = tk.Button(self, text="Back to Main Menu", command=self.ui.show_startup_window)
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
