import os
import shutil

from blocks import markdown_to_html_node
from utils import extract_title

def copy_files_recursive(source_dir_path, dest_dir_path):
    if not os.path.exists(dest_dir_path):
        os.mkdir(dest_dir_path)

    for filename in os.listdir(source_dir_path):
        from_path = os.path.join(source_dir_path, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        print(f" * {from_path} -> {dest_path}")
        if os.path.isfile(from_path):
            shutil.copy(from_path, dest_path)
        else:
            copy_files_recursive(from_path, dest_path)

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}.")

    with open(from_path, 'r') as markdown_file:
        markdown_content = markdown_file.read()

    print(markdown_content, flush=True)

    with open (template_path, 'r') as template_file:
        template_content = template_file.read()
    print(template_content)
    html_node = markdown_to_html_node(markdown_content)
    html_content = html_node.to_html()

    print(html_content, flush=True)

    title = extract_title(markdown_content)

    final_html = template_content.replace("{{ Title }}", title).replace("{{ Content }}", html_content)

    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    with open(dest_path, 'w') as dest_file:
        dest_file.write(final_html)