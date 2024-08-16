import os
from markdown_to_html_node import markdown_to_html_node
from extract_title import extract_title

def find_markdown_files(path):
    directories = os.listdir(path)
    paths = []
    for directory in directories:
        next_path = f"{path}{directory}"
        if is_file(next_path):
            if is_markdown_file(next_path):
                paths.append(next_path)
        else:
            new_files = find_markdown_files(f"{next_path}/")
            paths += new_files
    return paths

def is_file(path):
    return os.path.isfile(path)

def is_markdown_file(path):
    return is_file(path) and path.endswith(".md")

def generate_page(from_path, template_path, to_path):
    print(f"Generating page from {from_path} to {to_path} using {template_path}")
    from_file = open(from_path)
    from_content = from_file.read()
    from_file.close()
    template_file = open(template_path)
    template_content = template_file.read()
    template_file.close()
    title = extract_title(from_content)
    html_node = markdown_to_html_node(from_content)
    final_content = template_content.replace("{{ Title }}", title)
    final_content = final_content.replace("{{ Content }}", html_node.to_html())
    create_directories(to_path)
    to_file = open(to_path, 'w')
    to_file.write(final_content)
    to_file.close()

def create_directories(path):
    start = path.rsplit('/', 1)[0]
    if not os.path.exists(start):
        os.makedirs(start)

def generate_pages_recursively(content_dir_path, template_path, destination_dir_path):
    md_file_paths = find_markdown_files(content_dir_path)
    for content_path in md_file_paths:
        destination_path = content_path.replace(content_dir_path, destination_dir_path)
        destination_file_path = destination_path.replace(".md", ".html")
        generate_page(content_path, template_path, destination_file_path)
