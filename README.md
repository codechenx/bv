# bv
Data Viewer in Terminal for Bioinformatician

[![GitHub license](https://img.shields.io/github/license/codechenx/tv.svg)](https://github.com/codechenx/bv/blob/master/LICENSE)
[![PyPI version](https://badge.fury.io/py/bv.svg)](https://badge.fury.io/py/bv)
[![Build Status](https://travis-ci.org/codechenx/bv.svg?branch=master)](https://travis-ci.org/codechenx/bv)

[中文版说明](README_CN.md)
# Table of Contents

- [Description](#description)
- [Feature](#feature)
- [To do](#to-do)
- [Installation](#installation)
  - [Linux and macOS](#Linux-and-macOS)
- [Key binding](#key-binding)
- [Usage](#usage)

#### Description

bv is a tool to view the common bioinformatics data file in terminal.The TUI of bv is modifyied from [vdtui](https://github.com/saulpw/visidata/blob/stable/visidata/vdtui.py)

 ![Screenshot](screenshots/example.png)


# Feature

- Spreadsheet-like view for biological delimited data
- Vim-like key binding 
- Support for gzip compressed file
- Automatically identify unknown file type's delimiter


# To do

- support for bam and fastaq format


# Supported file types

| File type | filename extension | description                                                  |
| --------- | ------------------ | ------------------------------------------------------------ |
| csv       | .csv               | Delimited text file that uses a comma to separate values     |
| tsv       | .tsv               | Delimited text file that uses a tab to separate values       |
| vcf       | .vcf               | The Variant Call Format (VCF) specifies the format of a text file used in bioinformatics for storing gene sequence variations |
| bed       | .bed               | A BED file  is a tab-delimited text file that defines a feature track |
| maf       | .maf               | Mutation Annotation Format (MAF) is a tab-delimited text file with aggregated mutation information from VCF Files and are generated on a project-level |
| gff       | .gff               | The GFF (General Feature Format) format consists of one line per feature, each containing 9 columns of data, plus optional track definition lines |
| gtf       | .gtf               | The Gene transfer format (GTF) is a file format used to hold information about gene structure |



# Installation
### Linux and macOS

```bash
$ pip install bv
```


#### Window

Not Support


# Key binding
| Key               | description                                                 |
| ----------------- | ----------------------------------------------------------- |
| q                 | Quit                                                        |
| h, left arrow     | Moves the cursor left  one column                           |
| l, right arrow    | Moves the cursor right  one column                          |
| j, down arrow     | Moves the cursor down one row                               |
| k, up             | Moves the cursor up one row                                 |
| g, home           | Move to the top                                             |
| G, end            | Move to the bottom                                          |
| ctrl-f, page down | Move down by one page                                       |
| ctrl-b, page up   | Move up by one page                                         |
| /                 | Seach string                                                |
| n                 | Move to the next instance of the result from the search     |
| p                 | Move to the previous instance of the result from the search |
| d                 | Delete current row                                          |
| s, space          | Highlight current row                                       |
| u                 | Clear highlight of current row                              |

# Usage

```console
usage: bv [-h] [-s S] [-header {0,1}] [-ss SS] [-sn SN] [-rc RC [RC ...]]
          [-hc HC [HC ...]] [-type {csv,tsv,vcf,maf,gff,gtf,bed}] [--trans]
          [--compressed]
          filename

positional arguments:

  filename              file name

optional arguments:
  -h, --help            show this help message and exit
  -s S                  delimiter
  -header {0,1}         0, column number as header;1, first line as header;
  -ss SS                ignore lines with specific prefix
  -sn SN                ignore first n lines
  -rc RC [RC ...]       only show columns(support for multiple arguments, separated by space)
  -hc HC [HC ...]       hide columns(support for multiple arguments, separated by space)
  -type {csv,tsv,vcf,maf,gff,gtf,bed} specify a file type to file manual
  --trans               view transposed data
  --compressed          file is compressed?
```