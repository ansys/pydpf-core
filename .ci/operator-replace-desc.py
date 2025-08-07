import os
import re

def extract_operator_description(content):
    match = re.search(r'## Description\s*(.*?)\s*(?=## |\Z)', content, re.DOTALL)
    return match.group(0) if match else None

def replace_operator_description(original, new_desc):
    return re.sub(r'## Description\s*.*?(?=## |\Z)', new_desc, original, flags=re.DOTALL)

def process_operator_files(root_directory):
    all_md_files = {}

    # Walk through the target directory and all subdirectories
    for root, _, files in os.walk(root_directory):
        for file in files:
            if file.endswith('.md'):
                full_path = os.path.join(root, file)
                all_md_files[full_path] = file  # Store full path and just filename

    for base_path, file_name in all_md_files.items():
        if file_name.endswith('_upd.md'):
            continue  # Skip update files

        # Construct the expected update file name and path
        name_wo_ext = file_name[:-3]
        upd_file_name = f"{name_wo_ext}_upd.md"

        # Look for the update file in the same folder
        upd_path = os.path.join(os.path.dirname(base_path), upd_file_name)
        if not os.path.exists(upd_path):
            print(f"❌ No update file found for: {base_path}")
            continue

        # Load contents
        with open(base_path, 'r', encoding='utf-8') as bf:
            base_content = bf.read()
        with open(upd_path, 'r', encoding='utf-8') as uf:
            upd_content = uf.read()

        # Extract and replace description
        new_description = extract_operator_description(upd_content)
        if new_description:
            updated_content = replace_operator_description(base_content, new_description)
            with open(base_path, 'w', encoding='utf-8') as bf:
                bf.write(updated_content)
            print(f"✅ Updated: {base_path}")
        else:
            print(f"⚠️ No 'operator_description' found in: {upd_path}")

# Run the script on doc/source/operators_doc
process_operator_files('doc/source/operators_doc')
