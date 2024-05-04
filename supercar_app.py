from supercar_controller import SupercarController
from csv_reader import Read
from supercar_model import  SupercarModel

if __name__ == '__main__':
    data = Read('data.csv')
    data.insert()
    Supercar = SupercarController(SupercarModel(data.info))
    Supercar.ui.run()
