import numpy as np
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

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
                    'max': np.max(data),
                    'min': np.min(data),
                    'mean': np.mean(data),
                    'median': np.median(data),
                    'mode': float(np.bincount(data).argmax()),
                    'std_dev': np.std(data),
                    'variance': np.var(data)
                }
                statistics_list.append(statistics_dict)
        return statistics_list

    def get_info_for_part_to_whole(self):
        car_make_counts = {}
        others = 0
        for entry in self.data:
            car_make = entry['Car Make']
            count = 0
            for car in self.data:
                if car['Car Make'] == car_make:
                    count += 1
            if count <= 2:
                others += count
            else:
                car_make_counts[car_make] = count
        car_make_counts['Others'] = others
        return car_make_counts

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

    def comparison_plotter(self, car1, car2):
        attributes = ['Engine Size (L)', 'Horsepower', 'Torque (lb-ft)',
                      '0-60 MPH Time (seconds)', 'Price (in USD)']
        if car1['Price (in USD)'] < car2['Price (in USD)']:
            car1, car2 = car2, car1

        num_attributes = len(attributes)
        attribute_indices = np.arange(num_attributes)  # Index values for the bars
        bar_width = 0.35  # Width of the bars

        # Plotting
        fig, ax = plt.subplots(figsize=(10, 6))

        car1_values = [car1[attr] for attr in attributes]
        car2_values = [car2[attr] for attr in attributes]

        ax.bar(attribute_indices - bar_width / 2, car1_values, bar_width, label=car1['Car Make'])
        ax.bar(attribute_indices + bar_width / 2, car2_values, bar_width, label=car2['Car Make'])

        # Add labels and legend
        ax.set_xlabel('Attributes')
        ax.set_ylabel('Values')
        ax.set_title('Comparison of Selected Cars')
        ax.set_xticks(attribute_indices)
        ax.set_xticklabels(attributes)
        ax.legend()
        return fig

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
        correlation_coefficient = np.corrcoef(data1, data2)[0, 1]
        # Create a new Figure
        fig = Figure(figsize=(5, 3), dpi=100)

        # Add a subplot to the Figure
        ax = fig.add_subplot(111)

        # Create scatter plot
        ax.scatter(data1, data2, alpha=0.7, color='red')

        # Set title and labels
        ax.set_title(f'Correlation Plot: {attribute1} vs {attribute2}')
        ax.set_xlabel(attribute1)
        ax.set_ylabel(attribute2)
        ax.text(0.05, 0.95,
                f'Correlation Coefficient: {correlation_coefficient:.2f}',
                verticalalignment='top', horizontalalignment='left',
                transform=ax.transAxes, fontsize=12, color='green')
        return fig

    def part_to_whole_plotter(self, data):
        labels = data.keys()
        sizes = data.values()
        # Create a new Figure
        fig = plt.figure(figsize=(5, 3), dpi=100)
        # Add a subplot to the Figure
        ax = fig.add_subplot(111)
        # Create pie chart
        ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
        ax.axis('equal')
        return fig

    def get_info_from_year(self, year, attribute):
        result = []
        for car in self.data:
            if car['Year'] == year:
                if attribute == 'Price (in USD)':
                    result.append(eval(car[attribute].replace(',', '')))
                else:
                    result.append(float(car[attribute]))

        return result

    def get_info_time_series(self, attribute):
        info = {}
        years = ['2020', '2021', '2022', '2023']
        print(attribute)
        for year in years:
            car_info = self.get_info_from_year(year, attribute)
            info[year] = np.mean(car_info)
        return info
