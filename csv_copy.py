import csv


def main():
    src_prompt = "Enter the source csv file name: "
    out_prompt = "Enter the output csv file name: "
    exported_rows = export_paid_rows(src_prompt, out_prompt)
    print(f"Exported {exported_rows} paid rows.")


def export_paid_rows(src_prompt, out_prompt) -> int:
    src_csv_file = input(src_prompt)
    out_csv_file = input(out_prompt)
    with open(src_csv_file, encoding="utf-8") as src_file:
        with open(out_csv_file, "w", newline="") as out_file:
            reader = csv.DictReader(src_file)
            assert reader.fieldnames is not None
            field_names = reader.fieldnames
            writer = csv.DictWriter(out_file, fieldnames=list(field_names))
            writer.writeheader()

            count: int = 0
            for row in reader:
                if row["status"].strip().lower() == "paid":
                    writer.writerow(row)
                    count += 1

    return count


if __name__ == "__main__":
    main()
