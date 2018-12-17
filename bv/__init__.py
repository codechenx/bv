import argparse
import gzip
import os

from . import vdtui
from .color_print import *
from .config import init_configure
from .io import GeneralReader
from .ui import TableViewer
from .utils import get_file_extension, get_simple_config, detect_sep, detect_encoding, trans_data


def bv():
    config_dict = init_configure()
    reader = GeneralReader()

    parser = argparse.ArgumentParser()
    parser.add_argument('filename', help="file name")
    parser.add_argument('-s', default=None, help="delimiter", type=str)
    parser.add_argument('-header', type=int, default=1, choices=[0, 1],
                        help="0, column number as header;1, first line as header;")
    parser.add_argument('-ss', default=None, type=str, help="ignore lines with specific prefix")
    parser.add_argument('-sn', default=0, type=int, help="ignore first n lines")
    parser.add_argument('-rc', default=None, nargs='+', type=int,
                        help="only show columns(support for multiple arguments, separated by space) ")
    parser.add_argument('-hc', default=None, nargs='+', type=int,
                        help="hide columns(support for multiple arguments, separated by space)")
    parser.add_argument('-type', choices=['csv', 'tsv', 'vcf', 'maf', 'gff', 'gtf', 'bed'],
                        help="specify a file type to file manual")
    parser.add_argument('--trans', action='store_true', help="view transposed data")
    parser.add_argument('--compressed', action='store_true', help="file is compressed?")

    args = parser.parse_args()

    fn = args.filename
    if not os.path.exists(fn):
        printout("file does not exist\n", RED)
        exit()
    ext, compressed = get_file_extension(fn)
    if args.type: ext = args.type
    if args.compressed: compressed = args.compressed
    file_config = config_dict.get(ext, None)
    if args.s is not None or args.ss is not None:
        file_config = get_simple_config(args.s, args.ss)
    if file_config is None:
        if compressed:
            encoding = detect_encoding(fn)
            with gzip.open(fn) as f:
                line = f.readline().decode(encoding)
        else:
            with open(fn) as f:
                line = f.readline()

        sep = detect_sep(line)
        file_config = get_simple_config(sep)
    reader.load_file(fn, file_config, compressed)

    if args.sn != 0:
        reader.data.body = reader.data.body[args.sn:len(reader.data.body)]

    if args.hc is not None:
        if isinstance(args.hc, int):
            args.hc = [args.hc]
        rm_col = [i - 1 for i in args.hc]
        reader.data.rm_col(rm_col)

    if args.rc is not None:
        if isinstance(args.rc, int):
            args.rc = [args.rc]
        rm_col = [i for i in range(reader.data.size[1]) if i + 1 not in args.rc]
        reader.data.rm_col(rm_col)

    if args.trans:
        reader.data.body = trans_data(reader.data.body)

    if args.header == 0:
        reader.data.body = [[str(i + 1) for i in range(reader.data.size[1])]] + reader.data.body

    vdtui.run([TableViewer(reader.path, reader)])
