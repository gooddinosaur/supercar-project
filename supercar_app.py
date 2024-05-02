from supercar_controller import SupercarController
from csv_reader import Read


if __name__ == '__main__':
    data = Read('data.csv')
    data.insert()
    Supercar = SupercarController(data.info)
    Supercar.ui.run()

