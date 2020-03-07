import unittest

from foo import bar

class TestFoo(unittest.TestCase):
  def test_foo(self):
    bar.foo()