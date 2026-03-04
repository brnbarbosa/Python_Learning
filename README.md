# Python Learning Exercises

A small collection of beginner-friendly Python practice scripts focused on:

- Lists and loops
- Dictionaries
- Input validation
- File reading and writing
- CSV reading, filtering, and aggregation

## Project Structure

- `list_get_positive_append.py`: asks for a positive number, builds a list from `1..n`, and prints the sum.
- `list_parsing_input.py`: parses space-separated integers and prints count, sum, min, and max.
- `dict_basic.py`: dictionary lookup example for a fixed item.
- `dict_loop.py`: loops through dictionary items and prints each key/value pair.
- `dict_lookup_user_input.py`: user-driven dictionary lookup with "not found" handling.
- `func_valid_input.py`: reusable integer input validation loop.
- `func_get_price.py`: function-based dictionary lookup using `dict.get()`.
- `file_read.py`: counts lines in a file with `FileNotFoundError` handling.
- `file_write_append.py`: appends user-provided text to a file.
- `file_reading_and_writing.py`: copies content from a source file to a destination file.
- `csv_basics.py`: reads a CSV file, skips the header, and counts data rows.
- `csv_count_row_condition.py`: counts rows where `status` is `paid` using `csv.DictReader`.
- `csv_total_by_status.py`: computes totals grouped by invoice status (`paid`, `open`, `overdue`).
- `csv_reusing_total_by_status.py`: imports and reuses `totals_by_status()` from another module.
- `csv_copy.py`: copies only `paid` rows from a source CSV into a new output CSV.
- `data.txt` / `new_data.txt`: sample text files for file I/O practice.
- `sales.csv` / `copy_sales.csv`: sample CSV files for CSV practice scripts.

## Requirements

- Python 3.10+ recommended (type hints use `int | None`)

## Run Any Script

From this folder:

```bash
python script_name.py
```

Example:

```bash
python list_parsing_input.py
```

## Learning Notes

This repository is intentionally simple and focused on core fundamentals before moving to larger projects.
