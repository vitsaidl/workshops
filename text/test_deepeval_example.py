from deepeval import evaluate
from deepeval.test_case import LLMTestCase, SingleTurnParams
from deepeval.metrics import GEval
from deepeval import assert_test

def test_example():
    correctness_metric = GEval(
        model="gpt-4.1-mini",
        name="Correctness",
        criteria="Determine if the 'actual output' is correct based on the 'expected output'.",
        evaluation_params=[SingleTurnParams.ACTUAL_OUTPUT, SingleTurnParams.EXPECTED_OUTPUT],
        threshold=0.5,
        verbose_mode=True
    )

    test_case = LLMTestCase(
        input="Když jsou králící šťastní, skáčou radostí?",
        actual_output="Ano, když jsou králící šťastní, tak skáčou.",
        expected_output="Ano, králíci skáčou radostí a tento projev je jasným znakem maximálního štěstí, bezpečí a životní energie. Tomuto specifickému chování se v chovatelské komunitě mezinárodně říká binky."
    )

    assert_test(test_case, [correctness_metric])