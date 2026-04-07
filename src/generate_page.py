from markdown_blocks import extract_title, markdown_to_html_node
import os

def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path}, to {dest_path} using {template_path}")
    with open(from_path, "r") as f:
        markdown = f.read()
    with open(template_path, "r") as f:
        template = f.read()
    title = extract_title(markdown)
    markdown_html = markdown_to_html_node(markdown).to_html()
    webpage_html = (
        template
        .replace("{{ Title }}", title)
        .replace("{{ Content }}", markdown_html)
        .replace('href="/', f'href="{basepath}')
        .replace('src="/', f'src="{basepath}')
    )
    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
    with open(dest_path, "w") as f:
        f.write(webpage_html)

def generate_page_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    content_list = os.listdir(dir_path_content)
    for item in content_list:
        item_path = os.path.join(dir_path_content, item)
        dest_path = os.path.join(dest_dir_path, item)
        if os.path.splitext(item_path)[1] == ".md":
            dest_path = dest_path[:-2]
            dest_path += "html"
            generate_page(item_path, template_path, dest_path, basepath)
        elif os.path.isdir(item_path):
            generate_page_recursive(item_path, template_path, dest_path, basepath)