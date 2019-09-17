from django.shortcuts import make_toast
from django.test import SimpleTestCase


class MakeToastsTests(SimpleTestCase):
    def test_make_toast(self):
        self.assertEqual(make_toast(), "toast")
