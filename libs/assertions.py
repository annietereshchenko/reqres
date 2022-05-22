import json
from requests import Response
import allure


class Assertions:
    @staticmethod
    def assert_json_has_key(response: Response, name):
        try:
            response_as_dict = response.json()
        except json.JSONDecoder:
            assert False, f"Response is not in JSON format. Response text is '{response.text}'"
        with allure.step(f'Check that JSON has {name} key'):
            assert name in response_as_dict, f"Response JSON doesn't have {name} key"

    @staticmethod
    def assert_json_has_not_key(response: Response, name):
        try:
            response_as_dict = response.json()
        except json.JSONDecoder:
            assert False, f"Response is not in JSON format. Response text is '{response.text}'"
        with allure.step(f'Check that JSON does not have {name} key'):
            assert name not in response_as_dict, f"Response JSON has {name} key"

    @staticmethod
    def assert_code_status(response: Response, expected_status):
        with allure.step(f'Check status code'):
            assert response.status_code == expected_status, \
                f"Unexpected status code. Expected {expected_status}, got {response.status_code}, {response.text}"

    @staticmethod
    def assert_json_value_by_name(response: Response, name, expected_value):
        try:
            response_as_dict = response.json()
        except json.JSONDecoder:
            assert False, f"Response is not in JSON format. Response text is '{response.text}'"
        with allure.step(f'Check that {response_as_dict[name]} is equal {expected_value}'):
            assert response_as_dict[name] == expected_value, f'{response_as_dict[name]} != {expected_value}'

    @staticmethod
    def assert_expected_value_in_json_value_by_name(response: Response, name, expected_value):
        try:
            response_as_dict = response.json()
        except json.JSONDecoder:
            assert False, f"Response is not in JSON format. Response text is '{response.text}'"
        with allure.step(f'Check that {expected_value} is contained in {response_as_dict[name]}'):
            assert expected_value in response_as_dict[name], f'{expected_value} not in {response_as_dict[name]}'
