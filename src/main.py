from copystatic import move_files
from generate_page import generate_page_recursive
import sys

def main():
    move_files("static", "docs")
    basepath = "/"
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    generate_page_recursive("content", "template.html", "docs", basepath)
main()