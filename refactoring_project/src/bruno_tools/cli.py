from bruno_tools.csv_utils import export_rows_by_status


def main():
    src_filename = input("Enter source filename: ")
    dst_filename = input("Enter destination filename: ")
    status = input("Enter status: ")

    try:
        src_filename = "tests\\data\\" + str(src_filename)
        dst_filename = "tests\\data\\" + str(dst_filename)
        exported_rows = export_rows_by_status(src_filename, dst_filename, status)
        print(f"Exported {exported_rows} rows.")
    except FileNotFoundError:
        print("File not found.")


if __name__ == "__main__":
    main()
