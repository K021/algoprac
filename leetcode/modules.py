from typing import Iterable, Tuple, Any

from pydantic import BaseModel


class TestFailed(Exception):
    """Test failed"""

    ...


class TestCase(BaseModel):
    """Test case for a solution function"""
    input: Tuple
    output: Any
    operator: str = "__eq__"

    def check(self, output):
        return getattr(self.output, self.operator)(output)


class TestManager:
    """Test manager for a solution function"""

    def __init__(self, test_cases: Iterable[TestCase]):
        self.test_cases = test_cases

    def run(self, solution):
        for case_number, test_case in enumerate(self.test_cases):
            output = solution(*test_case.input)
            if test_case.check(output) is False:
                raise TestFailed(
                    f"[TestCase #{case_number + 1}] "
                    f"Expected `{test_case.output}`, got `{output}`"
                )

        print(f"All tests passed (Total TestCases: {len(self.test_cases)})")
