
from dataclasses import dataclass
from datetime import datetime
import os
from pathlib import Path
from subprocess import call

DEFAULT_TEMPLATE = """# Q:

Related:
-

Tags:
-
"""

@dataclass
class Configuration():
    file_path: Path = Path(os.getenv("ZET_PATH", Path(Path.home(), 'zet')))
    file_name: str = os.getenv("ZET_FILE_NAME", "README.md")
    folder_name_format: str = os.getenv("ZET_FOLDER_NAME_FORMAT", "%Y%m%d%H%M%S%f")
    template_path: Path = Path(file_path, 'templates')
    editor = os.environ.get('EDITOR', 'nvim')

    # Ensure all default paths exist
    for path in [file_path, template_path]:
        if not os.path.exists(path):
            os.makedirs(path)

    # If the default template does not exist, create it
    default_template_path = Path(template_path, 'default.md')
    if not os.path.isfile(default_template_path):
        with open(default_template_path, 'w') as default_file:
            default_file.write(DEFAULT_TEMPLATE)
    


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
    with open(configuration.default_template_path,  'r') as default_template:
        default = default_template.read()

    with open(new_file, 'w') as file:
        file.write(default)
        file.flush()
        call([configuration.editor, file.name])
    
    print("Note saved to: ", new_file)


    

def list_all():
    """
    List all of the Zettelkasten
    """

    configuration = Configuration()

    for path in configuration.file_path.rglob("*.md"):
        print(path)


