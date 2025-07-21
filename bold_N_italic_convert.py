import os
import re

# Change this to the path where your devotional text files are stored
folder_path = "j67"

# Regex pattern to match _*text*_ and convert to ***text***
pattern = re.compile(r'_\*(.*?)\*_')

# Loop through all .txt files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith(".md"):
        filepath = os.path.join(folder_path, filename)
        with open(filepath, "r", encoding="utf-8") as file:
            content = file.read()

        # Replace _*text*_ with ***text***
        new_content = pattern.sub(r'***\1***', content)

        # Write back to the same file or a new one
        with open(filepath, "w", encoding="utf-8") as file:
            file.write(new_content)

        print(f"Converted formatting in {filename}")
