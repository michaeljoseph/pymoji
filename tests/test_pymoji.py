from . import BaseTestCase

from pymoji import pymoji


class TestPymoji(BaseTestCase):

    def test_something(self):
        self.assertEquals(
            'Hello World!',
            pymoji(),
        )
