from yougov import survey_manager
from yougov import survey_estimator
from yougov import view
from yougov import single_answer


class Controller:
    def __init__(self):
        self._view = view.View(self)
        self._model = survey_manager.SurveyManager('first_survey.csv', survey_estimator.SurveyEstimator1())
        self._answer = 5 * [single_answer.SingleAnswer.UNKNOWN]
        self._n_answered = 0

    def run(self):
        self._view.run()

    def process(self, s_answer) -> float:
        if self._n_answered == 5:
            self._answer = 5 * [single_answer.SingleAnswer.UNKNOWN]
            self._n_answered = 0
        self._answer[self._n_answered] = single_answer.SingleAnswer(s_answer)
        self._n_answered += 1

        return self._model.estimate(self._answer, self._n_answered)


if __name__ == '__main__':
    Controller().run()
