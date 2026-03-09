from bruno_tools.csv_utils import export_rows_by_status, totals_by_status


def main():
    testing_export()
    testing_totals()


def testing_export():
    result = export_rows_by_status(
        src="refactoring_project/tests/data/sales.csv",
        dst="refactoring_project/tests/data/paid_sales.csv",
        status="paid",
    )
    expected = 2

    print("Exported rows:", result)
    assert result == expected, f"Expected {expected}, got {result}"
    print("PASS")


def testing_totals():
    result = totals_by_status("refactoring_project/tests/data/sales.csv")
    expected = {"paid": 2, "open": 1, "overdue": 1, "canceled": 1}

    print("Result:", result)
    assert result == expected, f"Expected {expected}, got {result}"
    print("PASS")


if __name__ == "__main__":
    main()
