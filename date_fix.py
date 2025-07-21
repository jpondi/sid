import os
import re

folder = "j67"

for filename in os.listdir(folder):
    if not filename.endswith(".md"):
        continue

    path = os.path.join(folder, filename)
    with open(path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Fix front matter
    if lines[0].strip() == "---":
        for i in range(1, len(lines)):
            if lines[i].strip().startswith("date: "):
                telugu_date = lines[i].strip().split("date: ")[1]
                # Replace with ISO date based on filename
                iso_date = filename.replace(".md", "")  # from 2025-04-01.md
                lines[i] = f"date: {iso_date}\n"
                lines.insert(i + 1, f'telugu_date: "{telugu_date}"\n')
                break

    # Save
    with open(path, 'w', encoding='utf-8') as f:
        f.writelines(lines)

    print(f"✅ Fixed date in {filename}")
