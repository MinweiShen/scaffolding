import os
import sys
from render import Template


class Handler(object):
    """ Given a directory or file which may containing variables, it should
        be able to return a converted directory or file name
    """
    def __init__(self, path, context):
        self.path = path.rstrip('/')
        self.context = context

    def convert(self):
        base = os.path.basename(self.path)
        template = Template(file=None, temp_str=base)
        base = template.render(self.context)
        return base
