import csv_total_by_status


def main():
    counts = csv_total_by_status.totals_by_status("Enter csv file name: ")
    sorted_counts = sorted(counts.items(), key=lambda item: (-item[1], item[0]))
    for status, count in sorted_counts:
        print(f"{status}: {count}")


if __name__ == "__main__":
    main()
