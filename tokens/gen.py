import json
import os
import shutil

# Define the base structure of the JSON
base_structure = {
    "id": 1,
    "image": "https://www.unchainedguild.xyz/unchained_logo.webp",
    "token_id": "1",
    "background_color": None,
    "animation_url": None,
    "youtube_url": None,
    "name": "Unchained Member Token",
    "description": "Unchained on-chain.",
    "external_url": "https://www.unchainedguild.xyz",
    "attributes": []
}

# Directory to store files
output_dir = "unchained_files"
os.makedirs(output_dir, exist_ok=True)

# Generate JSON files with sequential id and token_id
for i in range(1, 1001):
    structure = base_structure.copy()
    structure["id"] = i
    structure["token_id"] = str(i)

    # Save each file without an extension
    with open(f"{output_dir}/{i}", "w") as file:
        json.dump(structure, file, indent=2)

# Create a zip file of the directory
shutil.make_archive("unchained_member_tokens", 'zip', output_dir)

print("Zip file 'unchained_member_tokens.zip' has been created with 1000 files.")
