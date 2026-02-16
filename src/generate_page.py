from markdown_blocks import extract_title, markdown_to_html_node
import os


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path}, to {dest_path} using {template_path}")
    with open(from_path, "r") as f:
        markdown = f.read()
    with open(template_path, "r") as f:
        template = f.read()
    title = extract_title(markdown)
    markdown_html = markdown_to_html_node(markdown).to_html()
    webpage_html = template.replace("{{ Title }}", title).replace("{{ Content }}", markdown_html)
    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
    with open(dest_path, "w") as f:
        f.write(webpage_html)