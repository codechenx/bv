def tabstr_to_tab(tab_str):
    """
    translate "\\t" to "\t"
    :param tab_str: str
    :return: str
    """
    assert isinstance(tab_str, str)
    if tab_str == "\\t":
        return "\t"
    else:
        return tab_str


def check_unified_length(data):
    """
    check nested list data have same length

    :param data: list
    :return: bool
    """
    assert isinstance(data, list)
    length_list = map(len, data)
    if len(set(length_list)) == 1:
        return True
    else:
        return False


def convert_numeric_list(str_list):
    """
    try to convert list of string to list of integer(preferred) or float

    :param str_list: list of string
    :return: list of integer or float or string
    """
    assert isinstance(str_list, list)

    if not str_list:
        return str_list

    try:
        return list(map(int, str_list))
    except ValueError:
        try:
            return list(map(float, str_list))
        except ValueError:
            return str_list


def trans_data(data):
    """
    transposed  data

    :param data: list
    :return: list
    """
    assert isinstance(data, list)
    return list(map(list, zip(*data)))


def get_file_extension(fn):
    """
    get file extension and check if it is compressed
    :param: str, file path
    :return: str,bool
    """
    # assert isinstance(fn, str)

    compressed_file_ext = ["gz"]
    fn_part = fn.split(".")
    compressed = False
    ext = fn_part[-1]
    if ext in compressed_file_ext:
        compressed = True
        ext = fn_part[-2]
    return ext, compressed


def get_simple_config(sep, ignore=None):
    """
    get a file config with specify separator and ignore regex
    :param sep: str, separator
    :param ignore: str, ignore lines with specific prefix
    :return:
    """
    from bv.config import TypeConfig
    simple = TypeConfig()
    TypeConfig.body_config = {"sep": sep}
    if ignore is not None:
        TypeConfig.ignore_config = {"regex": "^" + ignore}
    return simple


def detect_file_sep(fn, compressed=False):
    """
    guess sep from file
    :param data: str, file path
    :return: str, delimiter
    """
    import csv
    import gzip

    if compressed:
        encoding = detect_file_encoding(fn)
        with gzip.open(fn) as f:
            line = f.readline().decode(encoding)
    else:
        with open(fn) as f:
            line = f.readline()

    detector = csv.Sniffer()

    return detector.sniff(line).delimiter


def detect_file_encoding(fn):
    """
    detect gzip file encoding
    :param fn:
    :return:
    """
    import chardet
    import gzip

    with gzip.open(fn) as f:
        rawdata = f.read()
    encoding = chardet.detect(rawdata)
    return encoding.get('encoding')

class Color:
    BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE = range(8)

def has_colours(stream):
    """ 
    check the console can display color
    :param stream:
    """
    if not hasattr(stream, "isatty"):
        return False
    if not stream.isatty():
        return False  # auto color only on TTYs
    try:
        import curses
        curses.setupterm()
        return curses.tigetnum("colors") > 2
    except:

        return False

def colorprint(text, colour=Color.WHITE):
    import sys
    if has_colours(sys.stdout):
        seq = "\x1b[1;%dm" % (30 + colour) + text + "\x1b[0m"
        sys.stdout.write(seq)
    else:
        sys.stdout.write(text)
