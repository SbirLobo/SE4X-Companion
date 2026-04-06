"""Convert full_text fields in master_rule_book.py from single strings to lists.

Each line becomes a separate list entry.
Empty lines (from double newlines) become empty string entries.
"""
import re
from pathlib import Path

FILE = Path("app/data/master_rule_book.py")


def build_list(indent, text):
    lines = text.split("\n")

    # Strip leading and trailing empty lines
    while lines and not lines[0].strip():
        lines.pop(0)
    while lines and not lines[-1].strip():
        lines.pop()

    if not lines:
        return f"{indent}'full_text': [],"

    items = []
    for line in lines:
        if line.strip() == "":
            items.append(f'{indent}    """"""')
        else:
            # Escape trailing " to avoid creating """" (invalid syntax)
            stripped = line.rstrip('"')
            trailing = len(line) - len(stripped)
            if trailing:
                line = stripped + '\\"' * trailing
            items.append(f'{indent}    _("""{line}""")')

    return f"{indent}'full_text': [\n" + ",\n".join(items) + f",\n{indent}],"


def convert(content):
    return re.sub(
        r"( +)'full_text': _\(\"\"\"(.*?)\"\"\"\),",
        lambda m: build_list(m.group(1), m.group(2)),
        content,
        flags=re.DOTALL,
    )


if __name__ == "__main__":
    content = FILE.read_text()
    new_content = convert(content)

    changed = content.count("'full_text': _(")
    print(f"Entries converted: {changed}")

    FILE.write_text(new_content)
    print("Done.")
