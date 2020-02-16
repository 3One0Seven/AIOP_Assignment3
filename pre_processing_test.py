"""Test"""
import unittest
import pre_processing

class TestMyModule(unittest.TestCase):
    """Test Module"""


    def setUp(self):
        """Setup"""
        return

    def test_do_divide(self):
        """Do Test"""
        first_arg = '{"text": "@my_handler here is my tweet http://www.columbia.com"}'

        result = pre_processing.PreProc(first_arg)

        expected_result = [229, 32, 29, 274, 0, 0, 0, 0, 0, 0,\
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,\
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,\
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,\
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,\
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        self.assertEqual(result.word_index, expected_result)

    # def test_do_divide_by_zero(self):
    #     first_arg = 4
    #     second_arg = 0

    #     result = class_example.do_divide(first_arg,second_arg)

    #     expected_result = None

    #     self.assertEqual(result, expected_result)
