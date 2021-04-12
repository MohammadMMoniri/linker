from django.test import TestCase
from .models import LinkModel
from django.contrib.auth import get_user_model


class LinkTestCase(TestCase):
    def setUp(self):
        LinkModel.objects.create(title="google", link="www.google.com", shortcut="xXse3")
        user = get_user_model().objects.first()
        LinkModel.objects.create(owner=user, title="yahoo", link="www.yahoo.com", shortcut="yahoo")
    
    def test_get_orginal_link(self):
        google = LinkModel.get_orginal_link("xXse3")
        self.assertEqual(google, "www.google.com")
        yahoo = LinkModel.get_orginal_link(shortcut="yahoo")
        self.assertEqual(yahoo, "www.yahoo.com")
