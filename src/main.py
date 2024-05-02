#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Main file multiline Docstring
"""

__author__ = "First Last"
__copyright__ = "Copyright 2024, First Last"
__credits__ = ["C D", "A B"]
__license__ = "ISC"
__version__ = "1.0.0"
__maintainer__ = "First Last"
__email__ = "test@example.org"
__status__ = "Development"

import os

def main():
    """ Main entry point of the app """
    print('====================================================')
    filenames = os.listdir('.')

    for filename in filenames:
        print(filename)
    print('====================================================')

if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()