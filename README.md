*This activity has been created as part of the 42 curriculum by sabu-kha.*

# Call Me Maybe

## Description

**Call Me Maybe** is a Python project that explores function calling with a language model using constrained decoding.

The application receives natural-language prompts and a set of function definitions. Its goal is to identify the appropriate function and generate parameters that match the function's expected schema.

For example:

**Input:**
```text
What is the sum of 40 and 2?
```

**Expected output:**
```json
{
  "prompt": "What is the sum of 40 and 2?",
  "name": "fn_add_numbers",
  "parameters": {
    "a": 40,
    "b": 2
  }
}
```

## Project Structure

```text
call_me_maybe/
├── data/
│   ├── input/
│   │   ├── functions_definition.json
│   │   └── function_calling_tests.json
│   └── output/
├── llm_sdk/
├── src/
│   ├── __init__.py
│   ├── __main__.py
│   ├── cli.py
│   ├── parser.py
│   ├── validator.py
│   ├── vocabulary.py
│   ├── llm_handler.py
│   ├── constrained_decoder.py
│   └── output.py
├── Makefile
├── pyproject.toml
├── uv.lock
└── README.md
```

## Instructions

### Requirements

- Python 3.10 or higher
- [uv](https://docs.astral.sh/uv/)
- Git

### Installation

Clone the repository:

```bash
git clone <repository-url>
cd call_me_maybe
```

Install dependencies:

```bash
make install
```

### Execution

Run the application:

```bash
make run
```

Or run it directly:

```bash
uv run python -m src
```

### Custom input files

The application supports custom file paths:

```bash
uv run python -m src \
  --functions_definition path/to/functions.json \
  --input path/to/tests.json \
  --output path/to/results.json
```

## Resources

- Python documentation: https://docs.python.org/3/
- Pydantic documentation: https://docs.pydantic.dev/
- NumPy documentation: https://numpy.org/doc/
- Hugging Face documentation: https://huggingface.co/docs
- uv documentation: https://docs.astral.sh/uv/

## Algorithm

The project is organized into separate modules:

1. **Parser:** Reads function definitions and test prompts from JSON files.
2. **Validator:** Checks that input data follows the expected structure and types.
3. **Vocabulary:** Provides token-to-ID and ID-to-token mappings.
4. **LLM Handler:** Provides an interface to the language model for encoding, decoding, and retrieving token logits.
5. **Constrained Decoder:** Responsible for guiding token generation according to the available function definitions and valid output structure.
6. **Output:** Saves generated function calls to a JSON file.

The intended decoding process uses the model's next-token scores and the allowed output structure to guide generation. The incremental token-filtering mechanism is still under development.

## Design Decisions

- **Modular architecture:** Each component has a specific responsibility.
- **Pydantic validation:** Used to validate input structures and function definitions.
- **JSON configuration:** Function definitions are stored separately from the application logic.
- **SDK abstraction:** Model operations are handled through the provided `llm_sdk` interface.
- **Type hints and documentation:** Used to improve readability and maintainability.

## Testing Strategy

The project uses the provided function definitions and test prompts to check:

- JSON input loading.
- Function definition validation.
- Test case validation.
- Vocabulary mapping.
- Function name validation.
- Parameter names and types.
- Complete function-call structure.
- JSON output generation.

The input dataset currently contains five function definitions and eleven test cases.

## Challenges

- Understanding how tokenization maps text to token IDs.
- Working with model logits to guide next-token generation.
- Designing a decoding mechanism that respects function schemas.
- Handling incomplete JSON prefixes during generation.
- Ensuring that generated parameters match the selected function definition.

## Performance Analysis

The project aims to generate valid function calls while maintaining accurate function selection and parameter extraction.

Performance will be evaluated using:

- Function selection accuracy.
- Parameter extraction accuracy.
- Output schema validity.
- Generation time.

Actual performance measurements will be added after the end-to-end implementation and evaluation.

## AI Usage

AI tools may be used as learning and development assistants to help understand concepts, review implementation decisions, and troubleshoot errors. The project implementation and technical decisions should be understood and reviewed by the project author.
