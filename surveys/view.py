from typing import Sequence

from surveys.controller import Controller


class View:
    def run(self, controller: Controller, questions: Sequence[str]):
        print(f'You will be given {len(questions)} questions. '
              'For each of those type T (true), F (false) or U (preferred not to answer).')
        i = 1
        while i <= len(questions):
            question = questions[i - 1]
            answer = input(f'{question}: ')
            if answer in ['T', 'F', 'U']:
                score = controller.process(answer)
                print(f'Your current chance of becoming a panelist is equal {score * 100}%.')
                i += 1
            else:
                print('Invalid type of answer. You can provide either T, F or U.')
