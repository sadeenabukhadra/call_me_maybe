
"""Module responsible for reading JSON input files."""

import json
from pathlib import Path
from typing import Any


def load_json_file(file_path: str | Path) -> Any:
    """
    Load and return the content of a JSON file.

    Args:
        file_path: Path to the JSON file.

    Returns:
        The parsed JSON data.

    Raises:
        FileNotFoundError: If the file does not exist.
        ValueError: If the JSON content is invalid.
        OSError: If the file cannot be read.
    """
    path = Path(file_path)

    try:
        with path.open("r", encoding="utf-8") as file:
            return json.load(file)

    except FileNotFoundError:
        raise FileNotFoundError(
            f"Input file not found: {path}"
        ) from None

    except json.JSONDecodeError as error:
        raise ValueError(
            f"Invalid JSON in {path}: {error}"
        ) from error

    except UnicodeDecodeError as error:
        raise ValueError(
            f"Invalid text encoding in {path}: {error}"
        ) from error


def load_input_files(
    functions_path: str | Path,
    tests_path: str | Path
) -> tuple[Any, Any]:
    """
    Load function definitions and function calling tests.

    Args:
        functions_path: Path to the function definitions JSON file.
        tests_path: Path to the function calling tests JSON file.

    Returns:
        A tuple containing function definitions and test prompts.
    """
    functions = load_json_file(functions_path)
    tests = load_json_file(tests_path)

    return functions, tests
