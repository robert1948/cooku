from django.test import TestCase

class HelloWorldTest(TestCase):
    def test_hello_world(self):
        self.assertEqual("Hello, World!", "Hello, World!")