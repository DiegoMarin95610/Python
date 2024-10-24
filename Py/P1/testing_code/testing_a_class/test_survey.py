import pytest
from survey import AnonymousSurvey


@pytest.fixture
def language_survey():
    """A survey that will be available to all test functions."""
    question = "What language did you first learn to speak?"
    AnonymousSurvey(question)
    return AnonymousSurvey(question)


@pytest.mark.parametrize(
    "response, expected",
    [
        ("English", "English"),
        ("Spanish", "Spanish"),
        ("Japanes", "Japanes"),
    ],
)
def testing_survey_language_responses_params(language_survey, response, expected):
    "testing con parametros"

    language_survey.store_response(response)
    assert expected in language_survey.responses


@pytest.fixture
def age_survey():
    """A survey that will be available to all test functions."""
    question = "How old are you?"
    AnonymousSurvey(question)
    return AnonymousSurvey(question)


@pytest.mark.parametrize(
    "response, expected",
    [
        (18, 18),
        (24, 24),
        (42, 42),
    ],
)
def testing_survey_ages_responses_params(language_survey, response, expected):
    "testing con parametros"

    language_survey.store_response(response)
    assert expected in language_survey.responses
