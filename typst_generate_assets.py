import subprocess
import csv
from pathlib import Path

TYPST_TEMPLATE_STRING = "\n".join(
    [
        r"#set page(width: auto, height: auto, margin: 0em, fill: none)",
        r"#circle(radius: 12pt, fill: eval(sys.inputs.c))",
    ]
)


def convert_oklch_css2typst(css_oklch):
    return css_oklch.replace(" ", ",")


def typst_compile(typst_oklch, output_filename):
    subprocess.run(
        [
            "typst",
            "compile",
            "--input",
            f"c={typst_oklch}",
            "-",
            output_filename,
        ],
        input=TYPST_TEMPLATE_STRING.encode(),
    )


def main():
    lettepa_csv_path = Path("lettepa.csv")
    if not lettepa_csv_path.exists():
        print("lettepa.csv not found")
        return

    output_dir = Path("assets")
    output_dir.mkdir(exist_ok=True, parents=True)

    with open("lettepa.csv", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            css_oklch = row["oklch"]
            typst_oklch = convert_oklch_css2typst(css_oklch)
            name = row["name"].replace("ü", "v")
            output_filename = output_dir / f"{name}.svg"
            print(f"Generating {output_filename}")
            typst_compile(typst_oklch, output_filename)


if __name__ == "__main__":
    main()
