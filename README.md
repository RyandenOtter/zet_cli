# Zet App

This little application is a tool that I wrote to help me quickly create Zettelkasten notes. By default, this app will create notes in the `~/zet/` folder on your computer. Each new note is created as `README.md` and is put in a new folder named based off of the current `datetime` when you created them. They are formatted in `%Y%m%d%H%M%S%f`. This allows the notes that are created to be easily displayed in github.

# Installation
NOTE: It is currently not compiled as a package or anything. So, for the time being you have to run it manually.
- Clone the git repo.
- Connect the pipenv by running `pipenv shell`
- Navigate the `zet_cli` folder.
- Execute the `new` command to create a new note:
```bash
python __main__.py new
```

ToDo:
- [ ] Compile this so it can be installed and run as a CLI tool

