import xml.dom.minidom


class Display(object):

    def __init__(self, dom=None):
        if dom is not None:
            self.dom = dom.cloneNode(True)

    @classmethod
    def from_file(cls, filename):
        disp = cls()
        disp.dom = xml.dom.minidom.parse(filename)
        return disp

    @property
    def cells(self):
        if not hasattr(self, '_cells'):
            self._cells = self._get_cells()
        return self._cells

    def for_board(self, board):
        new_disp = self.__class__(self.dom)
        return new_disp

    def cell(self, coords, val=None):
        if val is not None:
            self._set_cell(coords, val)

        retval = self._get_cell(coords)
        return retval

    def _set_cell(coords, val):
        pass

    def _get_cell(coords):
        pass

    def get_rows(self):
        rows = []
        groups = self.dom.getElementsByTagName('g')
        for g in groups:
            if g.hasAttribute('class'):
                if g.getAttribute('class') == 'row':
                    rows.append(g)
        return rows

    def _get_cells(self):
        cells = {}
        rows = self.get_rows()
        for x, node in enumerate(rows):
            groups = node.getElementsByTagName('g')
            for y, g in enumerate(groups):
                if g.hasAttribute('class'):
                    if g.getAttribute('class') == 'cell':
                        cells[(x, y)] = g
        return cells
