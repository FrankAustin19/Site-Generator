import os
import shutil

from copystatic import copy_files_recursive


dir_path_static = "/root/Site/static"
dir_path_public = "/root/Site/public"


def main():
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to public directory...")
    copy_files_recursive(dir_path_static, dir_path_public)


main()
