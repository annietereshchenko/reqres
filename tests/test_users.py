from datetime import datetime
import pytest
from test_data.test_data import TestDataUsers as TD
from libs.assertions import Assertions
from libs.my_requests import MyRequests
import allure


@allure.epic('Users')
class TestUsers:
    @allure.feature('Create user')
    @allure.story('Create user with correct data')
    def test_create_user_successfully(self):
        create_user_response = MyRequests.post('/users', data=TD.CREATE_USER)
        Assertions.assert_code_status(create_user_response, 201)

    @allure.feature('Create user')
    @allure.story('Create user with correct data')
    def test_create_user_successfully_check_id(self):
        create_user_response = MyRequests.post('/users', data=TD.CREATE_USER)
        Assertions.assert_json_has_key(create_user_response, 'id')

    @allure.feature('Create user')
    @allure.story('Create user with correct data')
    def test_create_user_successfully_check_name(self):
        create_user_response = MyRequests.post('/users', data=TD.CREATE_USER)
        Assertions.assert_json_has_key(create_user_response, 'name')

    @allure.feature('Create user')
    @allure.story('Create user with correct data')
    def test_create_user_successfully_check_job(self):
        create_user_response = MyRequests.post('/users', data=TD.CREATE_USER)
        Assertions.assert_json_has_key(create_user_response, 'job')

    @allure.feature('Create user')
    @allure.story('Create user with correct data')
    def test_create_user_successfully_check_created_date(self):
        create_user_response = MyRequests.post('/users', data=TD.CREATE_USER)
        Assertions.assert_json_has_key(create_user_response, 'createdAt')

    @allure.feature('Create user')
    @allure.story('Create user with correct data')
    def test_create_user_successfully_check_name_in_response(self):
        create_user_response = MyRequests.post('/users', data=TD.CREATE_USER)
        Assertions.assert_json_value_by_name(create_user_response, 'name', TD.USER_NAME)
        print(create_user_response.status_code)
        print(create_user_response.content)

    @allure.feature('Create user')
    @allure.story('Create user with correct data')
    def test_create_user_successfully_check_job_in_response(self):
        create_user_response = MyRequests.post('/users', data=TD.CREATE_USER)
        Assertions.assert_json_value_by_name(create_user_response, 'job', TD.USER_JOB)

    @allure.feature('Create user')
    @allure.story('Create user with correct data')
    def test_create_user_successfully_check_created_date_in_response(self):
        create_user_response = MyRequests.post('/users', data=TD.CREATE_USER)
        expected_date = datetime.utcnow().strftime("%Y-%m-%d")
        Assertions.assert_expected_value_in_json_value_by_name(create_user_response, 'createdAt', expected_date)

    @allure.feature('Create user')
    @allure.story('Create user with incorrect data')
    @pytest.mark.parametrize('data', TD.MISSING_REQUIRED_DATA)
    @pytest.mark.xfail
    # The expected result is unknown, TBD
    def test_create_user_without_required_data(self, data):
        create_user_response = MyRequests.post('/users', data=data)
        Assertions.assert_code_status(create_user_response, 400)

    @allure.feature('Delete user')
    @allure.story('Delete user with correct data')
    def test_delete_user_successfully(self):
        delete_user_response = MyRequests.delete('/users/2')
        Assertions.assert_code_status(delete_user_response, 204)
