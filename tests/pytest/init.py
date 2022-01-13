import requests
import config
import allure
import json

def get_endpoint(slug):
    return config.DOMAIN + slug


def get_request(url):
    """Отправка get-запроса"""
    response = requests.get(url)
    return response


def post_request(url, request_body):
    response = requests.post(url, json=request_body)
    return response


def send_request(slug, method=None, request_body=None, attach=True):
    """Метод отправки запроса."""
    response = None
    url = get_endpoint(slug)
    if method == "get" or method == "GET":
        response = get_request(url)
    elif method == "post" or method == "POST":
        response = post_request(url, request_body=request_body)
    if attach:
        add_attachments(url, request_body, response, method)
    return response


def add_attachments(url, request_body, response, method):
    """Добавление к отчету вложений"""
    allure.attach(
        name=f"Request {method} {url}",
        body=json.dumps(request_body, ensure_ascii=False),
        attachment_type=allure.attachment_type.JSON
    )
    allure.attach(
        name=f"Response with code {response.status_code}",
        body=response.text,
        attachment_type=allure.attachment_type.JSON
    )