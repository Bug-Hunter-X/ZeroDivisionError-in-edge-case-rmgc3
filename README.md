# Uncommon Error: ZeroDivisionError in Edge Case
This repository demonstrates an uncommon error in a Python function that occurs when it encounters an edge case where both inputs are zero. The function does not gracefully handle this situation, leading to a ZeroDivisionError.

## Bug Description
The function `function_with_uncommon_error` aims to perform division but fails to account for a scenario where both the numerator and denominator are 0. This results in a runtime error.

## Bug Solution
The solution demonstrates the importance of handling edge cases within a function to ensure robustness and avoid unexpected errors. By adding a check for both inputs being zero, the error is prevented, and the function now returns a more appropriate value or raises a custom exception.