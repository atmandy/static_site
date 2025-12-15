import os
import shutil


def static_copy(source_path, dest_path):
    if not os.path.exists(dest_path):
        os.mkdir(dest_path)

    for filename in os.listdir(source_path):
        from_path = os.path.join(source_path, filename)
        destin_path = os.path.join(dest_path, filename)
        print(f" * {from_path} -> {destin_path}")
        if os.path.isfile(from_path):
            shutil.copy(from_path, destin_path)
        else:
            static_copy(from_path, destin_path)
