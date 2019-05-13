import re

class Row:
    dec_pat = re.compile("<class '.*\.(.*)'>")

    def __init__(self, row):
        for i, k in enumerate(self.keys):
            setattr(self, k, row[i])

    def __str__(self):
        klass = str(self.__class__)
        m = self.dec_pat.match(klass)
        klass = m.group(1) if m else 'n/a'
        return f'{klass}(' + ' '.join([str(getattr(self, k)) for k in self.keys]) + ')'

    def __repr__(self):
        return str(self)


class Table(list):
    def __init__(self, table_name):
        c = conn[0].cursor()
        self.extend([self.row_klass(r) for r in c.execute(f'select * from {table_name}')])
        self.idmap = {}
        for it in self:
            self.idmap[it.id] = it

conn = [None]
