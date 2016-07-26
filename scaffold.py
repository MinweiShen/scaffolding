"""scaffolding

Usage:
  scaffold.py list
  scaffold.py create <name>
  scaffold.py create --template=<path>


Options:
  -h --help             Show this screen.
  --template=<path>     Path to your template, should be a directory

"""
import sys
import os
from utils.command_parser import CommandParser
from utils.handler import Scaffolder


VERSION = '0.1.0'
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


if __name__ == '__main__':
    parser = CommandParser(__doc__, sys.argv[1:], VERSION)
    tdir = os.path.join(BASE_DIR, 'templates')
    scaffolder = Scaffolder(tdir)
    if parser.is_list:
        scaffolder.list_templates()
    elif parser.is_create:
        scaffolder.create_layout(name=parser.args['<name>'], template=parser.args['--template'])
