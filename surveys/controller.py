"""
Controller from the MVC pattern.
"""

from typing import NoReturn

from surveys import single_answer
from surveys import survey_estimator
from surveys import survey_manager
from surveys import view


class Controller:
    """
    A controller class from the MVC pattern.
    Manages the view and the model.
    """

    def __init__(self, survey_view: 'view.View', manager: survey_manager.SurveyManager):
        """
        :param survey_view: The view.
        :param manager: The survey manager.
        """
        self._view = survey_view
        self._model = manager
        self._answer = self._model.n_questions * [single_answer.SingleAnswer.UNKNOWN]
        self._n_answered = 0
        self._n_questions = self._model.n_questions

    def run(self) -> NoReturn:
        """
        Launches the application.
        """
        self._view.run(self, self._model.questions)

    def process(self, s_answer: str) -> float:
        """
        Takes each next single answer from the view
        and returns the probability of becoming a panelist,
        providing all previous single answers.
        :param s_answer: Next SingleAnswer gathered from the view.
        :return: The probability that a person will become a panelist.
        """
        if self._n_answered == self._n_questions:
            self._answer = self._n_questions * [single_answer.SingleAnswer.UNKNOWN]
            self._n_answered = 0
        self._answer[self._n_answered] = single_answer.SingleAnswer(s_answer)
        self._n_answered += 1

        return self._model.estimate(self._answer, self._n_answered)


if __name__ == '__main__':
    v = view.View()
    m = survey_manager.SurveyManager('first_survey.csv', survey_estimator.SurveyEstimator1, 'questions.txt')
    Controller(v, m).run()
