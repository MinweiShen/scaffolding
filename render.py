import sys
import re
tag = re.compile('({{.*?}})')


class ContextDoseNotExist(Exception):
    def __init__(self, file='', lineno=0, name=''):
        if file:
            self.message = '%s line %d: {{ %s }} not defined.' % (
                file, lineno, name
            )
        else:
            self.message = '{{ %s }} not defined.' % name


class Template(object):
    def __init__(self, file, temp_str=''):
        self.file = file
        self.template_string = temp_str or self._get_template_string(file)
        self.node_list = self.make_node_list()

    def make_node_list(self):
        tokens = tag.split(self.template_string)
        result = []
        for token in tokens:
            if token.startswith('{{'):
                result.append((token[2:-2].strip(), 'VAR'))
            else:
                result.append((token, 'TEXT'))
        return result

    def render(self, context):
        result = []
        lineno = 1
        try:
            for node in self.node_list:
                result.append(self._render(node, context, lineno))
                lineno += node[0].count('\n')
        except ContextDoseNotExist, e:
            if self.file:
                print e.message
            else:
                print 'In %s, %s' % (self.template_string, e.message)
            sys.exit(-1)
        return ''.join(result)

    def _render(self, node, context, lineno):
        token, t = node
        if t == 'TEXT':
            return token
        else:
            try:
                return context[token]
            except KeyError:
                raise ContextDoseNotExist(self.file, lineno, token)

    @classmethod
    def _get_template_string(cls, f):
        with open(f, 'r') as temp:
            return temp.read()





