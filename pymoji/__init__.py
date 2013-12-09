"""Emits HTML from emoji"""

__author__ = 'Michael Joseph'
__email__ = 'michaeljoseph@gmail.com'
__url__ = 'https://github.com/michaeljoseph/pymoji'
__version__ = '0.0.1'

from .emoji import emoji

def pymoji(text):
	if text[0] <> text[:-1] and text[0] <> ':':
		text = ':%s:' % text
	return emoji(text)
