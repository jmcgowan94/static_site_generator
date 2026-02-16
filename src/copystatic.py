import os
import shutil

def walk_and_copy(from_path, to_path):
    items = os.listdir(from_path)
    for item in items:
        current_path = os.path.join(from_path, item)
        current_dest = os.path.join(to_path, item)
        if not os.path.isdir(current_path):
            # print(f"Copying {item} from {from_path} to {to_path}")
            shutil.copy(current_path, current_dest)
        else:
            # print(f"{item} is not a file. Moving to {current_path} directory.")
            os.makedirs(current_dest, exist_ok=True)
            walk_and_copy(current_path, current_dest)


def move_files(from_dir, to_dir):
    root_path = os.getcwd()
    from_path = os.path.join(root_path, from_dir)
    to_path = os.path.join(root_path, to_dir)
    if not os.path.exists(from_path):
        raise Exception(f"from_path {from_path} does not exist!")
    if os.path.exists(to_path):
        shutil.rmtree(to_path)
    os.mkdir(to_path)
    walk_and_copy(from_path, to_path)