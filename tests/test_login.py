import pytest
from test_data.test_data import TestDataUserAuthentication as TD
from libs.assertions import Assertions
from libs.my_requests import MyRequests
import allure


@allure.epic('Login')
class TestUserLogin:

    @allure.story('Login with correct data')
    def test_login_successfully(self):
        user_login_response = MyRequests.post('/login', data=TD.USER_DATA)
        Assertions.assert_code_status(user_login_response, 200)

    @allure.story('Login with correct data')
    def test_login_successfully_check_token(self):
        user_login_response = MyRequests.post('/login', data=TD.USER_DATA)
        Assertions.assert_json_has_key(user_login_response, 'token')

    @allure.story('Login with incorrect data')
    def test_login_with_non_existing_user(self):
        user_login_response = MyRequests.post('/login', data=TD.UNREGISTERED_USER_DATA)
        Assertions.assert_code_status(user_login_response, 400)

    @allure.story('Login with incorrect data')
    def test_login_with_non_existing_user_check_no_token(self):
        user_login_response = MyRequests.post('/login', data=TD.UNREGISTERED_USER_DATA)
        Assertions.assert_json_has_not_key(user_login_response, 'token')

    @allure.story('Login with incorrect data')
    def test_login_with_non_existing_user_check_error(self):
        user_login_response = MyRequests.post('/login', data=TD.UNREGISTERED_USER_DATA)
        Assertions.assert_json_has_key(user_login_response, 'error')

    @allure.story('Login with incorrect data')
    def test_login_with_non_existing_user_check_error_msg(self):
        user_login_response = MyRequests.post('/login', data=TD.UNREGISTERED_USER_DATA)
        Assertions.assert_json_value_by_name(user_login_response, 'error', 'user not found')

    @allure.story('Login with incorrect data')
    @pytest.mark.parametrize('data', TD.MISSING_REQUIRED_DATA)
    def test_login_without_required_data(self, data):
        user_login_response = MyRequests.post('/login', data=data)
        Assertions.assert_code_status(user_login_response, 400)

    @allure.story('Login with incorrect data')
    @pytest.mark.parametrize('data', TD.MISSING_REQUIRED_DATA)
    def test_login_without_required_data_check_no_token(self, data):
        user_login_response = MyRequests.post('/login', data=data)
        Assertions.assert_json_has_not_key(user_login_response, 'token')

    @allure.story('Login with incorrect data')
    @pytest.mark.parametrize('data', TD.MISSING_REQUIRED_DATA)
    def test_login_without_required_data_check_error(self, data):
        user_login_response = MyRequests.post('/login', data=data)
        Assertions.assert_json_has_key(user_login_response, 'error')

    @allure.story('Login with incorrect data')
    @pytest.mark.parametrize('data, expected_msg', zip(TD.MISSING_REQUIRED_DATA, TD.MISSING_REQUIRED_DATA_ERRORS))
    def test_login_without_required_data_check_error_msg(self, data, expected_msg):
        user_login_response = MyRequests.post('/login', data=data)
        Assertions.assert_json_value_by_name(user_login_response, 'error', expected_msg)

    @allure.story('Login with incorrect data')
    def test_login_incorrect_password(self):
        user_login_response = MyRequests.post('/login', data=TD.USER_WITH_INCORRECT_PASSWORD)
        Assertions.assert_code_status(user_login_response, 400)

    @allure.story('Login with incorrect data')
    def test_login_incorrect_password_check_no_token(self):
        user_login_response = MyRequests.post('/login', data=TD.USER_WITH_INCORRECT_PASSWORD)
        Assertions.assert_json_has_not_key(user_login_response, 'token')
