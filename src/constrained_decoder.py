
"""Module responsible for validating generated function calls."""

from src.validator import FunctionDefinition


class ConstrainedDecoder:
    """Validate generated function calls against available definitions."""

    def __init__(
        self,
        function_definitions: list[FunctionDefinition],
    ) -> None:
        """
        Initialize the decoder with available function definitions.

        Args:
            function_definitions: Validated function definitions.
        """
        if not function_definitions:
            raise ValueError(
                "At least one function definition is required."
            )

        self.function_definitions = function_definitions

        self.function_names = {
            definition.name
            for definition in function_definitions
        }

    def is_valid_function_name(self, name: str) -> bool:
        """
        Check whether a function name is defined.

        Args:
            name: Function name to check.

        Returns:
            True if the function exists, otherwise False.
        """
        return name in self.function_names

    def is_valid_parameters(
        self,
        function_name: str,
        parameters: dict[str, object],
    ) -> bool:
        """
        Check whether parameters match a function definition.

        Args:
            function_name: Name of the function.
            parameters: Parameters supplied to the function.

        Returns:
            True if all parameter names and types are valid.
        """
        definition = next(
            (
                item
                for item in self.function_definitions
                if item.name == function_name
            ),
            None,
        )

        if definition is None:
            return False

        # Check that all required parameters exist
        # and that no extra parameters were provided.
        if set(parameters) != set(definition.parameters):
            return False

        for name, parameter_definition in definition.parameters.items():
            value = parameters[name]

            if parameter_definition.type == "number":
                # bool is a subclass of int in Python,
                # so we must explicitly reject it.
                if isinstance(value, bool) or not isinstance(
                    value, (int, float)
                ):
                    return False

            elif parameter_definition.type == "string":
                if not isinstance(value, str):
                    return False

        return True

    def is_valid_function_call(
        self,
        function_call: dict[str, object],
    ) -> bool:
        """
        Validate a complete generated function call.

        Args:
            function_call: Generated function call.

        Returns:
            True if the function call has the correct structure,
            function name, and parameters.
        """
        # A function call must contain exactly these two keys.
        if set(function_call) != {"name", "parameters"}:
            return False

        name = function_call["name"]
        parameters = function_call["parameters"]

        if not isinstance(name, str):
            return False

        if not isinstance(parameters, dict):
            return False

        # Check that the function exists.
        if not self.is_valid_function_name(name):
            return False

        # Check that its parameters match the definition.
        if not all(isinstance(key, str) for key in parameters):
            return False

        return self.is_valid_parameters(name, parameters)
