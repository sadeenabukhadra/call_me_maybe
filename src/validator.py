
"""Module responsible for validating input data."""

from typing import Any, Literal

from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class TestCase(BaseModel):
    """Represent and validate a function calling test case."""

    model_config = ConfigDict(str_strip_whitespace=True)

    prompt: str = Field(min_length=1)


class ParameterDefinition(BaseModel):
    """Represent a function parameter definition."""

    type: Literal["number", "string"]


class ReturnDefinition(BaseModel):
    """Represent a function return definition."""

    type: Literal["number", "string"]


class FunctionDefinition(BaseModel):
    """Represent and validate a function definition."""

    name: str = Field(min_length=1)
    description: str = Field(min_length=1)
    parameters: dict[str, ParameterDefinition]
    returns: ReturnDefinition


def validate_test_cases(data: Any) -> list[TestCase]:
    """
    Validate a list of function calling test cases.

    Args:
        data: Raw test case data loaded from a JSON file.

    Returns:
        A list of validated TestCase objects.

    Raises:
        ValidationError: If the data does not match the expected structure.
    """
    adapter = TypeAdapter(list[TestCase])
    return adapter.validate_python(data)


def validate_function_definitions(
    data: Any
) -> list[FunctionDefinition]:
    """
    Validate a list of function definitions.

    Args:
        data: Raw function definitions loaded from a JSON file.

    Returns:
        A list of validated FunctionDefinition objects.

    Raises:
        ValidationError: If the data does not match the expected structure.
    """
    adapter = TypeAdapter(list[FunctionDefinition])
    return adapter.validate_python(data)
