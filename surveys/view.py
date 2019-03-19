"""
View from the MVC pattern.
"""

from typing import Sequence, NoReturn

from surveys.controller import Controller


class View:
    """
    The main view class.
    """

    def run(self, controller: Controller, questions: Sequence[str]) -> NoReturn:
        """
        Runs the facade of the application responsible
        for interactions with the user.
        :param controller: Controller instance.
        :param questions: Sequence of questions to ask.
        """
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
