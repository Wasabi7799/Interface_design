"""Exercise the deployed entry file's error handling without starting Streamlit."""
import ast
from pathlib import Path
from types import SimpleNamespace
import unittest
from unittest.mock import Mock

import requests


class ApiErrorTests(unittest.TestCase):
    def setUp(self):
        tree = ast.parse(Path(__file__).with_name('app.py').read_text(encoding='utf-8'))
        names = {'api_error_text', 'api_error_messages', 'api_request'}
        selected = [node for node in tree.body if
                    isinstance(node, ast.FunctionDef) and node.name in names or
                    isinstance(node, ast.Assign) and any(isinstance(target, ast.Name) and target.id == 'API_ERROR_TEXT' for target in node.targets)]
        self.errors = []
        self.state = {'lang':'zh-TW'}
        self.transport = SimpleNamespace(request=Mock(), post=Mock(), Timeout=requests.Timeout, RequestException=requests.RequestException)
        self.ns = {'st':SimpleNamespace(session_state=self.state, error=self.errors.append),
                   't':lambda key:key, 'requests':self.transport, 'api_base_url':lambda:'https://example.test/api'}
        exec(compile(ast.Module(body=selected, type_ignores=[]), 'app.py', 'exec'), self.ns)

    def response(self, status, data):
        self.transport.request.return_value = SimpleNamespace(status_code=status, ok=status < 400, json=lambda:data)
        return self.ns['api_request']('POST', 'auth/register/', payload={'password':'DO-NOT-EXPOSE'})

    def test_password_validation_and_duplicate_account(self):
        self.assertIsNone(self.response(400, {'password':['This password is too common.', 'This password is entirely numeric.']}))
        self.assertIn('密碼太常見', self.errors[0])
        self.assertIn('不能全部是數字', self.errors[0])
        self.assertEqual(len(self.errors), 1)
        self.errors.clear()
        self.response(400, ['Unable to register this account.'])
        self.assertIn('Email 可能已註冊', self.errors[0])

    def test_login_list_error_and_english(self):
        self.state['lang'] = 'en'
        self.response(400, ['Email or password is incorrect.'])
        self.assertIn('Email or password is incorrect.', self.errors[0])
        self.assertNotIn('Cannot reach', self.errors[0])

    def test_listing_validation_identifies_category_and_district(self):
        self.response(400, {'sub':['Unknown category/subcategory pair.'], 'district':['Unknown district.']})
        self.assertIn('subcategory:', self.errors[0])
        self.assertIn('後端缺少此分類', self.errors[0])
        self.assertIn('district:', self.errors[0])
        self.assertIn('後端缺少此地區', self.errors[0])

    def test_status_messages_do_not_expose_raw_backend_details(self):
        for status, expected in [(403,'權限'),(404,'找不到 API'),(429,'次數過多'),(500,'Render Logs')]:
            self.errors.clear()
            self.response(status, {'detail':'SECRET_TOKEN traceback DO-NOT-EXPOSE'})
            self.assertIn(expected, self.errors[0])
            self.assertNotIn('SECRET_TOKEN', self.errors[0])
            self.assertNotIn('DO-NOT-EXPOSE', self.errors[0])

    def test_transport_and_invalid_json_are_distinct(self):
        for error, expected in [(requests.Timeout(),'逾時'),(requests.ConnectionError(),'無法連上'),(ValueError(),'非預期格式')]:
            self.errors.clear()
            self.transport.request.side_effect = error
            self.assertIsNone(self.ns['api_request']('POST', 'auth/login/'))
            self.assertIn(expected, self.errors[0])

    def test_html_error_and_success(self):
        self.transport.request.return_value = SimpleNamespace(status_code=502, ok=False, json=Mock(side_effect=ValueError()))
        self.ns['api_request']('POST', 'auth/login/')
        self.assertIn('HTTP 502', self.errors[0])
        self.errors.clear()
        self.assertEqual(self.response(200, {'ok':True}), {'ok':True})
        self.assertEqual(self.errors, [])


if __name__ == '__main__':
    unittest.main()
