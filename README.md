# Python Learning Exercises

A small collection of beginner-friendly Python practice scripts focused on:

- Lists and loops
- List comprehensions and lambda sorting
- Dictionaries
- Input validation
- File reading and writing
- CSV reading, filtering, and aggregation
- Refactoring into a small reusable package

## Project Structure

Most beginner scripts now live under `exercises/`:

- `exercises/list_get_positive_append.py`: asks for a positive number, builds a list from `1..n`, and prints the sum.
- `exercises/list_parsing_input.py`: parses space-separated integers and prints count, sum, min, and max.
- `exercises/list_comp.py`: normalization and filtering examples with list comprehensions.
- `exercises/lambda_sorting.py`: sorting tuples with a lambda key (descending count, ascending name).
- `exercises/lambda_listcomp.py`: returns top-k statuses using sorting + list comprehension and validation.
- `exercises/dict_basic.py`: dictionary lookup example for a fixed item.
- `exercises/dict_loop.py`: loops through dictionary items and prints each key/value pair.
- `exercises/dict_lookup_user_input.py`: user-driven dictionary lookup with "not found" handling.
- `exercises/func_valid_input.py`: reusable integer input validation loop.
- `exercises/func_get_price.py`: function-based dictionary lookup using `dict.get()`.
- `exercises/file_read.py`: counts lines in a file with `FileNotFoundError` handling.
- `exercises/file_write_append.py`: appends user-provided text to a file.
- `exercises/file_reading_and_writing.py`: copies content from a source file to a destination file.
- `exercises/csv_basics.py`: reads a CSV file, skips the header, and counts data rows.
- `exercises/csv_count_row_condition.py`: counts rows where `status` is `paid` using `csv.DictReader`.
- `exercises/csv_total_by_status.py`: computes totals grouped by invoice status (`paid`, `open`, `overdue`).
- `exercises/csv_reusing_total_by_status.py`: imports and reuses `totals_by_status()` from another module.
- `exercises/csv_copy.py`: copies only `paid` rows from a source CSV into a new output CSV.
- `exercises/data.txt` / `exercises/new_data.txt`: sample text files for file I/O practice.
- `exercises/sales.csv` / `exercises/copy_sales.csv`: sample CSV files for CSV practice scripts.

## Refactoring Project

`refactoring_project/` contains an in-progress package refactor using a `src/` layout:

- `pyproject.toml`: project metadata for `bruno-tools`.
- `src/bruno_tools/csv_utils.py`: reusable CSV helpers (`totals_by_status`, `export_rows_by_status`).
- `src/bruno_tools/cli.py`: small command-line entry script for exporting rows by status.
- `src/bruno_tools/reporting.py`: reusable `top_statuses()` helper.
- `src/bruno_tools/__init__.py`: package marker.
- `scripts/status_report.py` and `scripts/export_paid.py`: placeholders for CLI scripts.
- `tests/`: script-based checks plus CSV fixtures under `tests/data/`.

## Requirements

- Python 3.10+ recommended (type hints use `int | None`)

## Run Any Script

From this folder:

```bash
python script_name.py
```

Example:

```bash
python exercises/list_parsing_input.py
```

## Learning Notes

This repository is intentionally simple and focused on core fundamentals before moving to larger projects.
