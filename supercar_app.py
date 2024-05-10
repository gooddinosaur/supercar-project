"""Main script for running the supercar application.

This script initializes the necessary components for running the supercar
application, including reading data from a CSV file, initializing the model
with the read data,creating a controller with the initialized model,
and running the user interface."""

from supercar_controller import SupercarController
from csv_reader import Read
from supercar_model import SupercarModel

if __name__ == '__main__':
    data = Read('data.csv')
    data.insert()
    Supercar = SupercarController(SupercarModel(data.info))
    Supercar.ui.run()
