import os
import re

input_folder = "_devotionals"

for filename in os.listdir(input_folder):
    if not filename.endswith(".md"):
        continue

    path = os.path.join(input_folder, filename)
    try:
        with open(path, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        # Separate front matter and body
        if lines[0].strip() == "---":
            end_index = None
            for i in range(1, len(lines)):
                if lines[i].strip() == "---":
                    end_index = i
                    break
            if end_index is None:
                raise ValueError("Front matter not closed with '---'")

            front_matter = lines[:end_index + 1]
            body_lines = lines[end_index + 1:]
        else:
            front_matter = []
            body_lines = lines

        # Remove devotional header block lines
        cleaned_body = []
        for line in body_lines:
            stripped = line.strip()
            if "విశ్వాసాన్ని పెంపొందించే అనుదిన ధ్యానములు" in stripped:
                continue
            elif "⭐" in stripped and "*" in stripped:
                continue
            elif any(sym in stripped for sym in ["╭", "╰", "═══", "➖"]):
                continue
            else:
                cleaned_body.append(line)

        # Convert *text* to **text**, but preserve ***text*** and **text**
        def convert_asterisks(text):
            return re.sub(r'(?<!\*)\*(?!\*)([^*\n]+?)\*(?!\*)', r'**\1**', text)

        cleaned_body = [convert_asterisks(line) for line in cleaned_body]

        # Write back to the file
        with open(path, 'w', encoding='utf-8') as f:
            f.writelines(front_matter + cleaned_body)

        print(f"✅ Cleaned {filename}")

    except Exception as e:
        print(f"❌ Error with {filename}: {e}")
