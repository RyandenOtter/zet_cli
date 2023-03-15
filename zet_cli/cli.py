import argparse
from typing import List
from model import list_all_notes, create_new_note, create_new_template, \
        list_all_templates, Configuration

CONFIGURATION = Configuration()

def handle_notes(args: argparse.Namespace):
    """ Handler for the notes parser"""
    if args.action_command == 'new':
        create_new_note(template=args.template, configuration=CONFIGURATION)
    elif args.action_command == 'list':
        list_all_notes(configuration=CONFIGURATION)
    else:
        raise Exception(f"{args.action_command} is not a valid command")

def handle_template(args: argparse.Namespace):
    """ Handler for the Template parser"""
    if args.action_command == 'new':
        create_new_template(name=args.name, configuration=CONFIGURATION)
    if args.action_command == 'list':
        list_all_templates(configuration=CONFIGURATION)


def main(args: argparse.Namespace):
    if args.service == 'note':
        handle_notes(args)
    if args.service == "template":
        handle_template(args)
    pass

def parse_args(args: List[str]) -> argparse.Namespace:
    """
    Argument parser for zet
    """

    parser = argparse.ArgumentParser(
            prog="zet",
            description="Utility for creating Zettelkasten notes")

    subparser = parser.add_subparsers(help="Actions",
                          dest="service")

    parser_note = subparser.add_parser(
            'note',
            help='Interact with Notes')

    parser_new_actions = parser_note.add_subparsers(
            title="action",
            dest="action_command")

    note_new = parser_new_actions.add_parser(
            'new',
            help="Add a new note")

    note_new.add_argument(
            "--template",
            "-t",
            help="Specify which template to use with your new note",
            required=False)

    parser_new_actions.add_parser(
            'list',
            help="List all notes")


    parser_template = subparser.add_parser(
            'template',
            help='Interact with the templates')

    parser_template_actions = parser_template.add_subparsers(
            title="action",
            dest="action_command")

    template_new = parser_template_actions.add_parser(
            'new',
            help='Add a new template')
    
    template_new.add_argument(
            "--name",
            "-n",
            help="Specify the name of the new template",
            required=True)

    parser_template_actions.add_parser(
            'list',
            help='List all templates')



    return parser.parse_args(args)
