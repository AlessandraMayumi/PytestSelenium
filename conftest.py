import os
import pytest
from selenium import webdriver
from datetime import datetime


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    if not os.path.exists('reports'):
        os.makedirs('reports')
    config.option.htmlpath = 'reports/'+datetime.now().strftime("%d-%m-%Y %H-%M-%S")+".html"


@pytest.fixture(params=["chrome", "firefox"])
def browser(request):
    if request.param == "chrome":
        driver = webdriver.Chrome(executable_path='drivers/chromedriver')
    if request.param == "firefox":
        driver = webdriver.Firefox(executable_path='drivers/geckodriver', service_log_path='reports/geckodriver.log')
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    driver.quit()
