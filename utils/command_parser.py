from docopt import docopt


class CommandParser(object):
    def __init__(self, doc, argv, version):
        self.args = docopt(doc, argv=argv, version=version)

    @property
    def is_list(self):
        return self.args['list']

    @property
    def is_create(self):
        return self.args['create']

    @property
    def is_show(self):
        return self.args['show']

    @property
    def is_location(self):
        return self.args['location']

    @property
    def name(self):
        return self.args['<name>']


    @property
    def template(self):
        return self.args['--template']
