import re
from pathlib import Path

def boldify_asterisks(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Convert *text* to **text**, but skip already bold or italic (like **bold** or ***bold italic***)
    # This uses a negative lookahead to avoid ** or *** inside
    def replacer(match):
        text = match.group(1)
        return f"**{text}**"

    # Replace only *text* that is not already part of ** or ***
    # Pattern explanation:
    # (?<!\*)\*([^*]+)\*(?!\*)  → Matches *something* not preceded or followed by *
    new_content = re.sub(r'(?<!\*)\*([^*\n]+?)\*(?!\*)', replacer, content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

    print(f"✔ Updated: {filepath.name}")

# === Main block: Process all .md files in j67/ folder ===
folder = Path('j67')
for file in folder.glob('*.md'):
    boldify_asterisks(file)
