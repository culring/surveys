from surveys.single_answer import SingleAnswer
from surveys.survey_estimator import SurveyEstimator1


def test_estimator1():
    estimator = SurveyEstimator1(5)
    answers = 2 * [3 * [SingleAnswer.NO] + [SingleAnswer.YES] + [SingleAnswer.NO]] + [5 * [SingleAnswer.NO]]
    estimator.initialize(answers)
    assert estimator.estimate(3 * [SingleAnswer.NO] + 2 * [SingleAnswer.UNKNOWN], 3) == 1 / 3
