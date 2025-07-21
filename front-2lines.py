import os

input_folder = "j67"

for filename in os.listdir(input_folder):
    if not filename.endswith(".md"):
        continue

    path = os.path.join(input_folder, filename)

    try:
        with open(path, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        # Identify front matter end (second '---')
        if lines[0].strip() == "---":
            end_index = None
            for i in range(1, len(lines)):
                if lines[i].strip() == "---":
                    end_index = i
                    break
            if end_index is None:
                raise ValueError("Missing closing '---' in front matter.")

            # Find up to 3 blank lines after front matter
            body_start = end_index + 1
            blank_lines = 0
            while body_start + blank_lines < len(lines) and lines[body_start + blank_lines].strip() == '' and blank_lines < 3:
                blank_lines += 1

            # Remove only the first 2 blank lines
            to_skip = min(blank_lines, 2)
            cleaned_lines = lines[:end_index + 1] + lines[body_start + to_skip:]

            with open(path, 'w', encoding='utf-8') as f:
                f.writelines(cleaned_lines)

            print(f"✅ Trimmed blank lines in {filename}")
        else:
            print(f"⚠️ No front matter found in {filename}, skipped.")

    except Exception as e:
        print(f"❌ Error processing {filename}: {e}")
