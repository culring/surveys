from yougov.controller import Controller


class View:
    def __init__(self, controller: Controller):
        self._controller = controller

    def run(self):
        questions = [
            '1. Do you live outside of UK?',
            '2. Are you underaged?',
            '3. Are you unemployed?',
            '4. Have you ever been in prison?',
            '5. Have you previously participated in an online survey?'
        ]
        print('You will be given 5 questions. '
              'For each of those type T (true), F (false) or U (answer unknown).')
        for i in range(5):
            question = questions[i]
            answer = input(f'{question}: ')
            if answer in ['T', 'F', 'U']:
                self._controller.process_response(answer)
            else:
                print('Invalid type of answer. You can provide either T, F or U. ')
                i -= 1

