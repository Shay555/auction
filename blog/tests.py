from django.test import TestCase
from .models import POST

# Create your tests here.

class PostTests(TestCase):

    """
    Here we'll define the tests
    that we'll run against our POST model
    """

    def test_str(self):
        test_title = POST(title = 'My Latest Blog Post')
        self.assertEquals(str(test_title),
                            'My Latest Blog Post')