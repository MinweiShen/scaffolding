from docopt import docopt


class CommandParser(object):
    def __init__(self, doc, argv, version):
        self.args = docopt(doc, argv=argv, version=version)
        print self.args

    @property
    def is_list(self):
        return self.args['list']

    @property
    def is_create(self):
        return self.args['create']
