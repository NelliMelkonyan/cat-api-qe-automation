import unittest
import pytest

from utils.request_builder.builder import Builder
from utils.response_validator.validator import ResponseValidator
from constants.const import *
from constants.status_codes import *

class GetFactsTest(unittest.TestCase):
    req_builder = Builder.createNewRequest()
    res_validator= ResponseValidator()

    @pytest.fixture(scope="session", autouse=True)
    def run_before_tests(self):
        self.req_builder.useExistingRequest().set_request_url(f"{BASE_URL}{Endpoints.FACTS.value}")
        self.req_builder.useExistingRequest().set_request_method('GET')
        yield
                

    def test_get_facts_with_valid_params(self):
        self.req_builder.useExistingRequest().set_request_params(max_length = 100, limit = 2)
        (status_code, res_body) = self.req_builder.send()
        self.assertEqual(status_code, Statuses.OK.value, 'Status code is not correct')
        self.assertEqual(len(res_body['data']), int(res_body['per_page']), 'Returned data length is not correct')
        for item in res_body['data']:
            self.assertTrue(item['length'] <= 100)
        self.res_validator.validate_response(res_body, 'schemas/get_facts.json')

    def test_get_facts_with_no_limit(self):
        self.req_builder.useExistingRequest().set_request_params(max_length = 100)
        (status_code, res_body) = self.req_builder.send()
        self.assertEqual(status_code, Statuses.OK.value, 'Status code is not correct')
        self.assertEqual(len(res_body['data']), res_body['per_page'], 'Returned data length is not correct')
        for item in res_body['data']:
            self.assertTrue(item['length'] <= 100)
        self.res_validator.validate_response(res_body, 'schemas/get_facts.json')


    def test_get_facts_with_no_max_length(self):
        self.req_builder.useExistingRequest().set_request_params(limit = 97)
        (status_code, res_body) = self.req_builder.send()
        self.assertEqual(status_code, Statuses.OK.value, 'Status code is not correct')
        self.assertEqual(len(res_body['data']), int(res_body['per_page']), 'Returned data length is not correct')
        self.res_validator.validate_response(res_body, 'schemas/get_facts.json')


    def test_get_facts_with_no_param(self):
        self.req_builder.useExistingRequest().clear_params()
        (status_code, res_body) = self.req_builder.send()
        self.assertEqual(status_code, Statuses.OK.value, 'Status code is not correct')
        self.assertEqual(len(res_body['data']), res_body['per_page'], 'Returned data length is not correct')
        self.assertEqual(len(res_body['data']), 10)
        self.res_validator.validate_response(res_body, 'schemas/get_facts.json')

    def test_get_facts_with_negative_limit(self):
        self.req_builder.useExistingRequest().set_request_params(limit = -1)
        (status_code, res_body) = self.req_builder.send()
        self.assertEqual(status_code, Statuses.NOT_FOUND.value, 'Status code is not correct')
        self.assertEqual(res_body['message'], 'Not Found')

    def test_get_facts_with_limit_exceed_total(self):
        self.req_builder.useExistingRequest().set_request_params(limit = 5000)
        (status_code, res_body) = self.req_builder.send()
        self.assertEqual(status_code, Statuses.OK.value, 'Status code is not correct')
        self.assertEqual(len(res_body['data']), int(res_body['total']), 'Returned data length is not correct')
        self.res_validator.validate_response(res_body, 'schemas/get_facts.json')
    
    def test_get_facts_with_negative_max_length(self):
        self.req_builder.useExistingRequest().set_request_params(max_length = -5)
        (status_code, res_body) = self.req_builder.send()
        self.assertEqual(status_code, Statuses.OK.value)
        self.assertEqual(len(res_body['data']), 0)

    def test_get_facts_with_non_number_limit(self):
        self.req_builder.useExistingRequest().set_request_params(limit = 'aaa')
        (status_code, res_body) = self.req_builder.send()
        self.assertEqual(status_code, Statuses.OK.value, 'Status code is not correct')
        self.assertEqual(len(res_body['data']), res_body['per_page'], 'Returned data length is not correct')
        self.res_validator.validate_response(res_body, 'schemas/get_facts.json')
