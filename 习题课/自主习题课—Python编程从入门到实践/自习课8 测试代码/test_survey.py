"""
import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    '''针对AnonymousSurvey类的测试'''

    def test_store_single_response(self):
        '''测试单个答案会被妥善的存储'''
        question = "What language did you first learn to speak?"
        llr_survey = AnonymousSurvey(question)
        llr_survey.store_response('汉语')

        self.assertIn("汉语", llr_survey.responses)

    def test_store_three_response(self):
        '''测试单个答案会被妥善的保存'''
        question = "What language did you first learn to speak?"
        llr_survey = AnonymousSurvey(question)
        responses = ['汉语', '英语', '日语']
        for r in responses:
            llr_survey.store_response(r)
        for r in responses:
            self.assertIn(r, llr_survey.responses)


if __name__ == '__main__':
    unittest.main()
"""

# 使用setUp()方法
import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    '''针对AnonymousSurvey类的测试'''

    def setUp(self):
        '''创建一个调查对象和一组答案，供使用的测试方法使用'''
        question = "What language did you first learn to speak?"
        self.llr_survey = AnonymousSurvey(question)
        self.responses = ['汉语', '英语', '日语']

    def test_store_single_response(self):
        '''测试单个答案会被妥善的存储'''
        self.llr_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.llr_survey.responses)

    def test_store_three_response(self):
        '''测试单个答案会被妥善的保存'''
        for r in self.responses:
            self.llr_survey.store_response(r)
        for r in self.responses:
            self.assertIn(r, self.llr_survey.responses)

if __name__ == '__main__':
    unittest.main()

