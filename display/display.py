import os
import xml.dom.minidom


base_svg = os.path.join(os.path.dirname(__file__), 'board.svg')
default_base_dom = xml.dom.minidom.parse(base_svg)


class Display(object):

    def __init__(self, dom=None):
        if dom is not None:
            self.dom = dom.cloneNode(True)
        else:
            self.dom = default_base_dom.cloneNode(True)

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
            self._set_cell_value(coords, val)
            self._set_cell_color(coords, val)
        return self.cells[coords]

    def _set_cell_value(self, coords, val):
        node = self.cells[coords]
        text = node.getElementsByTagName('text')

        if text.hasChildNodes():
            for n in text.childNodes:
                text.removeChild(n)
        text.appendChild(self.dom.createTextNode(val))

    def _set_cell_color(self, coords, val):
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
