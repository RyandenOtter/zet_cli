
from dataclasses import dataclass
from datetime import datetime
import os
from pathlib import Path
from subprocess import call


@dataclass
class Configuration():
    file_path:Path = Path(os.getenv("ZET_PATH", Path(Path.home(), 'zet')))
    file_name = os.getenv("ZET_FILE_NAME", "README.md")
    folder_name_format = os.getenv("ZET_FOLDER_NAME_FORMAT", "%Y%m%d%H%M%S%f")
    editor = os.environ.get('EDITOR', 'nvim')
    template = "# Q: \n\n" \
            "Related:\n-\n\n" \
            "Tags:\n-"

    if not os.path.exists(file_path):
        os.makedirs(file_path)
    


def generate_folder_name() -> str:
    configuration = Configuration()
    return str(datetime.now().strftime(configuration.folder_name_format))

def create_new_zettelkasten():

    configuration = Configuration()

    # Ensure the path exists
    if not os.path.exists(configuration.file_path):
        print("Creating path ", configuration.file_path)
        os.makedirs(configuration.file_path)

    # Get the name of the folder
    folder_name = generate_folder_name()
    folder_path = Path(configuration.file_path, folder_name)

    # Create the new folder
    os.mkdir(folder_path)

    # Create the new file
    new_file = Path(folder_path, configuration.file_name)
    with open(new_file, 'w') as file:
        file.write(configuration.template)
        file.flush()
        call([configuration.editor, file.name])
    
    print(new_file)


    

def list_all():
    """
    List all of the Zettelkasten
    """

    configuration = Configuration()

    for path in configuration.file_path.rglob("*.md"):
        print(path)


