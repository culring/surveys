import csv
from typing import Iterable, Sequence, NoReturn, List

from surveys import single_answer
from surveys import survey_estimator


class SurveyManager:
    def __init__(self, answers_filename: str, estimator: survey_estimator.SurveyEstimator, questions_filename: str):
        self._filename = answers_filename
        with open(answers_filename, newline='') as csvfile:
            answers_reader = csv.reader(csvfile, delimiter=',')
            self._headers = next(answers_reader)
            answers = self._preprocess(answers_reader)
        self._estimator = estimator
        self._estimator.initialize(answers)
        with open(questions_filename, newline='') as file:
            self._questions = file.read().splitlines()

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
    def questions(self) -> List[str]:
        return self._questions

    @property
    def n_questions(self) -> int:
        """
        Returns the number of the questions in the survey.
        """
        return len(self._questions)

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
