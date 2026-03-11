import csv
from pathlib import Path

from bruno_tools.csv_utils import export_rows_by_status, totals_by_status

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "tests" / "data"
TMP = ROOT / "tests" / "tmp"
TMP.mkdir(exist_ok=True)

sales_csv = DATA / "sales.csv"
no_status_csv = DATA / "no_status.csv"
paid_out_csv = TMP / "paid_sales.csv"


def main():
    testing_export()
    testing_totals()


def testing_export():

    result_exported_rows = export_rows_by_status(
        src=str(sales_csv),
        dst=str(paid_out_csv),
        status="paid",
    )
    expected_exported_rows = 2

    print("Exported rows:", result_exported_rows)
    assert result_exported_rows == expected_exported_rows, (
        f"Expected {expected_exported_rows}, got {result_exported_rows}"
    )
    print("PASS")

    with open(str(paid_out_csv), "r", encoding="utf-8") as test_f:
        reader = csv.DictReader(test_f)

        result_header = reader.fieldnames
        expected_header = ["date", "client", "invoice_id", "amount", "status"]
        print("Result header test: ", result_header)
        assert result_header == expected_header, (
            f"Expected {expected_header}, got {result_header}"
        )
        print("PASS")

        result_exported_count = 0
        for row in reader:
            assert row["status"].strip().lower() == "paid"
            result_exported_count += 1

        print("Result paid rows: ", result_exported_count)
        assert result_exported_count == result_exported_rows, (
            f"Expected {result_exported_rows}, got {result_exported_count}"
        )
        print("PASS")

    try:
        export_rows_by_status(
            src=str(no_status_csv),
            dst=str(paid_out_csv),
            status="paid",
        )
        assert False, "Expected ValueError"
    except ValueError as e:
        print(e)
        assert str(e) == 'CSV must contain a "status" column'
        print("PASS")


def testing_totals():
    result = totals_by_status(str(sales_csv))
    expected = {"paid": 2, "open": 1, "overdue": 1, "canceled": 1}

    print("Result:", result)
    assert result == expected, f"Expected {expected}, got {result}"
    print("PASS")

    try:
        totals_by_status(str(no_status_csv))
        assert False, "Expected ValueError"
    except ValueError as e:
        print(e)
        assert str(e) == 'CSV must contain a "status" column'
        print("PASS")


if __name__ == "__main__":
    main()
