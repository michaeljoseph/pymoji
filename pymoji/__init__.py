"""Emits HTML from emoji"""

__author__ = 'Michael Joseph'
__email__ = 'michaeljoseph@gmail.com'
__url__ = 'https://github.com/michaeljoseph/pymoji'
__version__ = '0.0.1'

from .emoji import emoji


def pymoji(text):
    single_word = len(text.split(' ')) < 2
    first_and_last_dont_match = text[0] != text[-1:]
    first_character_is_colon = text[0] != ':'

    if first_and_last_dont_match and first_character_is_colon and single_word:
        text = ':%s:' % text

    return emoji(text)
