from . import BaseTestCase

from pymoji import pymoji


class TestPymoji(BaseTestCase):

    def test_pymoji(self):
        self.assertEquals(
            '<img class="emoji" title="+1" alt="+1" '
            'height="20" width="20" '
            'src="http://a248.e.akamai.net/assets.github.com/'
            'images/icons/emoji/+1.png" align="top">',
            pymoji(':+1:'),
        )

    def test_pymoji_phrase(self):
        self.assertEquals(
            'this is a phrase with a '
            '<img class="emoji" title="+1" alt="+1" '
            'height="20" width="20" '
            'src="http://a248.e.akamai.net/assets.github.com/'
            'images/icons/emoji/+1.png" align="top">',
            pymoji('this is a phrase with a :+1:'),
        )

    def test_pymoji_word(self):
        self.assertEquals(
            '<img class="emoji" title="+1" alt="+1" '
            'height="20" width="20" '
            'src="http://a248.e.akamai.net/assets.github.com/'
            'images/icons/emoji/+1.png" align="top">',
            pymoji('+1'),
        )

    def test_unknown_emoji(self):
        self.assertEquals(':wat:', pymoji(':wat:'))
