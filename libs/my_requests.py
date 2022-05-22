import requests
import allure


class MyRequests:

    @staticmethod
    def post(url: str, data: dict):
        url = f'https://reqres.in/api{url}'
        with allure.step(f'POST request to {url}'):
            return requests.post(url=url, data=data)

    @staticmethod
    def get(url: str, params: dict):
        url = f'https://reqres.in/api{url}'
        with allure.step(f'GET request to {url}'):
            return requests.get(url=url, params=params)

    @staticmethod
    def delete(url: str):
        url = f'https://reqres.in/api{url}'
        with allure.step(f'DELETE request to {url}'):
            return requests.delete(url=url)
