
"""Module responsible for saving function calling results."""

import json
from pathlib import Path
from typing import Any


def save_results(
    results: list[dict[str, Any]],
    output_path: str | Path,
) -> None:
    """
    Save function calling results to a JSON file.

    Args:
        results: List of generated function calling results.
        output_path: Destination path for the JSON file.

    Raises:
        OSError: If the output file cannot be written.
        TypeError: If the results cannot be serialized to JSON.
        ValueError: If the results contain invalid JSON values.
    """
    path = Path(output_path)

    path.parent.mkdir(parents=True, exist_ok=True)

    with path.open("w", encoding="utf-8") as file:
        json.dump(
            results,
            file,
            indent=2,
            ensure_ascii=False,
            allow_nan=False,
        )

        file.write("\n")
