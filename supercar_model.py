from tkinter import messagebox
import numpy as np
from matplotlib.figure import Figure


class SupercarModel:

    def __init__(self, data):
        self.data = data

    def get_search_result(self, text):
        result = []
        for car in self.data:
            if text.lower() in car['Car Make'].lower() + "-" + car['Car Model'].lower():
                result.append(car)
        return result

    def car_getter(self, text):
        for car in self.data:
            if car['Car Make'] + " - " + car['Car Model'] == text:
                return car

    def get_descriptive_statistics(self):
        statistics_list = []
        attributes = list(self.data[0].keys())
        for attribute in attributes:
            if attribute not in ['Car Make', 'Car Model']:
                data = self.get_info_for_statistic(attribute)
                statistics_dict = {
                    'attribute': attribute,
                    'mean': np.mean(data),
                    'median': np.median(data),
                    'mode': float(np.bincount(data).argmax()),
                    'std_dev': np.std(data),
                    'variance': np.var(data)
                }
                statistics_list.append(statistics_dict)
        return statistics_list

    def get_info_for_statistic(self, attribute):
        data = []
        for car in self.data:
            if attribute == 'Price (in USD)':
                    value = eval(car[attribute].replace(',', ''))
            else:
                try:
                    value = float(car[attribute])
                except:
                    pass
            data.append(value)
        return data

    def distribution_histogram_plotter(self, attribute):
        fig = Figure(figsize=(1, 4), dpi=100)
        ax = fig.add_subplot(111)
        ax.hist(self.get_info_for_statistic(attribute), bins=10, alpha=0.7, color='blue', edgecolor='black')
        ax.set_title(f'Distribution - Histogram of {attribute}')
        ax.set_xlabel(attribute)
        ax.set_ylabel('Frequency')
        return fig

    def correlation_plotter(self, attribute1, attribute2):
        data1 = self.get_info_for_statistic(attribute1)
        data2 = self.get_info_for_statistic(attribute2)

        # Create a new Figure
        fig = Figure(figsize=(8, 6), dpi=100)

        # Add a subplot to the Figure
        ax = fig.add_subplot(111)

        # Create scatter plot
        ax.scatter(data1, data2, alpha=0.7, color='red')

        # Set title and labels
        ax.set_title(f'Correlation Plot: {attribute1} vs {attribute2}')
        ax.set_xlabel(attribute1)
        ax.set_ylabel(attribute2)
        return fig
