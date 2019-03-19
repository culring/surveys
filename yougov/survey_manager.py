import csv

from yougov import single_answer
from yougov import survey_estimator

from typing import Iterable, Sequence, NoReturn, List


# TODO: the original csv file with no empty lines at the end
# TODO: doesn't work. for now, it is simplified so that the file
# TODO: is initially extended with one superficial line


class SurveyManager:
    def __init__(self, filename: str, estimator: survey_estimator.SurveyEstimator):
        self._filename = filename
        with open(filename, newline='') as csvfile:
            answers_reader = csv.reader(csvfile, delimiter=',')
            self._headers = next(answers_reader)
            answers = self._preprocess(answers_reader)
        self._estimator = estimator
        # self._estimator.initialize(answers)

    def add_answer(self, answer: Sequence[single_answer.SingleAnswer]) -> NoReturn:
        """
        Adds a new answer.
        :param answer: A sequence of SingleAnswer objects representing the answer.
        """
        if len(answer) != self.n_questions:
            raise ValueError(f'Answers parameter should have the length equal {self.n_questions}.')

        with open(self._filename, 'a', newline='') as csvfile:
            answers_writer = csv.writer(csvfile, delimiter=',')
            answers_writer.writerow([s_answer.value for s_answer in answer])

        self._estimator.add_answer(answer)

    def estimate(self, answer: Sequence[single_answer.SingleAnswer], n_answered: int) -> float:
        if len(answer) != self.n_questions:
            raise ValueError(f'Answer parameter should have the length equal {self.n_questions}.')

        return self._estimator.estimate(answer, n_answered)

    @property
    def n_questions(self) -> int:
        """
        Returns the number of the questions in the survey.
        """
        return len(self._headers)

    @staticmethod
    def _preprocess(answers: Iterable[List[str]]) -> List[List[single_answer.SingleAnswer]]:
        preprocessed_answers = []
        for answer in answers:
            preprocessed_answer = []
            for s_answer in answer:
                if s_answer not in ['T', 'F', 'U']:
                    raise ValueError('A single answer in the file should be either T, F or U.')
                preprocessed_answer.append(single_answer.SingleAnswer(s_answer))
            preprocessed_answers.append(preprocessed_answer)

        return preprocessed_answers


if __name__ == '__main__':
    sm = SurveyManager('first_survey.csv', survey_estimator.SurveyEstimator1())
    sm.add_answer([single_answer.SingleAnswer.NO] * 5)
    sm.add_answer([single_answer.SingleAnswer.NO] * 5)
    sm.add_answer([single_answer.SingleAnswer.NO] * 4 + [single_answer.SingleAnswer.YES])
    print(sm.estimate([single_answer.SingleAnswer.NO] * 4 + [single_answer.SingleAnswer.UNKNOWN], 4))
