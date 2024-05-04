import tkinter as tk
from PIL import ImageTk, Image


class StatisticFrame(tk.Frame):
    def __init__(self, parent, controller, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.controller = controller
        self.init_components()

    def init_components(self) -> None:
        upper_frame = UpperPart(self, self.controller)
        upper_frame.pack(side=tk.TOP)

        picture_frame = tk.Frame(self, width=200)
        picture_frame.pack(side=tk.TOP)
        image = Image.open('Images/timeseries.png')
        image = image.resize((116, 100), Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)

        picture_label = tk.Label(picture_frame, image=photo)
        picture_label.image = photo
        picture_label.pack(side=tk.TOP)
        button = tk.Button(self, text='Time series')
        button.pack(side=tk.TOP,padx=10,pady=10)


class UpperPart(tk.Frame):

    def __init__(self, parent, controller, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.controller = controller
        self.init_components()

    def init_components(self):
        configurations = {'padx': 10, 'pady': 10}
        pictures = [{'File Name': 'Images/descriptive statistic.png', 'row': 0, 'column': 0},
                    {'File Name': 'Images/distribution.png', 'row': 0, 'column': 1},
                    {'File Name': 'Images/correlation.png', 'row': 2, 'column': 0},
                    {'File Name': 'Images/parttowhole.png', 'row': 2, 'column': 1}]
        for picture in pictures:
            picture_frame = tk.Frame(self, width=200)
            picture_frame.grid(row=picture['row'], column=picture['column'])
            image = Image.open(picture['File Name'])
            image = image.resize((120, 120), Image.LANCZOS)
            photo = ImageTk.PhotoImage(image)

            picture_label = tk.Label(picture_frame, image=photo)
            picture_label.image = photo
            picture_label.pack(side=tk.TOP)

        buttons = [{'Name': 'Descriptive statistic', 'row': 1, 'column': 0},
                    {'Name': 'Distribution', 'row': 1, 'column': 1},
                    {'Name': 'Correlation', 'row': 3, 'column': 0},
                    {'Name': 'Part-to-whole', 'row': 3, 'column': 1}]
        for button_info in buttons:
            button = tk.Button(self, text=button_info['Name'])
            button.grid(row=button_info['row'], column=button_info['column'], **configurations)


