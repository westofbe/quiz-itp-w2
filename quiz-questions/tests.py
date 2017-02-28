import unittest
from question_1 import question_1


class QuestionsTestCase(unittest.TestCase):
    def test_question_1(self):
        self.assertEqual(question_1(), 30, "Question 1 answer FAILED")
