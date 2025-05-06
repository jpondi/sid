import os
from datetime import datetime

# Map month abbreviations to numbers
month_map = {
    'Jan': '01', 'Feb': '02', 'Mar': '03', 'Apr': '04',
    'May': '05', 'Jun': '06', 'Jul': '07', 'Aug': '08',
    'Sep': '09', 'Oct': '10', 'Nov': '11', 'Dec': '12'
}

# Telugu month names
telugu_months = {
    '01': 'జనవరి', '02': 'ఫిబ్రవరి', '03': 'మార్చి', '04': 'ఏప్రిల్',
    '05': 'మే', '06': 'జూన్', '07': 'జూలై', '08': 'ఆగస్టు',
    '09': 'సెప్టెంబర్', '10': 'అక్టోబర్', '11': 'నవంబర్', '12': 'డిసెంబర్'
}

input_folder = "./raw2"  # where your Apr01.txt etc. are
output_folder = "_devotionals"  # adjust this as needed

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

            # Compose date in Telugu format (e.g., ఏప్రిల్ 1)
            telugu_month = telugu_months[mon_num]
            telugu_date = f"{telugu_month} {day}"

            # Create front matter
            front_matter = f"""---
title: "{title}"
date: {telugu_date}
layout: devotional
lang: te
---
"""

            output_filename = f"{mon_abbr}{day:02d}.md"
            output_path = os.path.join(output_folder, output_filename)

            with open(output_path, 'w', encoding='utf-8') as out:
                out.write(front_matter + "\n" + content.strip())

            print(f"✅ Converted {filename} → {output_filename}")

        except Exception as e:
            print(f"❌ Error with {filename}: {e}")
