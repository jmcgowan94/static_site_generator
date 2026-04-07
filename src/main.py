from copystatic import move_files
from generate_page import generate_page, generate_page_recursive

def main():
    move_files("static", "public")
    # generate_page("content/index.md", "template.html", "public/index.html")
    generate_page_recursive("content", "template.html", "public")

main()