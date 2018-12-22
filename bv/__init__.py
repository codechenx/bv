import argparse
import gzip
import os

from . import vdtui
from .color_print import *
from .config import init_configure
from .io import GeneralReader, ExcelReader
from .ui import TableViewer
from .utils import get_file_extension, get_simple_config, detect_file_sep, detect_file_encoding, trans_data


def bv():
    # initialize and get dict of all file configure 
    config_dict = init_configure()

    # argument parser
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', help="file name")
    parser.add_argument('-s', default=None, help="delimiter", type=str)
    parser.add_argument('-ss', default=None, type=str, help="ignore lines with specific prefix")
    parser.add_argument('-sn', default=0, type=int, help="ignore first n lines")
    parser.add_argument('-rc', default=None, nargs='+', type=int,
                        help="only show columns(support for multiple arguments, separated by space) ")
    parser.add_argument('-hc', default=None, nargs='+', type=int,
                        help="hide columns(support for multiple arguments, separated by space)")
    parser.add_argument('-type', choices=['csv', 'tsv', 'vcf', 'maf', 'gff', 'gtf', 'bed', 'xlsl'],
                        help="specify a file type to file manual")
    parser.add_argument('--noheader', action='store_true',help="don't use fist line as header")
    parser.add_argument('--trans', action='store_true', help="view transposed data")
    parser.add_argument('--compressed', action='store_true', help="file is compressed?")
    parser.add_argument('--version', action='version', version='bv 0.1.3')

    args = parser.parse_args()

    # get file extension and corresponding config
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
        sep = detect_file_sep(fn)
        file_config = get_simple_config(sep)

    # get suitable reader
    reader = ExcelReader() if ext == "xlsx" else GeneralReader()

    # load file data to reader
    if args.noheader:
        reader.load_file(fn, file_config, compressed, False)
        reader.data.header = [str(i + 1) for i in range(reader.data.size[1])]
    else:
        reader.load_file(fn, file_config, compressed)

    # skip first N line
    if args.sn != 0:
        reader.data.body = reader.data.body[args.sn:len(reader.data.body)]
    
    # hide column assigned by the user
    if args.hc is not None:
        if isinstance(args.hc, int):
            args.hc = [args.hc]
        rm_col = [i - 1 for i in args.hc]
        reader.data.rm_col(rm_col)
    
    # only show column assigned by the user
    if args.rc is not None:
        if isinstance(args.rc, int):
            args.rc = [args.rc]
        rm_col = [i for i in range(reader.data.size[1]) if i + 1 not in args.rc]
        reader.data.rm_col(rm_col)

    # transpose data if True
    if args.trans:
        if args.noheader:
            reader.data.body = trans_data(reader.data.body)
            reader.data.header = [str(i + 1) for i in range(reader.data.size[1])]
        else:
            combind_header_body = [reader.data.header] + reader.data.body
            trans_combind_header_body = trans_data(combind_header_body)
            reader.data.body = trans_combind_header_body[1:]
            reader.data.header = trans_combind_header_body[0]

    
    # show data
    vdtui.run([TableViewer(reader.path, reader)])
