
from dataclasses import dataclass
from datetime import datetime
import os
from pathlib import Path
from subprocess import call
from typing import Optional

DEFAULT_TEMPLATE = """# Q:

Related:
-

Tags:
-
"""

@dataclass
class Configuration():
    zet_path: Path = Path(os.getenv("ZET_PATH", Path(Path.home(), 'zet')))
    note_path: Path = Path(zet_path, 'notes')
    file_name: str = os.getenv("ZET_FILE_NAME", "README.md")
    folder_name_format: str = os.getenv("ZET_FOLDER_NAME_FORMAT", "%Y%m%d%H%M%S%f")
    template_path: Path = Path(zet_path, 'templates')
    editor = os.environ.get('EDITOR', 'nvim')

    # Ensure all default paths exist
    for path in [note_path, template_path]:
        if not os.path.exists(path):
            os.makedirs(path)

    # If the default template does not exist, create it
    default_template_path = Path(template_path, 'default.md')
    if not os.path.isfile(default_template_path):
        with open(default_template_path, 'w') as default_file:
            default_file.write(DEFAULT_TEMPLATE)
    


def generate_folder_name(configuration: Configuration) -> str:
    return str(datetime.now().strftime(configuration.folder_name_format))

def _get_template(template: Optional[str], configuration:Configuration):

    # Create the template path and make sure it exists:
    if template is None:
        template_path = configuration.default_template_path
    else:
        # Shoud this be handled in the cli.py?
        assert Path(template).suffix == '', \
                "Please do not include the extension in the template name"

        template_path = Path(configuration.template_path, f"{template}.md")

    assert os.path.isfile(template_path), f"{template} is not a defined tempate."

    with open(template_path,  'r') as template_file:
        template_data = template_file.read()

    return template_data


def create_new_note(template: Optional[str], configuration: Configuration):

    # Get the name of the folder
    folder_name = generate_folder_name(configuration)
    folder_path = Path(configuration.note_path, folder_name)

    # Create the new folder
    os.mkdir(folder_path)

    # Create the new file
    template_data = _get_template(template, configuration)

    new_file = Path(folder_path, configuration.file_name)
    with open(new_file, 'w') as file:
        file.write(template_data)
        file.flush()
        call([configuration.editor, file.name])
    
    print("Note saved to: ", new_file)

def create_new_template(name: str, configuration: Configuration):


    if Path(name).suffix == '':
        name = f"{name}.md"
    new_template_file = Path(configuration.template_path, name)
    with open(new_template_file, 'w') as file:
        file.flush()
        call([configuration.editor, file.name])
    
    print("New Template created: ", new_template_file )


    

def _list_all_md_files(path: Path):
    for note_path in path.rglob("*.md"):
        print(note_path)

def list_all_notes(configuration: Configuration):
    """
    List all of the notes
    """

    _list_all_md_files(configuration.note_path)


def list_all_templates(configuration: Configuration):
    """
    List all of the templates
    """

    _list_all_md_files(configuration.template_path)


