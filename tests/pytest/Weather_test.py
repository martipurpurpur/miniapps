import pytest
from init import send_request
import allure


class TestWeather:
    url_get = '/weather/'
    url_post = '/weather/update/'
    method_get = 'GET'
    method_post = 'POST'

    def test_correct_response(self):
        """1. Получаем страницу с приложением погоды"""
        # WHEN
        status_code = 200
        # THEN
        response = send_request(
            slug=TestWeather.url_get,
            method=TestWeather.method_get
        )
        # AFTER
        with allure.step(f"Проверка на код {status_code}"):
            assert response.status_code == status_code


