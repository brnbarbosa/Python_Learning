import csv


def totals_by_status(path: str) -> dict[str, int]:
    with open(path, "r", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)

        fieldnames = reader.fieldnames
        if fieldnames is None or "status" not in fieldnames:
            raise ValueError('CSV must contain a "status" column')

        count: dict[str, int] = {}
        for row in reader:
            status = row["status"].strip().lower()
            count[status] = count.get(status, 0) + 1

        return count


def export_rows_by_status(src: str, dst: str, status: str) -> int:
    with open(src, "r", encoding="utf-8") as src_f:
        with open(dst, "w", encoding="utf-8", newline="") as dst_f:
            reader = csv.DictReader(src_f)
            field_names = reader.fieldnames
            if field_names is None or "status" not in field_names:
                raise ValueError('CSV must contain a "status" column')

            writer = csv.DictWriter(dst_f, fieldnames=field_names)
            writer.writeheader()

            target_status = status.strip().lower()
            exported_count: int = 0
            for row in reader:
                if row["status"].strip().lower() == target_status:
                    exported_count += 1
                    writer.writerow(row)

            return exported_count
