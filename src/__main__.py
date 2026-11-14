
"""Main entry point of the Call Me Maybe project."""

from pydantic import ValidationError

from src.cli import parse_arguments
from src.parser import load_input_files
from src.validator import (
    validate_function_definitions,
    validate_test_cases,
)


def main() -> None:
    """Run the function calling application."""
    args = parse_arguments()

    try:
        # Load input JSON files.
        functions_data, tests_data = load_input_files(
            args.functions_definition,
            args.input,
        )

        # Validate the loaded data.
        function_definitions = validate_function_definitions(
            functions_data
        )

        test_cases = validate_test_cases(tests_data)

        print("Input files loaded successfully.")
        print(f"Function definitions: {len(function_definitions)}")
        print(f"Test cases: {len(test_cases)}")

        print(
            "Input validation completed successfully."
        )

    except (OSError, ValueError, ValidationError) as error:
        print(f"Error: {error}")
        raise SystemExit(1) from error


if __name__ == "__main__":
    main()
