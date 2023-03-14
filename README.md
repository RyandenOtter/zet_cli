# Zet App

This little application is a tool that I wrote to help me quickly create Zettelkasten notes. By default, this app will create notes in the `~/zet/` folder on your computer. Each new note is created as `README.md` and is put in a new folder named based off of the current `datetime` when you created them. They are formatted in `%Y%m%d%H%M%S%f`. This allows the notes that are created to be easily displayed in github.

# Installation
NOTE: It is currently not compiled as a package or anything. So, for the time being you have to run it manually.
- Clone the git repo.
- Connect the pipenv by running `pipenv shell`
- Navigate to the `zet_cli` folder.
- Execute your commands

### Commands
Execute the `new` command to create a new note:
```bash
python zet_cli/__main__.py new
```

Execute the `list` command to list all of the notes you have created:
```bash
python zet_cli/__main__.py list
```

ToDo:
- [x] Add feature to automatically open new notes in NeoVim
- [ ] Compile this so it can be installed and run as a CLI tool
- [ ] Add the ability to specify and use templates when creating new notes

