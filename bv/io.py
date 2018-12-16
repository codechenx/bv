import abc
import csv
import gzip
import re

from .config import TypeConfig
from .data import Data
from .utils import tabstr_to_tab, detect_encoding


class Reader:
    """
    file reader
    :ivar _path: str, file path
    :ivar _data: Data(), data class sotore file data
    :ivar _config: file type configure
    """

    def __init__(self):
        self._path = None
        self._data = Data()
        self._config = None

    @property
    def path(self):
        return self._path

    @property
    def data(self):
        return self._data

    @property
    def config(self):
        return self._config

    @abc.abstractmethod
    def load_file(self, m_path, m_config=None, compressed=False):
        raise Exception("implement load_file is required")

    def update_config(self, m_config):
        self.load_file(self._path, m_config)


class GeneralReader(Reader):
    def load_file(self, m_path, m_config=None, compressed=False):
        """
        :param m_path: str, file path
        :param m_config: TypeConfig(), file processing configure
        :param compressed: bool, check if compressed
        :return:
        """
        assert isinstance(m_path, str) and isinstance(m_config, TypeConfig)

        self._path, self._config = m_path, m_config
        try:
            if compressed:
                encoding = detect_encoding(self._path)
                f = gzip.open(self._path)
            else:
                f = open(self._path)
            ignore_regex = self._config.ignore_config.get("regex", None)
            header_regex = self._config.metadata_config.get("regex", None)
            sep = self._config.body_config.get("sep", None)
            sep = tabstr_to_tab(sep)  # translate "\\t" to "\t" if possible
            for line in f:
                line = line.decode(encoding).strip() if compressed else line.strip()
                # ignore line
                if ignore_regex and re.match(ignore_regex, line):
                    continue
                # add header data
                if header_regex and re.match(header_regex, line):
                    self._data.metadata.append(line)
                    continue
                # add body data
                self.data.body.append(list(csv.reader([line], delimiter=sep))[0])
            f.close()
        except FileNotFoundError:
            raise Exception("File is not exists")
