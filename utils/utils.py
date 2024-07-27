import shutil
import os
import logging


def send_file_to_archive(file_path: str, archive_dir: str) -> None:
    """
    Move a file to the specified archive directory.

    Parameters:
    - file_path: Path of the file to move.
    - archive_dir: Directory where the file should be moved.

    Returns:
    - None
    """
    try:
        # Construct the new file path in the archive directory
        archived_file_path = os.path.join(archive_dir, os.path.basename(file_path))

        # Move the file to the archive directory
        shutil.move(file_path, archived_file_path)

        logging.info(f'Successfully moved the file to archive: {archived_file_path}')

    except Exception as e:
        logging.error(f'Failed to move the file: {e}')


def get_first_file_name(folder_path: str):
    """
    Get the name of the first file in the specified folder
    """
    try:
        # List all files and directories in the folder
        files_and_dirs = os.listdir(folder_path)

        # Filter out directories and keep only files
        files = [f for f in files_and_dirs if os.path.isfile(os.path.join(folder_path, f))]

        # Check if there are any files
        if files:
            # Return the first file name
            return files[0]
        else:
            return None

    except Exception as e:
        print(f"Error: {e}")
        return None
