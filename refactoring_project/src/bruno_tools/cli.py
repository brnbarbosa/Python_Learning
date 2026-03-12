from pathlib import Path

from bruno_tools.csv_utils import export_rows_by_status

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "tests" / "data"
TMP = ROOT / "tests" / "tmp"
TMP.mkdir(exist_ok=True)


def resolve_input_path(user_text: str, base_dir: Path) -> Path:
    p = Path(user_text).expanduser()
    if p.is_absolute():
        return p
    return base_dir / p


def main():
    src_filename = input("Enter source filename: ")
    src_path = resolve_input_path(src_filename, DATA).resolve()

    dst_filename = input("Enter destination filename: ")
    dst_path = resolve_input_path(dst_filename, TMP).resolve()

    status = input("Enter status: ")

    mode = input("Enter the mode (export/report):").strip().lower()
    if mode == "export":
        try:
            exported_rows = export_rows_by_status(str(src_path), str(dst_path), status)
            print(f"Exported {exported_rows} rows.")
        except FileNotFoundError:
            print(f"File not found: {src_path}.")
            print(f"CWD: {Path.cwd()}.")
            print(f"Tried: {src_path}.")
    elif mode == "report":
        pass
    else:
        print("Select a valid mode (export/report)")


if __name__ == "__main__":
    main()
