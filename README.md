# Zet App

This little application is a tool that I wrote to help me quickly create Zettelkasten notes. By default, this app will create notes in the `~/zet/` folder on your computer. Each new note is created as `README.md` and is put in a new folder named based off of the current `datetime` when you created them. They are formatted in `%Y%m%d%H%M%S%f`. This allows the notes that are created to be easily displayed in github.

# Installation
NOTE: It is currently not compiled as a package or anything. So, for the time being you have to run it manually.
- Clone the git repo.
- Connect the pipenv by running `pipenv shell`
- Navigate to the `zet_cli` folder.
- Execute your commands

### Commands

#### Create New Note
Execute the `note new` command to create a new note:
```bash
python __main__.py note new
```
The application will use the `default` template. If you want to specify which template you want used, provide the `--template` argument:
```bash
python __main__.py note new --template my-template
```

#### List all notes
To list all of the notes you have created:
```
python __main__.py note list
```

#### Create New Template
To create a new template:
```bash
python __main__.py template new --name test
```

#### List all templates
```bash
python __main__.py template list
```

ToDo:
- [x] Add feature to automatically open new notes in NeoVim
- [x] Add the ability to specify and use templates when creating new notes
- [x] Add the ability to specify your own templates.
- [ ] Clean up the codebase. Add some more comments.
- [ ] Build a django website that sits on top of your notes folder, and serves the markdown up in HTML
- [ ] Compile this so it can be installed and run as a CLI tool

