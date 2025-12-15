import os
import shutil

from gen_content import generate_page, generate_pages_recursive
from static_copy import static_copy

source_path = "./static"
dest_path = "./public"
dir_path_content = "./content"
template_path = "./template.html"


def main():
    if os.path.exists(dest_path):
        print("Deleting public dir")
        shutil.rmtree(dest_path)

    print("Copying...")
    static_copy(source_path, dest_path)

    print("Generating page...")
    generate_pages_recursive(dir_path_content, template_path, dest_path)

if __name__ == "__main__":
    main()
