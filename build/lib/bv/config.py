import configparser
import itertools


class TypeConfig:
    """
    class that store configure data

    configure file format: {"Format": ["name", "extension","description"], "Header": ["regex", "description"],
                "Body": ["sep", "description"], "Ignore": ["regex", "description"]}

    :cvar _keyword: keyword of configure file
    :ivar _config: ConfigParser
    """
    _keyword = {"Format": ["name", "extension", "description"], "Metadata": ["regex", "description"],
                "Body": ["sep", "description"], "Ignore": ["regex", "description"]}

    def __init__(self, config_path=None):
        """

        :param config_path:
        """
        self._config = configparser.ConfigParser()
        if config_path:
            try:
                self._config.read(config_path)
            except FileNotFoundError:
                raise Exception("configure file is not exists")
            except configparser.Error:
                raise Exception("configure file format is error")

        if config_path and not self.check_format():
            raise Exception("configure format is error")

    def check_format(self):
        """
        check if configure file format is correct

        :return: bool
        """
        sections = self._keyword.keys()
        params = list(itertools.chain(*self._keyword.values()))
        # necessary keyword
        if ("name" not in self._config["Format"].keys()) and ("extension" not in self._config["Format"].keys()):
            return False
        for key in self._config.sections():
            if key not in sections:
                return False
            if all([i not in params for i in self._config["Format"].keys()]):
                return False
        return True

    @property
    def format_config(self):
        """
        :return: dict
        """
        try:
            return dict(self._config["Format"])
        except KeyError:
            return dict()

    @format_config.setter
    def format_config(self, format_c):
        """
        :param format_c: dict
        """
        assert isinstance(format_c, dict)

        self._config["Format"] = format_c

        if self.check_format():
            raise Exception("configure format is error")

    @property
    def metadata_config(self):
        """
        :return: dict
        """
        try:
            return dict(self._config["Metadata"])
        except KeyError:
            return dict()

    @metadata_config.setter
    def metadata_config(self, metadata_c):
        """
        :param metadata_c:  dict
        """
        assert isinstance(metadata_c, dict)

        self._config["Metadata"] = metadata_c

        if self.check_format():
            raise Exception("configure format is error")

    @property
    def body_config(self):
        """
        :return: dict
        """
        try:
            return dict(self._config["Body"])
        except KeyError:
            return dict()

    @body_config.setter
    def body_config(self, body_c):
        """
        :param body_c: dict
        """
        assert isinstance(body_c, dict)

        self._config["Body"] = body_c

        if self.check_format():
            raise Exception("configure format is error")

    @property
    def ignore_config(self):
        """
        :return: dict
        """
        try:
            return dict(self._config["Ignore"])
        except KeyError:
            return dict()

    @ignore_config.setter
    def ignore_config(self, ignore_c):
        """
        :param ignore_c: dict
        """
        assert isinstance(ignore_c, dict)

        self._config["Ignore"] = ignore_c

        if self.check_format():
            raise Exception("configure format is error")


def init_configure():
    """
    read and initialize all file type configure under configure directory
    :return: dict, {type_name:config}
    """
    try:
        import os
        from bv.default import CONFIG_DIR, CONFIG_USER_DIR

        type_config_list = []
        CONFIG_DIR_REAL_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), CONFIG_DIR)
        CONFIG_USER_DIR_REAL_PATH = CONFIG_USER_DIR
        cfg_files = [f for f in os.listdir(CONFIG_DIR_REAL_PATH) if
                     os.path.isfile(os.path.join(CONFIG_DIR_REAL_PATH, f)) and f.endswith(".cfg")]
        if os.path.exists(CONFIG_USER_DIR_REAL_PATH):
            cfg_user_files = [f for f in os.listdir(CONFIG_USER_DIR_REAL_PATH) if
                              os.path.isfile(os.path.join(CONFIG_USER_DIR_REAL_PATH, f)) and f.endswith(".cfg")]

        else:
            cfg_user_files = []

        cfg_files_set = set(cfg_files + cfg_user_files)
        for fn in cfg_files_set:
            if fn in cfg_user_files:
                type_config_list.append(TypeConfig(os.path.join(CONFIG_USER_DIR_REAL_PATH, fn)))
            else:
                type_config_list.append(TypeConfig(os.path.join(CONFIG_DIR_REAL_PATH, fn)))

        return {type_config.format_config.get("extension"): type_config for type_config in type_config_list}
    except Exception:
        raise Exception("initialize all file type configure error")
