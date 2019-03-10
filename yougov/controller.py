from yougov.view import View


class Controller:
    def __init__(self):
        self._view = View(self)
        # self._model = Model()
        self._question = 0

    def run(self):
        self._view.run()

    def process_response(self, response):
        self._question += 1



if __name__ == '__main__':
    Controller().run()
