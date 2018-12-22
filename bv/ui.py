from . import vdtui


class TableViewer(vdtui.Sheet):
    def __init__(self, path, reader):
        super().__init__(path)
        self.columns = [
            vdtui.ColumnItem(colname, i)
            for i, colname in enumerate(reader.data.header)
        ]
        self.rows = reader.data.body
