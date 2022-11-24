from typing import Iterable, Tuple, Any

from pydantic import BaseModel


class TestFailed(Exception):
    """Test failed"""

    ...


class TestCase(BaseModel):
    input: Tuple
    output: Any


class TestManager:
    def __init__(self, inputs_and_answers: Iterable[TestCase]):
        self.inputs_and_outputs = inputs_and_answers

    def run(self, solution):
        for case_number, test_case in enumerate(self.inputs_and_outputs):
            output = solution(*test_case.input)
            if output != test_case.output:
                raise TestFailed(
                    f"[TestCase #{case_number + 1}] "
                    f"Expected {test_case.output}, got {output}"
                )
        print(f"All tests passed (Total TestCases: {len(self.inputs_and_outputs)})")
