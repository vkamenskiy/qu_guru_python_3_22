import os

import pytest
from dotenv import load_dotenv
from selene.support.shared import browser

from config import Hosts
from utils.base_session import BaseSession

load_dotenv()

LOGIN = os.getenv("DEMOSHOP_LOGIN")
PASSWORD = os.getenv("DEMOSHOP_PASSWORD")


def pytest_addoption(parser):
    parser.addoption("--env")


@pytest.fixture(scope="session")
def env(request):
    return request.config.getoption("--env")


@pytest.fixture(scope='session')
def demoshop(env):
    api_url = Hosts(env).demoqa
    return BaseSession(api_url)


@pytest.fixture(scope='session')
def reqres(env):
    api_url = Hosts(env).reqres
    return BaseSession(api_url)


@pytest.fixture(scope='session')
def demoshop_browser(demoshop):
    response = demoshop.post(
        "/login",
        json={"Email": LOGIN, "Password": PASSWORD},
        allow_redirects=False,
    )
    authorization_cookie = response.cookies.get("NOPCOMMERCE.AUTH")

    browser.open("/Themes/DefaultClean/Content/images/logo.png")

    browser.driver.add_cookie(
        {"name": "NOPCOMMERCE.AUTH", "value": authorization_cookie}
    )
