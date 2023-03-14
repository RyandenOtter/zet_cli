import argparse
from typing import List
from model import list_all, create_new_zettelkasten


def main(args: argparse.Namespace):
    if args.service == 'new':
        create_new_zettelkasten()
    if args.service == "list":
        list_all()
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

    subparser.add_parser(
            'new',
            help='Add a new Zettelkasten')

    subparser.add_parser(
            'list',
            help='List all of the Zettelkasten')



    return parser.parse_args(args)
