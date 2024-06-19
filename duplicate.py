import os


def find_and_delete_duplicates(directory):
    size_to_files = {}
    duplicates = []

    # Walk through the directory and map file sizes to file paths
    for root, _, files in os.walk(directory):
        for filename in files:
            filepath = os.path.join(root, filename)
            filesize = os.path.getsize(filepath)

            if filesize not in size_to_files:
                size_to_files[filesize] = [filepath]
            else:
                size_to_files[filesize].append(filepath)

    # Find duplicates based on file size and add them to the duplicates list
    for filepaths in size_to_files.values():
        if len(filepaths) > 1:
            # All files except the first one in the list are considered duplicates
            duplicates.extend(filepaths[1:])

    # Delete duplicates
    for duplicate in duplicates:
        try:
            os.remove(duplicate)
            print(f"Deleted duplicate: {duplicate}")
        except OSError as e:
            print(f"Error deleting {duplicate}: {e}")


if __name__ == "__main__":
    find_and_delete_duplicates(r"E:\final_file")
