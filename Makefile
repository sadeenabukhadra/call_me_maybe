
.PHONY: install run debug clean lint lint-strict

# Install project dependencies
install:
	uv sync

# Run the main program
run:
	uv run python -m src

# Run the program in debug mode
debug:
	uv run python -m pdb -m src

# Remove temporary files and caches
clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type d -name ".mypy_cache" -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

# Run flake8 and mypy checks
lint:
	uv run flake8 .
	uv run mypy . --warn-return-any --warn-unused-ignores --ignore-missing-imports --disallow-untyped-defs --check-untyped-defs

# Run strict linting (optional)
lint-strict:
	uv run flake8 .
	uv run mypy . --strict
