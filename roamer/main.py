#!/usr/bin/env python

"""
argh
"""

import os
from roamer.python_edit import file_editor
from roamer.directory import Directory
from roamer.edit_directory import EditDirectory
from roamer.engine import Engine
from roamer.record import Record


def main():
    """
    argh
    """
    cwd = os.getcwd()
    raw_entries = os.listdir(cwd)

    directory = Directory(cwd, raw_entries)
    output = file_editor(directory.text())
    record = Record()
    edit_directory = EditDirectory(cwd, output)
    diff_engine = Engine(directory, edit_directory, record)
    print diff_engine.print_commands()
    record.add_dir(directory)

if __name__ == "__main__":
    main()