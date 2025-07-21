import os
from datetime import datetime

# Map month abbreviations to numbers
month_map = {
    'Jan': '01', 'Feb': '02', 'Mar': '03', 'Apr': '04',
    'May': '05', 'June': '06', 'July': '07', 'Aug': '08',
    'Sep': '09', 'Oct': '10', 'Nov': '11', 'Dec': '12'
}

input_folder = "./raw2"  # where your Apr01.txt etc. are
output_folder = "j67"  # adjust this as needed

os.makedirs(output_folder, exist_ok=True)

for mon_abbr, mon_num in month_map.items():
    for day in range(1, 32):
        filename = f"{mon_abbr}{day:02d}.txt"
        input_path = os.path.join(input_folder, filename)

        if not os.path.exists(input_path):
            continue  # skip invalid dates

        try:
            with open(input_path, 'r', encoding='utf-8') as f:
                content = f.read().strip()

            # Try to extract title (e.g., between stars ⭐)
            title_line = next((line for line in content.splitlines() if '⭐' in line), "Devotional")
            title = title_line.replace('⭐', '').strip('* ').strip()

            # Compose date in YYYY-MM-DD
            try:
                date_str = f"2025-{mon_num}-{day:02d}"
                datetime.strptime(date_str, '%Y-%m-%d')  # validate
            except ValueError:
                continue

            # Create front matter
            front_matter = f"""---
title: "{title}"
date: {date_str}
layout: devotional
lang: te
---
"""

            output_filename = f"{date_str}.md"
            output_path = os.path.join(output_folder, output_filename)

            with open(output_path, 'w', encoding='utf-8') as out:
                out.write(front_matter + "\n" + content.strip())

            print(f"✅ Converted {filename} → {output_filename}")

        except Exception as e:
            print(f"❌ Error with {filename}: {e}")
