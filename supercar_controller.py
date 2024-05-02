from supercar_ui import SupercarUI


class SupercarController:
    """Controller class for the calculator application."""

    def __init__(self, data):
        self.ui = SupercarUI(self)
        self.data = data

    def show_search_result(self):
        search_text = self.ui.search.get()
        raw_result = []
        for car in self.data:
            if search_text.lower() in car['Car Make'].lower() + car['Car Model'].lower():
                raw_result.append(car)
        result = []
        for i in range(len(raw_result)):
            if raw_result[i] not in raw_result[i + 1:]:
                result.append(raw_result[i])
        return result





