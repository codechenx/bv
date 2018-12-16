from .utils import (check_unified_length, convert_numeric_list, trans_data)


class Data:
    """
    class that store data

    :ivar _type: str, The file type that data come from
    :ivar _metadata: list of string
    :ivar _body: list of list of string
    """

    def __init__(self):
        self._type = ""
        self._metadata = []
        self._body = []

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, m_type):
        assert isinstance(m_type, str)
        self._type = m_type

    @property
    def metadata(self):
        return self._metadata

    @metadata.setter
    def metadata(self, m_header):
        assert isinstance(m_header, list)
        self._metadata = m_header

    @property
    def body(self):
        return self._body

    @body.setter
    def body(self, m_body):
        assert isinstance(m_body, list) and check_unified_length(m_body)
        self._body = m_body

    @property
    def size(self):
        """
        :return: int int, row length column length
        """
        return (len(self._body), len(self._body[0])) if self._body else (0, 0)

    def empty(self):
        """empty all  data"""
        self._type = ""
        self._metadata = []
        self._body = []

    def sorted_by_col(self, col_num):
        """
        sort object body data by x column

        :param col_num: column number of data body
         """
        trans_body_data = trans_data(self._body)

        assert isinstance(col_num, int) and col_num < len(trans_body_data)

        numeric_col = convert_numeric_list(trans_body_data[col_num])
        col_sort_index = sorted(range(len(numeric_col)), key=numeric_col.__getitem__)  # get sort index of col
        for col_i in range(len(trans_body_data)):
            sorted_col = [trans_body_data[col_i][i] for i in col_sort_index]
            trans_body_data[col_i] = sorted_col
        if not check_unified_length(trans_body_data):
            raise Exception("sorted error")
        self._body = trans_data(trans_body_data)

    def sorted_by_row(self, row_num):
        """
        sort object body data by x row

        :param row_num: row number of data body
        """

        assert isinstance(row_num, int) and row_num < self.size[0]

        numeric_col = convert_numeric_list(self._body[row_num])

        col_sort_index = sorted(range(len(numeric_col)), key=numeric_col.__getitem__)  # get sort index of col
        for row_i in range(len(self._body)):
            sorted_row = [self._body[row_i][i] for i in col_sort_index]
            self._body[row_i] = sorted_row

    def get_sorted_row(self, row_num):
        """
        get sorted x row value

        :param row_num: row number of data body
        """
        assert isinstance(row_num, int) and row_num < self.size[0]

        return sorted(self._body[row_num])

    def get_sorted_col(self, col_num):
        """
        get sorted x column value

        :param col_num: column number of data body
        """
        assert isinstance(col_num, int) and col_num < self.size[1]

        col = [i[col_num] for i in self._body]
        return sorted(col)

    def get_col(self, col_num):
        """
        get n column value

        :param col_num: column number of data body
        :return: list of string
        """
        assert isinstance(col_num, int) and col_num < self.size[1]
        return [i[col_num] for i in self._body]

    def get_row(self, row_num):
        """
         get n row value

        :param row_num: row number of data body
        :return: list of string
        """
        assert isinstance(row_num, int) and row_num < self.size[0]
        return self._body[row_num]

    def rm_col(self, col_num):
        """
        remove some col from dada
        :param col_num: int or list
        """
        if isinstance(col_num, int):
            col_num = [col_num]

        assert all(map(lambda x: x < self.size[1], col_num))

        temp = []
        for row in self._body:
            new_row = [value for index, value in enumerate(row) if index not in col_num]
            temp.append(new_row)
        self._body = temp

    def rm_row(self, row_num):
        """
         remove som row from dada
        :param row_num: int or list
        """
        if isinstance(row_num, int):
            row_num = [row_num]

        assert all(map(lambda x: x < self.size[0], row_num))

        new_body = [value for index, value in enumerate(self._body) if index not in row_num]
        self._body = new_body
