from bruno_tools.csv_utils import export_rows_by_status


def main():
    result = export_rows_by_status(
        src="tests/data/sales.csv",
        dst="tests/data/paid_sales.csv",
        status="paid",
    )
    expected = 2

    print("Exported rows:", result)
    assert result == expected, f"Expected {expected}, got {result}"
    print("PASS")


if __name__ == "__main__":
    main()
