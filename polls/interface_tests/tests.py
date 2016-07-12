__author__ = 'bugmaster'
import unittest
import requests
import json

'''
Need to install requests Library
http://www.python-requests.org/en/master/
'''

class QuestionsTest(unittest.TestCase):

    def setUp(self):
        self.base_url = 'http://127.0.0.1:8000/polls/questions'

    def test_get_questions_success(self):
        '''get all questions success'''
        r = requests.get(self.base_url)
        result = json.loads(r.text)
        self.assertEqual(result['ststus'], 200)
        self.assertEqual(result['message'], 'success')


class QuestionOptionTest(unittest.TestCase):

    def setUp(self):
        self.base_url = 'http://127.0.0.1:8000/polls/question_option/'

    def test_get_question_option_success(self):
        '''get question option success'''
        r = requests.get(self.base_url,params={'qid':'1'})
        result = json.loads(r.text)
        self.assertEqual(result['ststus'], 200)
        self.assertEqual(result['message'], 'success')

    def test_get_question_option_qid_null(self):
        '''get question option qid null'''
        r = requests.get(self.base_url,params={'qid':''})
        result = json.loads(r.text)
        self.assertEqual(result['ststus'], 10021)
        self.assertEqual(result['message'], 'Parameter error')

    def test_get_question_option_qid_error(self):
        '''get question option qid error'''
        r = requests.get(self.base_url,params={'qid':'901'})
        result = json.loads(r.text)
        self.assertEqual(result['ststus'], 10022)
        self.assertEqual(result['message'], 'Query result is empty')


class QuestionResultTest(unittest.TestCase):

    def setUp(self):
        self.base_url = 'http://127.0.0.1:8000/polls/question_result/'

    def test_get_question_result_success(self):
        '''get question result success'''
        r = requests.get(self.base_url,params={'qid':'1'})
        result = json.loads(r.text)
        self.assertEqual(result['ststus'], 200)
        self.assertEqual(result['message'], 'success')

    def test_get_question_result_qid_null(self):
        '''get question result qid null'''
        r = requests.get(self.base_url,params={'qid':''})
        result = json.loads(r.text)
        self.assertEqual(result['ststus'], 10021)
        self.assertEqual(result['message'], 'Parameter error')

    def test_get_question_result_qid_error(self):
        '''get question result qid error'''
        r = requests.get(self.base_url,params={'qid':'901'})
        result = json.loads(r.text)
        self.assertEqual(result['ststus'], 10022)
        self.assertEqual(result['message'], 'Query result is empty')


class QuestionVoteTest(unittest.TestCase):

    def setUp(self):
        self.base_url = 'http://127.0.0.1:8000/polls/question_vote/'

    def test_post_question_vote_qid_null(self):
        '''get question vote qid null'''
        r = requests.post(self.base_url, data={'qid': '','cid':'2'})
        result = json.loads(r.text)
        self.assertEqual(result['ststus'], 10021)
        self.assertEqual(result['message'], 'Parameter error')

    def test_post_question_vote_cid_null(self):
        '''get question vote cid null'''
        r = requests.post(self.base_url, data={'qid': '1','cid':''})
        result = json.loads(r.text)
        self.assertEqual(result['ststus'], 10021)
        self.assertEqual(result['message'], 'Parameter error')

    def test_post_question_vote_qid_error(self):
        '''get question vote qid error'''
        r = requests.post(self.base_url, data={'qid': '901','cid':'1'})
        result = json.loads(r.text)
        self.assertEqual(result['ststus'], 10022)
        self.assertEqual(result['message'], 'Query result is empty')

    def test_post_question_vote_cid_error(self):
        '''get question vote cid error'''
        r = requests.post(self.base_url, data={'qid': '1','cid':'901'})
        result = json.loads(r.text)
        self.assertEqual(result['ststus'], 10023)
        self.assertEqual(result['message'], 'The problem is not the choice id')

    def test_post_question_vote_success(self):
        '''get question vote success'''
        r = requests.post(self.base_url, data={'qid': '1','cid':'1'})
        result = json.loads(r.text)
        self.assertEqual(result['ststus'], 200)
        self.assertEqual(result['message'], 'success')


if __name__ == '__main__':
    unittest.main()
