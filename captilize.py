import os

folder = "_en_md"

for filename in os.listdir(folder):
    if filename.endswith(".md"):
        new_filename = filename.capitalize()
        old_path = os.path.join(folder, filename)
        new_path = os.path.join(folder, new_filename)
        if old_path != new_path:
            os.rename(old_path, new_path)

print("✅ Filenames capitalized.")