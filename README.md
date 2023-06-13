# Rostelecom
Files:
conftest.py contains all the required code to catch failed test cases and make screenshot of the page in case any test case will fail.

pages/base.py contains PageObject pattern implementation for Python.

pages/elements.py contains helper class to define web elements on web pages.

tests/test_auth_page.py contains several tests for Rostelekom
(https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login&response_type=code&scope=openid&state=9f5cd20b-4285-44fc-87ee-86e56cfe8175&theme&auth_type)

How to run tests:
Install all requirements:

pip3 install -r requirements

Download Selenium WebDriver from https://chromedriver.chromium.org/downloads (choose version which is compatible with your browser)

Run tests:

python3 -m pytest -v --driver Chrome --driver-path ~/chrome tests/*
