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

        final_body = []
        for line in body_lines:
            stripped = line.strip()

            if stripped == "**దైవాశ్శీసులు!!!**":
                final_body.append('<div class="blessing">🙏 <span class="bless-text">దైవాశ్శీసులు!!!</span> ✨</div>\n')
            elif "సంకలనం" in stripped:
                final_body.append('<div class="credit">✍️ <span class="credit-text">▪ సంకలనం - చార్లెస్ ఇ. కౌమన్</span></div>\n')
            elif "అనువాదం" in stripped:
                final_body.append('<div class="credit">🌐 <span class="credit-text">▪ అనువాదం - డా. జోబ్ సుదర్శన్</span></div>\n')
            elif "మీ మిత్రులకు share" in stripped:
                final_body.append('<div class="share">📤 👉 <span class="share-text">మీ మిత్రులకు share చేసి మీ వంతుగా దేవుని పని చేయండి.</span></div>\n')
            else:
                final_body.append(line)

        # Write updated content back to the file
        with open(path, 'w', encoding='utf-8') as f:
            f.writelines(front_matter + final_body)

        print(f"✅ Cleaned {filename}")

    except Exception as e:
        print(f"❌ Error with {filename}: {e}")
