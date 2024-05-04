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
