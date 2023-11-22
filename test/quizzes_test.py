import unittest

from datetime import datetime
from app.controllers.quizzes_controller import QuizzesController

class QuizzesTest(unittest.TestCase):

    def setUp(self):
        # Run tests on non-production data
        self.ctrl = QuizzesController('quizzes_test.json')
        
    def test_expose_failure_01(self):
        self.ctrl.clear_data()
        # Test case for adding a new quiz.
        title = "New Quiz"
        text = "This is a new quiz"
        available_date = datetime.now()
        due_date = datetime(2023, 12, 31)  
        quiz_id = self.ctrl.add_quiz(title, text, available_date, due_date)
        quizzes = self.ctrl.get_quizzes()
        # Expecting two quizzes because there's one from setUp.
        self.assertEqual(len(quizzes), 2)  

    def test_expose_failure_02(self):
        self.ctrl.clear_data()
        # Test case for adding a new quiz.
        title = 20231101
        text = "This is a new quiz 2"
        available_date = datetime.now()
        due_date = datetime(2023, 12, 31) 
        # Crushing at quizzes_contoller line 63  , TypeError: unsupported operand type(s) for +: 'int' and 'str'
        quiz_id = self.ctrl.add_quiz(title, text, available_date, due_date)
        # Because of the early crash of the program, this line of code is not be executed.
        quizzes = self.ctrl.print_quiz(quiz_id)
        

if __name__ == '__main__':
    unittest.main()