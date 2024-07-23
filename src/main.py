import os
import shutil
import logging

from copystatic import copy_files_recursive, generate_page

# Configure logging
logging.basicConfig(filename='site_generation.log', level=logging.DEBUG, 
                    format='%(asctime)s %(levelname)s:%(message)s')

# Define paths
dir_path_static = "/root/Site/static"
dir_path_public = "/root/Site/public"
content_path = "/root/Site/content/index.md"
dest_path = "/root/Site/public/index.html"
template = "/root/Site/template.html"

def main():
    logging.info("Starting site generation...")

    # Delete the public directory if it exists
    if os.path.exists(dir_path_public):
        logging.info(f"Deleting public directory: {dir_path_public}")
        shutil.rmtree(dir_path_public)

    # Copy static files to the public directory
    logging.info(f"Copying static files from {dir_path_static} to {dir_path_public}") 
    copy_files_recursive(dir_path_static, dir_path_public)

    # Generate the HTML page
    logging.info(f"Generating page from {content_path} to {dest_path} using template {template}")
    generate_page(content_path, template, dest_path)
    
    logging.info("Site generation completed.")

# Run the main function
if __name__ == "__main__":
    main()