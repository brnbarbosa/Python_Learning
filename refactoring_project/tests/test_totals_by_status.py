from bruno_tools.csv_utils import totals_by_status


def main():
    result = totals_by_status("tests/data/sales.csv")
    expected = {"paid": 2, "open": 1, "overdue": 1, "canceled": 1}

    print("Result:", result)
    assert result == expected, f"Expected {expected}, got {result}"
    print("PASS")


if __name__ == "__main__":
    main()
