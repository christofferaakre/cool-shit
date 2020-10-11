import os

def ensure_dir(file_path: str):
    """
    Give a dummy filepath like plots/iWantThisDirectory/filename.extension.
    Then it will check if the directory plots/iWantThisDirectory exists, and
    if it doesn't, it will create it
    """
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)