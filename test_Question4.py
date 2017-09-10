import unittest
import Question4

class TestQuestion4(unittest.TestCase):
    def test_getCard(self):
        self.assertRaises(Exception, Question4.getCard, 70)
        self.assertRaises(TypeError, Question4.getCard, 20)

    def test_drawCard(self):
        self.assertRaises(Exception, Question4.drawCard, "Tester", 40, 2,)
        self.assertRaises(TypeError, Question4.drawCard, "Tester", 40, 2, )

if __name__ == '__main__':
    unittest.main()