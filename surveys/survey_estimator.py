"""
Calculating the probability of becoming a panelist.
"""

import abc
from typing import Sequence, NoReturn, Iterable

from surveys import single_answer


class SurveyEstimator(abc.ABC):
    """
    The prototype for the estimator.
    """

    def initialize(self, answers: Iterable[Sequence[single_answer.SingleAnswer]]) -> NoReturn:
        """
        Initializes the estimator with already gathered answers.
        :param answers: Already gathered answers.
        """
        for answer in answers: self.add_answer(answer)

    @abc.abstractmethod
    def add_answer(self, answer: Sequence[single_answer.SingleAnswer]) -> NoReturn:
        """
        Adds new answer.
        :param answer: A new answer.
        """
        pass

    @abc.abstractmethod
    def estimate(self, answer: Sequence[single_answer.SingleAnswer], n_answered: int) -> float:
        """
        Estimates the current probability of becoming a panelist
        given n_answered answers kept in the answer variable.
        :param answer: Contains SingleAnswer objects.
        :param n_answered: Specifies the number of already answered questions.
        """
        pass


class SurveyEstimator1(SurveyEstimator):
    """
    Suggested implementation of the SurveyEstimator prototype class.
    """

    def __init__(self, n_questions):
        self._n_questions = n_questions
        self._counts = n_questions * [0]
        self._xF_counts = n_questions * [0]
        self._n_answers = 0

    def add_answer(self, answer: Sequence[single_answer.SingleAnswer]) -> NoReturn:
        self._n_answers += 1
        false_streak = True
        for i, s_answer in enumerate(answer):
            if s_answer == single_answer.SingleAnswer.NO or \
                    s_answer == single_answer.SingleAnswer.UNKNOWN and self._counts[i] / self._n_answers >= 0.5:
                self._counts[i] += 1
            else:
                false_streak = False
            if false_streak: self._xF_counts[i] += 1

    def estimate(self, answer: Sequence[single_answer.SingleAnswer], n_answered: int) -> float:
        xF = 0
        multiplier = 1.0
        for i in range(n_answered):
            if answer[i] == single_answer.SingleAnswer.YES:
                break
            xF += 1
            if answer[i] == single_answer.SingleAnswer.UNKNOWN:
                multiplier *= self._counts[i] / self._n_answers
        if xF == 0: return 0.0

        return multiplier * self._xF_counts[self._n_questions - 1] / self._xF_counts[xF - 1]
