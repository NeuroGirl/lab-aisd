import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.join(current_dir, '..', '..')
sys.path.insert(0, src_dir)

import unittest

from lab4.task13.src.stack_functions import *

class TestStackFunctions(unittest.TestCase):
        # given
        # when
    def setUp(self):
        self.stack = Stack()
    
    def test_should_check_success_of_stack_empty(self):
        # then
        self.assertEqual(self.stack.isEmpty(), True)
        self.assertEqual(self.stack.display(), None)
    
    def test_should_check_success_of_stack_push_pop(self):
        # given
        # when
        self.stack.push(10)
        self.stack.push(8)
        
        # then
        self.assertEqual(self.stack.isEmpty(), False)

        popped_value = self.stack.pop()
        # then
        self.assertEqual(popped_value, 8)
        self.assertEqual(self.stack.isEmpty(), False)


if __name__ == '__main__':
    unittest.main()