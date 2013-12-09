"""
pymoji.

Usage:
  pymoji [options] <emoji>

  pymoji -h | --help

Options:
  --debug               Debug.
  -h --help             Show this screen.
"""

from docopt import docopt
import logging

import pymoji

log = logging.getLogger(__name__)


def main():
    arguments = docopt(__doc__, version=pymoji.__version__)
    debug = arguments.get('--debug', False)
    logging.basicConfig(level=logging.DEBUG if debug else logging.INFO)
    log.debug('arguments: %s', arguments)
    print(pymoji.pymoji(arguments['<emoji>']))
