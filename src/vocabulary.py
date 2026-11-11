
"""Module responsible for loading and accessing the model vocabulary."""

import json
from pathlib import Path
from typing import Any

from pydantic import BaseModel, ConfigDict, model_validator


class Vocabulary(BaseModel):
    """Represent a tokenizer vocabulary and its token IDs."""

    model_config = ConfigDict(strict=True)

    token_to_id: dict[str, int]

    @model_validator(mode="after")
    def validate_unique_ids(self) -> "Vocabulary":
        """Ensure that each token ID belongs to only one token."""
        ids = list(self.token_to_id.values())

        if len(ids) != len(set(ids)):
            raise ValueError("Vocabulary contains duplicate token IDs.")

        return self

    @property
    def id_to_token(self) -> dict[int, str]:
        """Return a mapping from token IDs to tokens."""
        return {
            token_id: token
            for token, token_id in self.token_to_id.items()
        }

    def get_token_id(self, token: str) -> int | None:
        """Return the ID of a token, or None if it does not exist."""
        return self.token_to_id.get(token)

    def get_token(self, token_id: int) -> str | None:
        """Return the token for an ID, or None if it does not exist."""
        return self.id_to_token.get(token_id)


def load_vocabulary(file_path: str | Path) -> Vocabulary:
    """Load and validate a vocabulary JSON file."""
    path = Path(file_path)

    try:
        with path.open("r", encoding="utf-8") as file:
            data: Any = json.load(file)

    except FileNotFoundError:
        raise FileNotFoundError(
            f"Vocabulary file not found: {path}"
        ) from None

    except json.JSONDecodeError as error:
        raise ValueError(
            f"Invalid vocabulary JSON in {path}: {error}"
        ) from error

    if not isinstance(data, dict):
        raise ValueError("Vocabulary JSON must contain an object.")

    return Vocabulary(token_to_id=data)
