import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


class GraphPlotter:
    @staticmethod
    def distribution_histrogram_plotter(data, attribute):
        fig = Figure(figsize=(6, 4), dpi=100)
        ax = fig.add_subplot(111)
        ax.hist(data, bins=10, alpha=0.7, color='blue', edgecolor='black')
        ax.set_title(f'Distribution - Histogram of {attribute}')
        ax.set_xlabel(attribute)
        ax.set_ylabel('Frequency')
        return fig
