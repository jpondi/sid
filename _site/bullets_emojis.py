import os
import re

input_folder = "j67"

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

        final_body = []
        scripture_found = False

        for line in body_lines:
            stripped = line.strip()

            # Insert 📖 after ** or *** in first bold scripture line only
            if not scripture_found and (stripped.startswith('**') or stripped.startswith('***')):
                match = re.match(r'^(\*{2,3})([^*].*?)\1$', stripped)
                if match:
                    stars, content = match.groups()
                    new_line = f"{stars}📖{content}{stars}\n"
                    final_body.append(new_line)
                    scripture_found = True
                    continue

            # Convert lines starting with 🔹 or 🔸 into - 🔹 ... format
            if stripped.startswith('🔹') or stripped.startswith('🔸'):
                final_body.append(f"- {stripped}\n")
                continue

            # Everything else remains the same
            final_body.append(line)

        # Write updated content back to the file
        with open(path, 'w', encoding='utf-8') as f:
            f.writelines(front_matter + final_body)

        print(f"✅ Cleaned {filename}")

    except Exception as e:
        print(f"❌ Error with {filename}: {e}")
