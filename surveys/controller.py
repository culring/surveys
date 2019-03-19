from surveys import single_answer
from surveys import survey_estimator
from surveys import survey_manager
from surveys import view


class Controller:
    def __init__(self, survey_view: 'view.View', manager: survey_manager.SurveyManager):
        self._view = survey_view
        self._model = manager
        self._answer = 5 * [single_answer.SingleAnswer.UNKNOWN]
        self._n_answered = 0
        self._n_questions = self._model.n_questions

    def run(self):
        self._view.run(self, self._model.questions)

    def process(self, s_answer) -> float:
        if self._n_answered == self._n_questions:
            self._answer = self._n_questions * [single_answer.SingleAnswer.UNKNOWN]
            self._n_answered = 0
        self._answer[self._n_answered] = single_answer.SingleAnswer(s_answer)
        self._n_answered += 1

        return self._model.estimate(self._answer, self._n_answered)


if __name__ == '__main__':
    v = view.View()
    m = survey_manager.SurveyManager('first_survey.csv', survey_estimator.SurveyEstimator1(), 'questions.txt')
    Controller(v, m).run()
