import os
import shutil
from textnode import TextNode
from generate_page import generate_pages_recursively

def main():
    copy_static_to_public()
    generate_pages_recursively("content/", "template.html", "public/")

def copy_static_to_public():
    static_exists = os.path.exists("static")
    public_exists = os.path.exists("public")
    if public_exists:
        shutil.rmtree("public")
    shutil.copytree("static", "public")

def create_directories(path):
    start = path.rsplit('/')
    if not os.path.exists(start):
        os.makedirs(start)

main()