import pytest
from test_data.test_data import TestDataUserAuthentication as TD
from libs.assertions import Assertions
import allure
from libs.my_requests import MyRequests


@allure.epic('Registration')
class TestUserRegister:

    @allure.story('Register a user with correct data')
    def test_register_new_user_successfully(self):
        user_register_response = MyRequests.post('/register', data=TD.USER_DATA)
        Assertions.assert_code_status(user_register_response, 200)

    @allure.story('Register a user with correct data')
    def test_register_new_user_successfully_check_id(self):
        user_register_response = MyRequests.post('/register', data=TD.USER_DATA)
        Assertions.assert_json_has_key(user_register_response, 'id')

    @allure.story('Register a user with correct data')
    def test_register_new_user_successfully_check_token(self):
        user_register_response = MyRequests.post('/register', data=TD.USER_DATA)
        Assertions.assert_json_has_key(user_register_response, 'token')

    # неактуальная проверка для тестового сайта
    # def test_create_user_with_existing_email(self):
    #     user_register_response = MyRequests.post('/register', data=TD.REGISTERED_USER_DATA)
    #     Assertions.assert_code_status(user_register_response, 400)

    @allure.story('Register a user with incorrect data')
    @pytest.mark.parametrize('data', TD.MISSING_REQUIRED_DATA)
    def test_register_user_without_required_data(self, data):
        user_register_response = MyRequests.post('/register', data=data)
        Assertions.assert_code_status(user_register_response, 400)

    @allure.story('Register a user with incorrect data')
    @pytest.mark.parametrize('data', TD.MISSING_REQUIRED_DATA)
    def test_register_user_without_required_data_check_no_token(self, data):
        user_register_response = MyRequests.post('/register', data=data)
        Assertions.assert_json_has_not_key(user_register_response, 'token')

    @allure.story('Register a user with incorrect data')
    @pytest.mark.parametrize('data', TD.MISSING_REQUIRED_DATA)
    def test_register_user_without_required_data_check_error(self, data):
        user_register_response = MyRequests.post('/register', data=data)
        Assertions.assert_json_has_key(user_register_response, 'error')

    @allure.story('Register a user with incorrect data')
    @pytest.mark.parametrize('data, expected_msg', zip(TD.MISSING_REQUIRED_DATA, TD.MISSING_REQUIRED_DATA_ERRORS))
    def test_register_user_without_required_data_check_error_msg(self, data, expected_msg):
        user_register_response = MyRequests.post('/register', data=data)
        Assertions.assert_json_value_by_name(user_register_response, 'error', expected_msg)
