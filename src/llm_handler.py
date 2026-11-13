
"""Module responsible for interacting with the language model."""

from llm_sdk import Small_LLM_Model


class LLMHandler:
    """Provide an interface to the language model."""

    def __init__(
        self,
        model_name: str = "Qwen/Qwen3-0.6B",
    ) -> None:
        """Initialize the language model."""
        self._model = Small_LLM_Model(model_name)

    def encode(self, text: str) -> list[int]:
        """
        Convert text into a list of token IDs.

        Args:
            text: Input text.

        Returns:
            A list of token IDs.

        Raises:
            ValueError: If the input text is empty.
        """
        if not text.strip():
            raise ValueError("Input text cannot be empty.")

        encoded = self._model.encode(text)

        return [int(token_id) for token_id in encoded[0].tolist()]

    def decode(self, token_ids: list[int]) -> str:
        """
        Convert token IDs back into text.

        Args:
            token_ids: A list of token IDs.

        Returns:
            The decoded text.
        """
        return self._model.decode(token_ids)

    def get_logits(self, token_ids: list[int]) -> list[float]:
        """
        Get the next-token logits from the language model.

        Args:
            token_ids: The input token IDs.

        Returns:
            A list of scores, one for each vocabulary token.

        Raises:
            ValueError: If the token list is empty.
        """
        if not token_ids:
            raise ValueError("Token IDs cannot be empty.")

        return self._model.get_logits_from_input_ids(token_ids)
