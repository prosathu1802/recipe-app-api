"""Sample Test  """

from django.test import SimpleTestCase

from app import calc


class CalcTests(SimpleTestCase):
    """Test the calc modules"""

    def test_add_numbers(self):
        result = calc.add(5, 6)
        self.assertEqual(result, 11)


    def test_subtract_numbers(self):
        result = calc.subtract(10, 15)

        self.assertEqual(result, 5)
